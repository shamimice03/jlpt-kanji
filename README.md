# Kanji for JLPT

Flashcards and a searchable browser for **1,042 JLPT kanji** (N5 → N1), with readings,
vocabulary and example sentences.

**Live site:** https://shamimice03.github.io/jlpt-kanji/

## What's in it

| Level | Kanji |
|---|---|
| N5 | 80 |
| N4 | 165 |
| N3 | 377 |
| N2 | 386 |
| N1 extras | 34 |
| **Total** | **1,042** |

Each kanji has:

- onyomi in katakana, kunyomi in hiragana
- English meaning
- 5–10 high-frequency vocabulary words with readings and English
- one short, everyday example sentence per word — **5,217 sentences in all**
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
- Keyboard: `Space` flip · `1` again · `2` got it · `←` `→` move · `F` furigana ·
  `E` english · `T` theme.
- Progress is saved in `localStorage` — in your browser only, nothing is uploaded.

## How the data was checked

JLPT kanji lists are unofficial — the Japan Foundation stopped publishing them after the
2010 revision, so every list in circulation is reverse-engineered. This one merges several
independent lists and verifies the contents against real dictionaries:

- **KANJIDIC2** — every onyomi, kunyomi and meaning (0 mismatches remaining)
- **JMdict** — all 5,217 vocabulary words checked as real dictionary headwords
- **Kanji alive** (University of Chicago) — independent cross-check of the readings
- **UniDic / fugashi** — sentence furigana, with 218 readings overridden by the
  JMdict-verified ones where the analyser mis-segmented a compound

Eight genuine reading errors and around twenty non-dictionary vocabulary entries were
found and fixed this way.

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
