#!/usr/bin/env python3
"""Зведена таблиця ручних PoC: статус ДО vs ПІСЛЯ по кожній знахідці."""
import json
b = {r['id']: r for r in json.load(open('artifacts/before/manual_before.json'))['results']}
a = {r['id']: r for r in json.load(open('artifacts/after/manual_after.json'))['results']}
R = '\033[31m'; G = '\033[32m'; N = '\033[0m'; B = '\033[1m'
print(f"{B}ID     OWASP      ДО (:3000)    ПІСЛЯ (:8443)  Назва{N}")
for i in sorted(b):
    bs = b[i]['status']; as_ = a.get(i, {}).get('status', '—')
    bc = f'{R}ВРАЗЛИВО {N}' if bs == 'VULNERABLE' else f'{G}виправлено{N}'
    ac = f'{R}ВРАЗЛИВО {N}' if as_ == 'VULNERABLE' else f'{G}ВИПРАВЛЕНО{N}'
    print(f"{i}   {b[i]['owasp']:<9}  {bc}     {ac}     {b[i]['title'][:42]}")
nb = sum(r['status'] == 'VULNERABLE' for r in b.values())
na = sum(r['status'] == 'VULNERABLE' for r in a.values())
print(f"\n{B}Разом вразливих: ДО = {R}{nb}/16{N}{B}   ПІСЛЯ = {G}{na}/16{N}")
