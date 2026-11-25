# СР №1 — Комплексний аудит OWASP (OWASP Juice Shop 20.4.0)

Матеріали самостійної роботи: комплексний аудит безпеки веб-застосунку за методологією
**OWASP Top 10:2025**, усунення знайдених вразливостей та повторне тестування.

> ⚠️ Навчальна лабораторія. Усі тести виконувалися **лише на локальному стенді**
> (loopback `127.0.0.1`), без сторонніх користувачів і не в продакшені. Секрети
> (токени, приватні ключі, паролі) до репозиторію **не включені**.

## Об'єкт і стенд
- **ДО** (вразлива версія): `http://localhost:3000` — незмінений OWASP Juice Shop 20.4.0.
- **ПІСЛЯ** (захищена версія): `https://localhost:8443` — реверс-проксі nginx + виправлений застосунок (`:3001`).

## Результат
- Виявлено **19 знахідок**, що покривають **усі 10 категорій** OWASP Top 10:2025.
- Оцінка за **OWASP Risk Rating** та **CVSS 3.1** (4 критичні, кілька високих).
- Усунення: **15 патчів** у коді (маркери `SR1-FIX`) + захисний реверс-проксі.
- Повторне тестування: **16/16 → 0/16** PoC; активний скан ZAP більше не знаходить SQLi та відкритого редиректу; регресії немає.

## Структура
| Шлях | Опис |
|---|---|
| `poc/manual_tests.py` | Ручна валідація знахідок (аналог Burp Repeater), ДО/ПІСЛЯ |
| `poc/http_exchange.py` | Демонстрація HTTP-обміну для окремих PoC (секрети маскуються) |
| `scripts/run_zap_local.sh` | Запуск ZAP Baseline/Full Scan (локально, аналог docker exec) |
| `hardening/nginx.conf` | Захисний реверс-проксі (HSTS, CSP, rate-limit, закриті службові шляхи) |
| `tools/parse_zap_xml_v2.py` | Парсер звітів ZAP, мапінг CWE→OWASP 2025, порівняння до/після |
| `tools/alert_monitor.py` | Аналізатор журналу доступу: сповіщення про brute-force/сканер (A09) |
| `patches/juice-shop-sr1-fixes.diff` | Патч оригінал → виправлена версія |
| `artifacts/` | Звіти ZAP (html/xml/json), результати PoC, nikto/nmap/npm audit |
| `docs/screenshots/` | Скриншоти для звіту |
| `report/` | Генератор звіту `.docx` |

## Джерела
- OWASP Top 10:2025 — https://owasp.org/Top10/2025/
- OWASP Risk Rating — https://owasp.org/www-community/OWASP_Risk_Rating_Methodology
- CVSS 3.1 — https://www.first.org/cvss/v3.1/specification-document
- OWASP ZAP — https://www.zaproxy.org/docs/
- OWASP Juice Shop — https://owasp.org/www-project-juice-shop/
