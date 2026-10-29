# -*- coding: utf-8 -*-
"""Pack passages as paragraphs of sentences: each sentence carries its own
furigana runs and its own English, so the page can interleave them."""
import json, re, sys
sys.path.insert(0, '/home/claude')
from reading_data import PASSAGES as _P1
from reading_n2   import PASSAGES as _P2
from reading_n2b  import PASSAGES as _P3
from reading_n2c  import PASSAGES as _P4
from reading_n2e  import PASSAGES as _P5
from reading_sent_en import SENT_EN
from furigana import full_furigana
PASSAGES = _P1 + _P2 + _P3 + _P4 + _P5
KAN = re.compile(r'[一-鿿々]')

def split_jp(line):
    """Sentences, keeping a closing bracket with the sentence it ends."""
    return [x for x in re.findall(r'[^。？！]*[。？！]+[）」』]?|[^。？！]+$', line) if x.strip()]

def split_en(t):
    return [x.strip() for x in re.findall(r'[^.?!]*[.?!]+[”")]*', t.replace('\n',' ')) if x.strip()]

out, problems = [], []
for p in PASSAGES:
    paras, flat = [], []
    for line in p['body'].split('\n'):
        line = line.strip()
        if not line: continue
        sents = split_jp(line)
        paras.append(sents); flat.extend(sents)
    en = SENT_EN.get(p['id']) or split_en(p['en'])
    if len(en) != len(flat):
        problems.append(f"{p['id']}: {len(flat)} Japanese sentences but {len(en)} English")
        en = en + [''] * (len(flat) - len(en))
    k = 0; packed = []
    for sents in paras:
        row = []
        for s in sents:
            runs = full_furigana(s)
            if ''.join(t for t, _ in runs) != s:
                problems.append(f"{p['id']}: furigana changed the text")
            row.append({"r": runs, "e": en[k]}); k += 1
        packed.append(row)
    tb = p.get('table')
    tbl = None
    if tb:
        tbl = {"head": [full_furigana(c) if c else [] for c in tb['head']],
               "rows": [[full_furigana(c) for c in row] for row in tb['rows']]}
    out.append({"id": p['id'], "t": p['tier'], "ti": p['title'], "k": p.get('kind',''),
                "p": packed, "en": p['en'], "tb": tbl,
                "q": [{"q": q['q'], "o": q['opts'], "a": q['ans'], "w": q['why']} for q in p['qs']]})

json.dump(out, open('reading_packed.json','w',encoding='utf-8'), ensure_ascii=False, separators=(',',':'))
ns = sum(len(r) for x in out for r in x['p'])
blank = sum(1 for x in out for r in x['p'] for s in r if not s['e'].strip())
print(f'passages {len(out)} | sentences {ns} | questions {sum(len(x["q"]) for x in out)} | '
      f'KB {round(len(json.dumps(out,ensure_ascii=False).encode())/1024,1)}')
print(f'sentences without English: {blank}')
print(f'PROBLEMS {len(problems)}')
for q in problems: print('  ✗', q)
sys.exit(1 if problems else 0)
