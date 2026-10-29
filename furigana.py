# -*- coding: utf-8 -*-
"""Whole-sentence furigana: split text into (run, reading|None) pairs."""
import re, fugashi
_tagger = fugashi.Tagger()
KAN = re.compile(r'[一-鿿々]')

def kata2hira(s):
    return ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)

def reading_of(tok):
    for attr in ('kana', 'pron'):
        v = getattr(tok.feature, attr, None)
        if v and v != '*': return kata2hira(v)
    return None

def align(surface, reading):
    """Split one token into runs, keeping ruby only over the kanji parts."""
    if not reading or not KAN.search(surface): return [[surface, None]]
    if surface == reading: return [[surface, None]]
    # trailing kana shared by both (okurigana) stays outside the ruby
    tail = 0
    while (tail < len(surface) - 1 and tail < len(reading) - 1
           and surface[-1-tail] == reading[-1-tail] and not KAN.match(surface[-1-tail])):
        tail += 1
    head = 0
    while (head < len(surface) and head < len(reading)
           and surface[head] == reading[head] and not KAN.match(surface[head])):
        head += 1
    core_s = surface[head:len(surface)-tail] if tail else surface[head:]
    core_r = reading[head:len(reading)-tail] if tail else reading[head:]
    out = []
    if head: out.append([surface[:head], None])
    if core_s:
        out.append([core_s, core_r] if KAN.search(core_s) and core_r else [core_s, None])
    if tail: out.append([surface[len(surface)-tail:], None])
    return out or [[surface, None]]

def full_furigana(text):
    runs = []
    for tok in _tagger(text):
        runs.extend(align(tok.surface, reading_of(tok)))
    merged = []
    for t, r in runs:
        if r is None and merged and merged[-1][1] is None: merged[-1][0] += t
        else: merged.append([t, r])
    return merged
