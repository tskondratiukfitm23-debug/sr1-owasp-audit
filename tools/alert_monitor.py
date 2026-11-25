#!/usr/bin/env python3
"""A09: простий детектор атак за JSON-журналом nginx (hardening/logs/access.jsonl).
Правила (вікно 60 с, на одну IP):
  R1 brute-force  — >=5 відповідей 401/429 на /rest/user/login
  R2 forbidden    — >=3 звернення до закритих ресурсів (403 на /ftp, /metrics, ...)
  R3 scanner      — >=50 відповідей 4xx (сканування/фазинг)
Сповіщення пишуться в alerts.jsonl і друкуються в консоль.
Використання: python3 tools/alert_monitor.py hardening/logs/access.jsonl [--since-min 30]
"""
import json, sys
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone

path = sys.argv[1] if len(sys.argv) > 1 else 'hardening/logs/access.jsonl'
since = int(sys.argv[sys.argv.index('--since-min') + 1]) if '--since-min' in sys.argv else 10 ** 6
cut = datetime.now(timezone.utc) - timedelta(minutes=since)
RULES = {'R1 brute-force': 5, 'R2 forbidden': 3, 'R3 scanner': 50}
win = defaultdict(deque); fired = {}; alerts = []; total = 0

for line in open(path, encoding='utf-8', errors='replace'):
    try:
        e = json.loads(line)
    except ValueError:
        continue
    ts = datetime.fromisoformat(e['ts'])
    if ts < cut:
        continue
    total += 1
    rule = None
    if e['uri'] == '/rest/user/login' and e['status'] in (401, 429):
        rule = 'R1 brute-force'
    elif e['status'] == 403:
        rule = 'R2 forbidden'
    if 400 <= e['status'] < 500:
        for r in filter(None, [rule, 'R3 scanner']):
            q = win[(r, e['ip'])]; q.append(ts)
            while q and ts - q[0] > timedelta(seconds=60):
                q.popleft()
            last = fired.get((r, e['ip']))
            if len(q) >= RULES[r] and (last is None or ts - last > timedelta(seconds=60)):
                fired[(r, e['ip'])] = ts
                a = {'ts': e['ts'], 'rule': r, 'ip': e['ip'], 'count_60s': len(q), 'sample_uri': e['uri'],
                     'severity': 'HIGH' if r.startswith('R1') else 'MEDIUM'}
                alerts.append(a)

with open('hardening/logs/alerts.jsonl', 'a', encoding='utf-8') as f:
    for a in alerts:
        f.write(json.dumps(a, ensure_ascii=False) + '\n')
print(f'Проаналізовано записів: {total}; сповіщень: {len(alerts)}')
for a in alerts[-15:]:
    print(f"[ALERT {a['severity']:<6}] {a['ts']}  {a['rule']:<15} ip={a['ip']}  подій за 60с={a['count_60s']}  напр. {a['sample_uri']}")
by = defaultdict(int)
for a in alerts:
    by[a['rule']] += 1
print('За правилами:', dict(by))
