# -*- coding: utf-8 -*-
"""A ruby is correct if ruby + the okurigana that follows it forms a real JMdict reading."""
import json, re, collections
from jamdict import Jamdict
jam = Jamdict()
deck = json.load(open('deck_all.json', encoding='utf-8'))
ALLKAN = re.compile(r'^[一-鿿々]+$')
KANA = re.compile(r'^[぀-ゟ]+')
cache = {}
def reads(word):
    if word not in cache:
        res = jam.lookup(word, strict_lookup=True)
        cache[word] = {f.text for en in res.entries if word in {x.text for x in en.kanji_forms}
                       for f in en.kana_forms}
    return cache[word]

real, okuri, unknown, good = [], 0, 0, 0
for e in deck:
    for i, s in enumerate(e['sents']):
        runs = s['furi']
        for j, (t, r) in enumerate(runs):
            if not (r and ALLKAN.match(t) and len(t) >= 2): continue
            if r in reads(t): good += 1; continue
            # try absorbing the okurigana that follows
            tail = ''
            nxt = runs[j+1][0] if j+1 < len(runs) and runs[j+1][1] is None else ''
            m = KANA.match(nxt or '')
            matched = False
            if m:
                for n in range(1, len(m.group(0))+1):
                    tail = m.group(0)[:n]
                    if (r + tail) in reads(t + tail): matched = True; break
            if matched: okuri += 1
            elif not reads(t): unknown += 1
            else: real.append((t, r, sorted(reads(t))[:3], e['k'], s['plain']))

print(f'ruby exactly matches a JMdict reading      : {good}')
print(f'correct once okurigana is absorbed         : {okuri}')
print(f'compound is not a JMdict headword (skipped): {unknown}')
print(f'GENUINELY WRONG                            : {len(real)}')
for t, r, rd, k, sent in real:
    print(f'  ✗ {t}[{r}]  JMdict {rd}  (「{k}」)  {sent}')
