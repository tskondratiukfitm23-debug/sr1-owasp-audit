#!/usr/bin/env python3
"""Покращений парсер ZAP XML (ZAP 2.10+ зберігає URL/параметри всередині <instances>,
тому вихідний tools/parse_zap_xml.py виводить порожні колонки URL/Param).
Додає мапінг CWE → OWASP Top 10:2025 та порівняння «до/після».

  python3 tools/parse_zap_xml_v2.py report.xml [--out artifacts/x] [--compare after.xml]
"""
import csv, sys, xml.etree.ElementTree as ET
from pathlib import Path

CWE_2025 = {  # основні CWE, які видає ZAP → категорія OWASP Top 10:2025
    '601': 'A01', '639': 'A01', '918': 'A01', '264': 'A01', '284': 'A01', '598': 'A01',
    '693': 'A02', '1021': 'A02', '16': 'A02', '497': 'A02', '524': 'A02', '525': 'A02', '615': 'A02', '200': 'A02',
    '1104': 'A03', '1395': 'A03', '829': 'A08',
    '319': 'A04', '311': 'A04', '326': 'A04', '614': 'A04',
    '79': 'A05', '89': 'A05', '78': 'A05', '943': 'A05', '749': 'A05',
    '359': 'A06', '352': 'A01', '287': 'A07', '384': 'A07', '1004': 'A07',
    '550': 'A10', '209': 'A10', '388': 'A10',
}
RISK_ORDER = {'High': 0, 'Medium': 1, 'Low': 2, 'Informational': 3}


def load(path):
    root = ET.parse(path).getroot(); rows = []
    for a in root.findall('.//alertitem'):
        inst = a.findall('.//instance')
        first = inst[0] if inst else a
        cwe = a.findtext('cweid') or ''
        rows.append({
            'risk': (a.findtext('riskdesc') or '').split(' (')[0], 'confidence': (a.findtext('riskdesc') or '').split('(')[-1].rstrip(')'),
            'name': a.findtext('alert') or '', 'plugin': a.findtext('pluginid') or '', 'cwe': cwe,
            'owasp2025': CWE_2025.get(cwe, '—'), 'count': int(a.findtext('count') or len(inst) or 1),
            'url': first.findtext('uri') or '', 'param': first.findtext('param') or '',
            'evidence': (first.findtext('evidence') or '').replace('\n', ' ')[:80]})
    rows.sort(key=lambda r: (RISK_ORDER.get(r['risk'], 9), r['name']))
    return root.attrib.get('version', ''), root.attrib.get('generated', ''), rows


def main():
    src = sys.argv[1]; out = Path(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else Path('artifacts')
    out.mkdir(parents=True, exist_ok=True)
    ver, gen, rows = load(src); stem = Path(src).stem
    with open(out / f'{stem}.findings.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ['risk']); w.writeheader(); w.writerows(rows)
    with open(out / f'{stem}.findings.md', 'w', encoding='utf-8') as f:
        f.write(f'ZAP {ver}, {gen}\n\n| Ризик | Довіра | Сповіщення | CWE | OWASP 2025 | К-сть | Приклад URL |\n|---|---|---|---|---|---|---|\n')
        for r in rows:
            f.write(f"| {r['risk']} | {r['confidence']} | {r['name']} | {r['cwe']} | {r['owasp2025']} | {r['count']} | {r['url'][:60]} |\n")
    stat = {k: sum(r['risk'] == k for r in rows) for k in RISK_ORDER}
    print(f'ZAP {ver} | {gen} | {src}')
    print(f"{'Ризик':<14}{'Довіра':<8}{'OWASP':<7}{'CWE':<6}{'К-сть':<6}Сповіщення / приклад URL")
    for r in rows:
        print(f"{r['risk']:<14}{r['confidence']:<8}{r['owasp2025']:<7}{r['cwe']:<6}{r['count']:<6}{r['name'][:48]:<49}{r['url'].split('//')[-1][:46]}")
    print('Разом типів сповіщень:', len(rows), stat)
    if '--compare' in sys.argv:
        _, _, after = load(sys.argv[sys.argv.index('--compare') + 1])
        a_names = {r['name'] for r in after}; b_names = {r['name'] for r in rows}
        print(f'\nПорівняння з {sys.argv[sys.argv.index("--compare") + 1]}:')
        print('  Закрито  :', len(b_names - a_names), sorted(b_names - a_names))
        print('  Лишилось :', len(b_names & a_names), sorted(b_names & a_names))
        print('  Нові     :', len(a_names - b_names), sorted(a_names - b_names))


if __name__ == '__main__':
    main()
