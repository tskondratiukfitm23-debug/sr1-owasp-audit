ZAP 2.17.0, Wed, 25 Nov 2026 21:21:21

| Ризик | Довіра | Сповіщення | CWE | OWASP 2025 | К-сть | Приклад URL |
|---|---|---|---|---|---|---|
| High | Medium | Off-site Redirect | 601 | A01 | 1 | http://localhost:3000/redirect?to=https://github.com/juice-s |
| Medium | High | Content Security Policy (CSP) Header Not Set | 693 | A02 | 5 | http://localhost:3000 |
| Medium | Medium | Cross-Domain Misconfiguration | 264 | A01 | 5 | http://localhost:3000/assets/public/favicon_js.ico |
| Medium | Medium | Missing Anti-clickjacking Header | 1021 | A02 | 3 | http://localhost:3000/socket.io/?EIO=4&transport=polling&t=m |
| Medium | High | Session ID in URL Rewrite | 598 | A01 | 5 | http://localhost:3000/socket.io/?EIO=4&transport=polling&t=m |
| Low | Medium | Application Error Disclosure | 550 | A10 | 1 | http://localhost:3000/rest/user/reset-password |
| Low | Medium | Cross-Origin-Embedder-Policy Header Missing or Invalid | 693 | A02 | 5 | http://localhost:3000 |
| Low | Medium | Cross-Origin-Opener-Policy Header Missing or Invalid | 693 | A02 | 5 | http://localhost:3000 |
| Low | Low | Dangerous JS Functions | 749 | A05 | 3 | http://localhost:3000/about.component-HWmrgSem.js |
| Low | Medium | Deprecated Feature Policy Header Set | 16 | A02 | 5 | http://localhost:3000/chunk-CE5v8pBj.js |
| Low | Medium | Private IP Disclosure | 497 | A02 | 1 | http://localhost:3000/rest/admin/application-configuration |
| Low | Low | Timestamp Disclosure - Unix | 497 | A02 | 4 | http://localhost:3000/rest/admin/application-configuration |
| Low | Medium | X-Content-Type-Options Header Missing | 693 | A02 | 5 | http://localhost:3000/socket.io/?EIO=4&transport=polling&t=m |
| Informational | High | Information Disclosure - Information in Browser sessionStorage | 359 | A06 | 1 | http://localhost:3000/#/basket |
| Informational | Medium | Information Disclosure - Sensitive Information in URL | 598 | A01 | 1 | http://localhost:3000/rest/user/security-question?email=foo- |
| Informational | Medium | Modern Web Application | -1 | — | 5 | http://localhost:3000 |
| Informational | Medium | Storable and Cacheable Content | 524 | A02 | 1 | http://localhost:3000/robots.txt |
| Informational | Medium | Storable but Non-Cacheable Content | 524 | A02 | 5 | http://localhost:3000/assets/public/favicon_js.ico |
