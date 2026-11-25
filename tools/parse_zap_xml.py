import sys, xml.etree.ElementTree as ET, csv, json, os
p = sys.argv[1] if len(sys.argv)>1 else 'artifacts/zap-baseline.xml'
root = ET.parse(p).getroot()
alerts = root.findall('.//alertitem')
os.makedirs('artifacts', exist_ok=True)
with open('artifacts/findings.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['risk','name','url','param','attack','evidence'])
    for a in alerts:
        w.writerow([(a.findtext('riskdesc') or ''), (a.findtext('alert') or ''), (a.findtext('uri') or ''), (a.findtext('param') or ''), (a.findtext('attack') or ''), (a.findtext('evidence') or '')])
with open('artifacts/findings.md','w',encoding='utf-8') as f:
    f.write('| Risk | Name | URL | Param | Evidence |\n|---|---|---|---|---|\n')
    for a in alerts:
        f.write(f"| {a.findtext('riskdesc') or ''} | {a.findtext('alert') or ''} | {a.findtext('uri') or ''} | {a.findtext('param') or ''} | {a.findtext('evidence') or ''} |\n")
print('Wrote artifacts/findings.csv and artifacts/findings.md')
