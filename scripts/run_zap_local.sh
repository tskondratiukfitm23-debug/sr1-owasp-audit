#!/usr/bin/env bash
# Запуск ZAP Baseline / Full Scan без Docker (локальна інсталяція ZAP 2.17.0, змонтована в /zap).
# Аналог scripts/run_baseline.sh та run_fullscan.sh викладача (там — docker exec).
# Використання:
#   MODE=baseline|full TARGET=http://localhost:3000 TAG=before [ROLE_TOKEN=<jwt>] bash scripts/run_zap_local.sh
set -euo pipefail
MODE=${MODE:-baseline}; TARGET=${TARGET:-http://localhost:3000}; TAG=${TAG:-run}
WRK=/zap/wrk; HOME_DIR=/home/ubuntu/sr1/.zaphome/$TAG; mkdir -p "$HOME_DIR"
export IS_CONTAINERIZED=true
Z="-dir $HOME_DIR -config spider.maxDuration=3 -config ajaxSpider.browserId=firefox-headless"
if [ -n "${ROLE_TOKEN:-}" ]; then   # автентифікований скан: replacer додає заголовок Authorization до кожного запиту
  Z="$Z -config replacer.full_list(0).description=auth -config replacer.full_list(0).enabled=true \
 -config replacer.full_list(0).matchtype=REQ_HEADER -config replacer.full_list(0).matchstr=Authorization \
 -config replacer.full_list(0).regex=false -config replacer.full_list(0).replacement=Bearer\ $ROLE_TOKEN"
fi
cd "$WRK"
date -Is > "$TAG.ts"
if [ "$MODE" = full ]; then
  Z="$Z -config scanner.maxScanDurationInMins=${MAXMIN:-12} -config scanner.threadPerHost=4"
  python3 /zap/zap-full-scan.py -t "$TARGET" -j -m 3 -r "zap-$TAG.html" -x "zap-$TAG.xml" -J "zap-$TAG.json" -w "zap-warn-$TAG.md" -z "$Z" > "$TAG.out" 2>&1 || true
else
  python3 /zap/zap-baseline.py -t "$TARGET" -j -m 3 -r "zap-$TAG.html" -x "zap-$TAG.xml" -J "zap-$TAG.json" -w "zap-warn-$TAG.md" -z "$Z" > "$TAG.out" 2>&1 || true
fi
date -Is >> "$TAG.ts"
# прибрати токени з артефактів (секрети не мають потрапляти у звіт/репозиторій)
sed -i -E 's/eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/<JWT-REDACTED>/g' "$WRK"/zap-$TAG.* "$WRK/$TAG.out" "$WRK/zap.yaml" 2>/dev/null || true
grep -E '^(FAIL|WARN)-NEW|^FAIL-NEW' "$TAG.out" | tail -40
