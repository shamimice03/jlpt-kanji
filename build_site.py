import json, re, pathlib
tpl  = pathlib.Path('n2_site_template.html').read_text(encoding='utf-8')
data = json.dumps(json.load(open('deck_packed.json',encoding='utf-8')), ensure_ascii=False, separators=(',',':'))
read = json.dumps(json.load(open('reading_packed.json',encoding='utf-8')), ensure_ascii=False, separators=(',',':'))
body = tpl.replace('__DATA__', data).replace('__READ__', read)
pathlib.Path('n2_kanji_site.html').write_text(body, encoding='utf-8')

title='Kanji for JLPT'
desc=('Flashcards for 1,061 JLPT kanji (N5-N1) with katakana onyomi, hiragana kunyomi, '
      '5,436 vocabulary words and example sentences with furigana. '
      'Verified against KANJIDIC2, JMdict and Kanji alive.')
body_nt = re.sub(r'^<title>.*?</title>\n', '', body, count=1)
head = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#EDF0F4">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Kanji">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%231E4E79'/%3E%3Ctext x='32' y='46' font-size='42' text-anchor='middle' fill='%23fff' font-family='serif'%3E漢%3C/text%3E%3C/svg%3E">
'''
links = re.findall(r'^<link rel="(?:preconnect|stylesheet)"[^>]*>\n', body_nt, flags=re.M)
for l in links: body_nt = body_nt.replace(l, '', 1)
head += ''.join(links) + '</head>\n<body>\n'
out = head + body_nt.lstrip('\n') + '\n</body>\n</html>\n'
for p in ['/mnt/user-data/outputs/index.html','/home/claude/jlpt-kanji/index.html']:
    pathlib.Path(p).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(p).write_text(out, encoding='utf-8')
print('artifact', len(body), '| standalone', len(out))
