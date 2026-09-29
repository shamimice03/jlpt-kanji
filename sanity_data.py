# -*- coding: utf-8 -*-
import json, re, collections, sys
deck = json.load(open('deck_all.json', encoding='utf-8'))
kd   = json.load(open('kanji.json', encoding='utf-8'))
FAIL, WARN = [], []
def fail(m): FAIL.append(m)
def warn(m): WARN.append(m)

KAN   = re.compile(r'[一-鿿々]')
LATIN = re.compile(r'[a-zA-Z]')
FOREIGN = re.compile('[' + ''.join(map(chr, list(range(0x0400,0x0500)) + list(range(0xAC00,0xD7B0)))) + ']')
JPSENT = re.compile(r'^[぀-ヿ一-鿿々、。ー？！（）～]+$')
KANA  = re.compile(r'^[぀-ヿー、（）()\-ー]+$')

print(f'=== 1. STRUCTURE ===')
print(f'kanji {len(deck)} | vocab {sum(len(e["vocab"]) for e in deck)} | sentences {sum(len(e["sents"]) for e in deck)}')
ks = [e['k'] for e in deck]
if len(set(ks)) != len(ks):
    fail(f'duplicate kanji entries: {[k for k,c in collections.Counter(ks).items() if c>1]}')
ns = [e['n'] for e in deck]
if sorted(ns) != list(range(1, len(deck)+1)): fail('card numbers are not 1..N without gaps')
for e in deck:
    for f in ('k','on','kun','mean','vocab','sents'):
        if f not in e: fail(f'{e["k"]}: missing field {f}')
    if len(e['k']) != 1: fail(f'entry key is not a single character: {e["k"]!r}')
    if len(e['vocab']) != len(e['sents']): fail(f'{e["k"]}: {len(e["vocab"])} words vs {len(e["sents"])} sentences')
    if len(e['vocab']) < 2: warn(f'{e["k"]}: only {len(e["vocab"])} words')
    if (e.get('lvl') or 'N2') not in {'N5','N4','N3','N2','N1*'}: fail(f'{e["k"]}: bad level {e.get("lvl")}')

print(f'\n=== 2. READINGS vs KANJIDIC2 ===')
def k2h(s): return ''.join(chr(ord(c)-0x60) if 'ァ'<=c<='ヶ' else c for c in s)
bad_on = bad_kun = 0
for e in deck:
    v = kd.get(e['k'])
    if not v: fail(f'{e["k"]}: not in KANJIDIC2'); continue
    if e['on'] != '—':
        if not KANA.match(e['on']): fail(f'{e["k"]}: onyomi not kana: {e["on"]}')
        for r in e['on'].split('、'):
            n = k2h(r).replace('(','.').replace(')','')
            if n not in {x.rstrip('.-') for x in (v.get('readings_on') or [])} and n not in set(v.get('readings_on') or []): bad_on += 1; fail(f'{e["k"]}: onyomi {r} not in KANJIDIC2')
    if e['kun'] != '—':
        if not KANA.match(e['kun']): fail(f'{e["k"]}: kunyomi not kana: {e["kun"]}')
        kk = {x.strip('.-') for x in (v.get('readings_kun') or [])}
        for r in e['kun'].split('、'):
            n = k2h(r).replace('(','.').replace(')','').strip('.-').replace('.','')
            if n not in {x.replace('.','') for x in kk}: bad_kun += 1; fail(f'{e["k"]}: kunyomi {r} not in KANJIDIC2')
print(f'onyomi mismatches {bad_on} | kunyomi mismatches {bad_kun}')

print(f'\n=== 3. VOCAB & SENTENCES ===')
for e in deck:
    for v in e['vocab']:
        if e['k'] not in v['w']: fail(f'{e["k"]}: word {v["w"]} does not contain the kanji')
        if not KANA.match(v['r']): fail(f'{e["k"]}/{v["w"]}: reading not kana: {v["r"]}')
        if FOREIGN.search(v['w']) or FOREIGN.search(v['r']): fail(f'{e["k"]}/{v["w"]}: foreign script')
        if LATIN.search(v['w']): fail(f'{e["k"]}/{v["w"]}: latin letters in word')
        if not v.get('en','').strip(): fail(f'{e["k"]}/{v["w"]}: empty english')
        if v.get('lv') and v['lv'] not in {'N1','N2','N3','N4','N5'}: fail(f'{e["k"]}/{v["w"]}: bad list level {v["lv"]}')
    for s in e['sents']:
        # `jp` is the authored source, which may carry （readings）; `plain` is what the site shows
        stripped = re.sub(r'（[\u3040-\u30FF\u30FC]+）', '', s['jp'])
        if stripped != s['plain']: fail(f'{e["k"]}: jp source does not reduce to plain: {stripped} / {s["plain"]}')
        if not JPSENT.match(s['plain']) and s['plain'] != '血液型はA型です。': fail(f'{e["k"]}: non-Japanese chars in sentence: {s["plain"]}')
        if FOREIGN.search(s['plain']): fail(f'{e["k"]}: foreign script in sentence: {s["plain"]}')
        if LATIN.search(s['plain']) and s['plain'] != '血液型はA型です。': fail(f'{e["k"]}: latin letters in sentence: {s["plain"]}')
        if re.search(r'[0-9]', s['plain']): warn(f'{e["k"]}: ASCII digits in sentence: {s["plain"]}')
        if not s['plain'].endswith(('。','？','！')): fail(f'{e["k"]}: sentence lacks final punctuation: {s["plain"]}')
        if not s.get('en','').strip(): fail(f'{e["k"]}: sentence has no english: {s["plain"]}')
        if ''.join(t for t,_ in s['furi']) != s['plain']: fail(f'{e["k"]}: furi runs do not equal plain')
        for t, r in s['furi']:
            if r is not None:
                if not KAN.search(t): fail(f'{e["k"]}: ruby over non-kanji {t!r}={r!r}')
                if not KANA.match(r): fail(f'{e["k"]}: ruby is not kana: {r!r}')

print(f'\n=== 4. PAIRING (sentence i belongs to word i) ===')
def stems(w):
    out = {w, re.sub(r'[぀-ゟ]+$', '', w)}
    if w.endswith('する'): out.add(w[:-2])
    runs = KAN.findall(w)
    if runs: out.add(max(runs, key=len))
    return {x for x in out if x}
bad = [e['k'] for e in deck
       if not all(any(st in e['sents'][i]['plain'] for st in stems(e['vocab'][i]['w']))
                  for i in range(len(e['vocab'])))]
print('misaligned kanji:', len(bad), ''.join(bad))
if bad: fail(f'{len(bad)} kanji have sentences out of order')

print(f'\n=== 5. FURIGANA COVERAGE ===')
nokanji = tot = 0
for e in deck:
    for s in e['sents']:
        for t, r in s['furi']:
            if r is None and KAN.search(t): nokanji += 1
            tot += 1
print(f'runs with kanji but no reading: {nokanji}')
if nokanji: warn(f'{nokanji} kanji runs carry no furigana')

print(f'\n=== RESULT ===')
print(f'FAILURES {len(FAIL)}'); [print('  ✗', m) for m in FAIL[:40]]
if len(FAIL) > 40: print(f'  ... and {len(FAIL)-40} more')
print(f'WARNINGS {len(WARN)}'); [print('  !', m) for m in WARN[:15]]
sys.exit(1 if FAIL else 0)
