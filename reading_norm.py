# -*- coding: utf-8 -*-
"""Shared loading rules for the passage set.

Two things live here so the checker and the builder cannot drift apart:

`pairs` form — a passage may give its body as paragraphs of (Japanese
sentence, English sentence) tuples instead of a body string plus a separate
translation. The two can then never fall out of step, which is what made
expanding a passage risky before: the Japanese and the English were edited in
different places and the counts had to be re-aligned by hand.

`merge` — a later module may republish a passage under an id that already
exists, replacing it in place and keeping its position in the order.
"""

OFFICIAL_LEN = {            # jlpt.jp/guideline/pdf/n2.pdf, 読解 問題構成
    '内容理解（短文）': 200,
    '内容理解（中文）': 500,
    '統合理解': 600,
    '主張理解（長文）': 900,
    '情報検索': 700,
}


def expand_pairs(passages, sent_en):
    """Turn every `pairs` passage into the body/en/SENT_EN form."""
    for p in passages:
        pr = p.get('pairs')
        if not pr:
            continue
        p['body'] = '\n'.join(''.join(jp for jp, _ in para) for para in pr)
        sent_en[p['id']] = [en for para in pr for _, en in para]
        # Always rebuilt, never merely filled in: an inherited translation from
        # before an expansion would describe a passage that no longer exists.
        p['en'] = '\n'.join(' '.join(en for _, en in para) for para in pr)
    return passages


def merge(base, override):
    """Overlay fields onto a passage of the same id; append anything new.

    Overlaying rather than replacing means a revision only has to carry what
    changed -- usually `pairs` -- and the questions, tier and title it does not
    mention stay exactly as they were.
    """
    at = {p['id']: i for i, p in enumerate(base)}
    for p in override:
        if p['id'] in at:
            if 'pairs' in p:
                base[at[p['id']]].pop('en', None)
            base[at[p['id']]].update(p)
        else:
            at[p['id']] = len(base)
            base.append(p)
    return base
