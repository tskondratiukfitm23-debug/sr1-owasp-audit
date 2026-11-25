import json, sys
for f in sys.argv[1:]:
    d = json.load(open(f))
    print(f, d['time'], d.get('regression'))
    for r in d['results']:
        print(' ', r['id'], r['status'], '|', r['evidence'])
