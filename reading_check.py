# -*- coding: utf-8 -*-
import json, re, sys
sys.path.insert(0, '/home/claude')
from reading_data import PASSAGES as _P1
from reading_n2 import PASSAGES as _P2
from reading_n2b import PASSAGES as _P3
from reading_n2c import PASSAGES as _P4
PASSAGES = _P1 + _P2 + _P3 + _P4

lv = json.load(open('kanji_by_level.json', encoding='utf-8'))
TIERS = {'N5': set(lv['N5']),
         'N4': set(lv['N5']) | set(lv['N4']),
         'N3': set(lv['N5']) | set(lv['N4']) | set(lv['N3']),
         'N2': set(lv['N5']) | set(lv['N4']) | set(lv['N3']) | set(lv['N2'])}
KAN = re.compile(r'[一-鿿々]')
FOREIGN = re.compile('[' + ''.join(map(chr, list(range(0x0400,0x0500)) + list(range(0xAC00,0xD7B0)))) + ']')
LATIN = re.compile(r'[A-Za-z]')

fails = []
print(f'{"id":4} {"tier":5} {"chars":>6} {"kanji":>6}  title')
for p in PASSAGES:
    allow = TIERS[p['tier']]
    texts = [p['body']] + [q['q'] for q in p['qs']] + [o for q in p['qs'] for o in q['opts']]
    body_k = set(KAN.findall(p['body']))
    print(f'{p["id"]:4} {p["tier"]:5} {len(p["body"]):6} {len(body_k):6}  {p["title"]}')
    for t in texts:
        for k in set(KAN.findall(t)):
            if k not in allow:
                fails.append(f'{p["id"]} ({p["tier"]}): kanji 「{k}」 is above tier  … {t[:30]}')
        if FOREIGN.search(t): fails.append(f'{p["id"]}: FOREIGN SCRIPT in: {t[:40]}')
        if LATIN.search(t):   fails.append(f'{p["id"]}: LATIN LETTERS in: {t[:40]}')
    if not (0 <= p['qs'][0]['ans'] < 4): fails.append(f'{p["id"]}: bad answer index')
    for q in p['qs']:
        if len(q['opts']) != 4: fails.append(f'{p["id"]}: {len(q["opts"])} options, expected 4')
        if len(set(q['opts'])) != len(q['opts']): fails.append(f'{p["id"]}: duplicate options')
        if not q.get('why','').strip(): fails.append(f'{p["id"]}: no explanation')
    if not p.get('en','').strip(): fails.append(f'{p["id"]}: no translation')

print(f'\nFAILURES: {len(fails)}')
for f in fails: print('  ✗', f)
sys.exit(1 if fails else 0)
