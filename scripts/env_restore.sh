#!/usr/bin/env bash
# Відновлення лабораторного середовища після перезапуску ВМ:
# nginx, точка монтування /zap, ціль "ДО" (:3000) та захищена версія (:8443)
ROOT=/home/ubuntu/sr1
command -v nginx >/dev/null || [ -x /usr/sbin/nginx ] || { sudo -n apt-get install -y -q nginx >/dev/null 2>&1 || { sudo -n apt-get update -q >/dev/null 2>&1; sudo -n apt-get install -y -q nginx >/dev/null 2>&1; }; }
sudo -n systemctl stop nginx 2>/dev/null; sudo -n pkill -x nginx 2>/dev/null
sudo -n ln -sfn $ROOT/tools_dl/ZAP_2.17.0 /zap
export PATH=$PATH:/usr/sbin
if ! curl -s -o /dev/null http://127.0.0.1:3000/; then
  cd $ROOT/tools_dl/juice-shop_20.4.0-SNAPSHOT && PORT=3000 setsid nohup node build/app.js > $ROOT/js_before.log 2>&1 < /dev/null &
fi
bash $ROOT/scripts/start_hardened.sh
until curl -s -o /dev/null http://127.0.0.1:3000/; do sleep 2; done; echo "before: http://localhost:3000"
