#!/usr/bin/env bash
# Послідовний запуск сканів (по одному екземпляру ZAP, обмежена пам'ять JVM)
cd /home/ubuntu/sr1; source .tokens.env
export _JAVA_OPTIONS=-Xmx4g
MODE=full MAXMIN=8 TAG=before-full TARGET=http://localhost:3000 ROLE_TOKEN=$CUST_B bash scripts/run_zap_local.sh
MODE=full MAXMIN=8 TAG=after-full TARGET=https://localhost:8443 ROLE_TOKEN=$CUST_A bash scripts/run_zap_local.sh
MODE=baseline TAG=before-admin TARGET=http://localhost:3000 ROLE_TOKEN=$ADMIN_B bash scripts/run_zap_local.sh
echo ALLDONE
