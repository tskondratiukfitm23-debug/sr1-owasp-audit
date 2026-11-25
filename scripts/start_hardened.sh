#!/usr/bin/env bash
# Запуск виправленої версії: Juice Shop (патчі SR1-FIX) на 127.0.0.1:3001 + nginx (TLS, заголовки, rate-limit) на :8443
set -euo pipefail
ROOT=/home/ubuntu/sr1
cd $ROOT/app/juice-shop
for p in $(pgrep -f "node build/app.js" || true); do tr '\0' '\n' < /proc/$p/environ | grep -q '^PORT=3001' && kill $p || true; done
sleep 1
JWT_PRIVATE_KEY_FILE=$ROOT/hardening/secrets/jwt.key PORT=3001 setsid nohup node build/app.js > $ROOT/js_after.log 2>&1 < /dev/null &
until curl -s -o /dev/null http://127.0.0.1:3001/; do sleep 2; done
python3 $ROOT/scripts/rotate_admin.py          # Juice Shop пересіює БД при старті → змінюємо стандартний пароль адміністратора
pgrep -x nginx >/dev/null || setsid nginx -p $ROOT/hardening -c nginx.conf
echo "hardened: https://localhost:8443"
