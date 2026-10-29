# -*- coding: utf-8 -*-
import json, re, sys
sys.path.insert(0, '/home/claude')
from reading_data import PASSAGES
from furigana import full_furigana
KAN = re.compile(r'[一-鿿々]')

out = []
for p in PASSAGES:
    paras = [full_furigana(x) for x in p['body'].split('\n') if x.strip()]
    out.append({"id": p['id'], "t": p['tier'], "ti": p['title'],
                "p": paras, "en": p['en'],
                "q": [{"q": q['q'], "o": q['opts'], "a": q['ans'], "w": q['why']} for q in p['qs']]})
json.dump(out, open('reading_packed.json','w',encoding='utf-8'), ensure_ascii=False, separators=(',',':'))

bad = 0
for p, o in zip(PASSAGES, out):
    plain = ''.join(t for para in o['p'] for t, _ in para)
    want = ''.join(p['body'].split('\n'))
    if plain.replace('　','') != want.replace('　',''):
        print('✗ text changed by furigana:', p['id']); bad += 1
    for para in o['p']:
        for t, r in para:
            if r is None and KAN.search(t): print(f'  ! {p["id"]}: no reading over 「{t}」'); bad += 1
print(f'passages {len(out)} | questions {sum(len(x["q"]) for x in out)} | '
      f'KB {round(len(json.dumps(out,ensure_ascii=False).encode())/1024,1)} | problems {bad}')
for o in out[:1]:
    print('\nsample:', ''.join(f'{t}[{r}]' if r else t for t,r in o['p'][0]))
