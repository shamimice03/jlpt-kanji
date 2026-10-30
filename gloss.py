# -*- coding: utf-8 -*-
"""Per-word glosses for the reading passages.

Builds, for each ruby run a sentence produces, the dictionary form of the word
that run came from plus a short English gloss, so the page can show the meaning
beside the reading when the reader taps a word.

Gloss sources, in order of trust:
  1. the deck's own vocabulary (hand-verified against JMdict already)
  2. JMdict via jamdict, strict lookup on the lemma, then on the surface
  3. KANJIDIC2 meanings, for a lone kanji no dictionary word covers
"""
import json, re, functools
import fugashi
from furigana import align, reading_of, KAN

_tagger = fugashi.Tagger()
SKIP_POS1 = {'助詞', '助動詞', '補助記号', '空白', '接続詞', '代名詞', '感動詞'}

# ---- source 1: the deck -----------------------------------------------------
def _deck_words(path='deck_packed.json'):
    out = {}
    for e in json.load(open(path, encoding='utf-8')):
        for v in e.get('v', []):
            w, r, en = v[0], v[1], v[2]
            out.setdefault(w, en)
    return out

# ---- source 2: JMdict -------------------------------------------------------
class _JM:
    def __init__(self):
        from jamdict import Jamdict
        self.jam = Jamdict()
    @functools.lru_cache(maxsize=20000)
    def look(self, key):
        try:
            r = self.jam.lookup(key, strict_lookup=True)
        except Exception:
            return None
        for e in r.entries:
            forms = [str(k.text) for k in e.kanji_forms] or [str(k.text) for k in e.kana_forms]
            if key not in forms:
                continue
            for s in e.senses:
                gs = [str(g) for g in s.gloss]
                gs = [g for g in gs if g and not g.startswith('(')]
                if gs:
                    return ', '.join(gs[:3])
        return None

# ---- source 3: KANJIDIC2 ----------------------------------------------------
def _kanji_meanings(path='kanji.json'):
    out = {}
    for k, v in json.load(open(path, encoding='utf-8')).items():
        m = v.get('meanings') or []
        if m:
            out[k] = ', '.join(m[:3])
    return out


class Glossary:
    def __init__(self):
        self.deck = _deck_words()
        self.jm = _JM()
        self.kd = _kanji_meanings()
        self.index = {}      # "lemma\ten" -> id
        self.entries = []    # [[lemma, en], ...]
        self.misses = set()

    def _gloss(self, lemma, surface):
        for key in (lemma, surface):
            if key in self.deck:
                return key, self.deck[key]
        for key in (lemma, surface):
            g = self.jm.look(key)
            if g:
                return key, g
        if len(lemma) == 1 and lemma in self.kd:
            return lemma, self.kd[lemma]
        self.misses.add(lemma)
        return None, None

    def _id(self, lemma, en):
        k = lemma + '\t' + en
        if k not in self.index:
            self.index[k] = len(self.entries)
            self.entries.append([lemma, en])
        return self.index[k]

    def runs(self, text):
        """Runs as [text, reading|None] or [text, reading, glossId]."""
        out = []
        prev_num = False
        for tok in _tagger(text):
            f = tok.feature
            pos1, pos2 = getattr(f, 'pos1', None), getattr(f, 'pos2', None)
            parts = align(tok.surface, reading_of(tok))
            gid = None
            # A counter after a number is a counter, not the word it looks like:
            # 月 in 十一月 is "month", not "moon", so leave it unglossed.
            counter = prev_num and getattr(f, 'pos3', None) == '助数詞可能'
            if (pos1 not in SKIP_POS1
                    and pos1 != '接尾辞' and pos2 not in ('固有名詞', '数詞')
                    and not counter
                    and KAN.search(tok.surface)):
                lemma = getattr(f, 'lemma', None) or tok.surface
                if lemma == '*':
                    lemma = tok.surface
                lemma, en = self._gloss(lemma, tok.surface)
                if en:
                    gid = self._id(lemma, en)
            if gid is not None:
                for p in parts:
                    if p[1]:                    # the ruby run carries the gloss
                        p.append(gid)
                        break
                else:
                    parts[0].append(gid)        # kanji with no ruby (e.g. 々)
            prev_num = (pos2 == '数詞')
            out.extend(parts)
        merged = []
        for p in out:
            if len(p) == 2 and p[1] is None and merged and len(merged[-1]) == 2 and merged[-1][1] is None:
                merged[-1][0] += p[0]
            else:
                merged.append(p)
        return merged
