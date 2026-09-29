# Kanji for JLPT

Flashcards and a searchable browser for **1,061 JLPT kanji** (N5 → N1), with readings,
vocabulary and example sentences.

**Live site:** https://shamimice03.github.io/jlpt-kanji/

## What's in it

| Level | Kanji |
|---|---|
| N5 | 80 |
| N4 | 165 |
| N3 | 380 |
| N2 | 386 |
| N1 extras | 50 |
| **Total** | **1,061** |

Each kanji has:

- onyomi in katakana, kunyomi in hiragana
- English meaning
- 5–11 high-frequency vocabulary words with readings and English
- one short, everyday example sentence per word — **5,436 sentences in all**
- whole-sentence furigana, switchable **On / Tap / Off**
- English translations, switchable **Show / Hide**

## Features

- **Study** — spaced-repetition flashcards (Leitner boxes 0–5, learned at box 3),
  in sets of 25, filterable by level, shufflable, with a "Needs work" filter.
- **Browse** — a grid of every kanji with search across kanji, readings, meanings,
  vocabulary and sentences; open any card to grade it *Again* / *Got it*, the same
  progress the Study tab uses.
- **Light / dark / auto** theme, and a text-size control that also scales itself up
  on large displays.
- Every vocabulary word carries the **JLPT vocabulary-list level** it appears on
  (N5–N1), and a **Words: My level** switch hides words harder than the level you're
  studying, along with their sentences.
- Keyboard: `Space` flip · `1` again · `2` got it · `←` `→` move · `F` furigana ·
  `E` english · `T` theme.
- Progress is saved in `localStorage` — in your browser only, nothing is uploaded.

## How the data was checked

JLPT kanji lists are unofficial — the Japan Foundation stopped publishing them after the
2010 revision, so every list in circulation is reverse-engineered. This one merges several
independent lists and verifies the contents against real dictionaries:

- **KANJIDIC2** — every onyomi, kunyomi and meaning (0 mismatches remaining)
- **JMdict** — all 5,436 vocabulary words checked as real dictionary headwords
- **Kanji alive** (University of Chicago) — independent cross-check of the readings
- **UniDic / fugashi** — sentence furigana, with 218 readings overridden by the
  JMdict-verified ones where the analyser mis-segmented a compound

Eight genuine reading errors and around twenty non-dictionary vocabulary entries were
found and fixed this way.

### A note on the level counts

JLPT level lists disagree at the boundaries, so the counts here are one defensible
reading rather than the only one:

- **N5 is 80**, matching the modern lists ([JLPTsensei](https://jlptsensei.com/jlpt-n5-kanji-list/)
  says 80; KANJIDIC2's `jlpt_new` tags say 79). The "about 100" figure often quoted comes
  from the **pre-2010 exam**, whose Level 4 had exactly 103 kanji — the 23 extras (手, 目,
  買, 飲, 駅, 魚 …) are all in this deck, just filed as N4 or N3.
- **N4 is 165**, against 166 in KANJIDIC2's `jlpt_new` and 170 in AnchorI. Every
  difference is a kanji this deck places one level away, not one it is missing.
- **N1 extras** are kanji that some list — usually the pre-2010 Level 2 list — expects at
  N2, but which the modern lists moved to N1. They're included so nothing on any of the
  reference lists is absent.

Checked against the union of all three reference lists, **no kanji tagged N5–N2 by any of
them is missing from this deck.**

### Vocabulary sourced from the JLPT word lists

The vocabulary was originally chosen to illustrate each kanji, which meant words on the
JLPT vocabulary lists could be absent. Every word from the
[Tanos](https://www.tanos.co.uk/jlpt/) N5–N1 vocabulary lists that contains a kanji at
that same level has now been added on top of what was already there — 125 words at N2,
with the other levels to follow. Nothing was removed.

Because that rule only reaches words built around a same-level kanji, it covers 588 of
the N2 list's 1,748 entries. Work is under way to attach every list word to whichever
deck kanji it contains, regardless of level — 1,299 more words across the N5–N2 lists.
A kanji deck can reach at most about two thirds of a vocabulary list either way: 253 N2
entries are kana-only (ショップ, すっきり) and 163 need kanji outside the deck, so they
have no kanji card to sit on.

Each added word was checked against JMdict for its headword and reading before inclusion;
affix placeholders (`～`), kana-only entries and rare or archaic senses were filtered out.

Vocabulary data from [Jonathan Waller's JLPT resources](https://www.tanos.co.uk/jlpt/),
used under [CC BY](https://creativecommons.org/licenses/by/4.0/).

## Running it

It's a single self-contained `index.html` — no build step, no dependencies.
Open the file directly, or serve the folder:

```sh
python3 -m http.server 8000
```

## Deploying

GitHub Pages: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`**.

## Licence

The code is MIT. Dictionary data is derived from
[KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) and
[JMdict](https://www.edrdg.org/jmdict/j_jmdict.html), which are the property of the
Electronic Dictionary Research and Development Group and used under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/);
[Kanji alive](https://kanjialive.com/) data is CC BY 4.0.
