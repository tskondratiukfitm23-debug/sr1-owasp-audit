#!/usr/bin/env python3
"""F-15: заміна стандартного пароля admin123 на випадковий (зберігається поза репозиторієм)."""
import os, secrets, requests
B = 'http://127.0.0.1:3001'; F = '/home/ubuntu/sr1/hardening/secrets/admin_password.txt'
npw = open(F).read().strip() if os.path.exists(F) else 'Adm!' + secrets.token_urlsafe(18)
r = requests.post(B + '/rest/user/login', json={'email': 'admin@juice-sh.op', 'password': 'admin123'})
if r.status_code == 200:
    t = r.json()['authentication']['token']
    c = requests.get(B + '/rest/user/change-password', params={'current': 'admin123', 'new': npw, 'repeat': npw},
                     headers={'Authorization': 'Bearer ' + t})
    open(F, 'w').write(npw + '\n'); os.chmod(F, 0o600)
    print('admin password rotated:', c.status_code)
else:
    print('admin password already non-default:', r.status_code)
