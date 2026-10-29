# -*- coding: utf-8 -*-
"""Graded reading passages. Every kanji in a passage must be at or below its tier;
reading_build.py verifies that and will not let an out-of-tier kanji ship."""

PASSAGES = [
{
 "id": "r1", "kind": "内容理解（短文）", "tier": "N5", "title": "にちようび",
 "body": "にちようび、わたしは父と母と山へ行きました。\n"
         "あさはやくうちを出て、電車に一時間ほどのりました。\n"
         "山の上から、川と小さなまちが見えました。そらが高くて、気もちがよかったです。\n"
         "おひるは、母のおべんとうを食べました。とてもおいしかったです。\n"
         "また三人で行きたいです。",
 "en": "On Sunday I went to the mountains with my father and mother. We left home early in "
       "the morning and rode the train for about an hour. From the top of the mountain we "
       "could see a river and a small town. The sky was high and it felt wonderful. For lunch "
       "we ate the packed lunch my mother had made. It was delicious. I want to go again, the three of us.",
 "qs": [
   {"q": "だれと山へ行きましたか。",
    "opts": ["友だちと", "父と母と", "先生と", "一人で"], "ans": 1,
    "why": "「わたしは父と母と山へ行きました」とあります。"},
   {"q": "山の上から何が見えましたか。",
    "opts": ["うみとふね", "川とまち", "電車とえき", "学校とうち"], "ans": 1,
    "why": "「川と小さな、まちが見えました」とあります。"},
 ]},
{
 "id": "r2", "kind": "内容理解（短文）", "tier": "N4", "title": "となりのせきの人",
 "body": "四月に新しい学校に来ました。はじめは知っている人が一人もいなくて、少しさびしかったです。\n"
         "ある日、となりのせきの人が「いっしょにお昼を食べませんか」と言ってくれました。"
         "わたしはうれしくて、すぐに「はい」と答えました。\n"
         "その日から毎日いっしょに食べています。話をしているうちに、同じ音楽がすきだと分かりました。\n"
         "今は、学校へ行くのが楽しみです。",
 "en": "In April I came to a new school. At first I did not know a single person and felt a "
       "little lonely. One day the person sitting next to me said, “Would you like to have "
       "lunch together?” I was so glad that I answered “yes” straight away. Since that day "
       "we have eaten together every day. While talking, we found we like the same music. "
       "Now I look forward to going to school.",
 "qs": [
   {"q": "はじめ、どうしてさびしかったのですか。",
    "opts": ["学校がとおかったから", "知っている人がいなかったから",
             "勉強がむずかしかったから", "お昼を食べられなかったから"], "ans": 1,
    "why": "「知っている人が一人もいなくて、少しさびしかった」とあります。"},
   {"q": "今、学校へ行くのが楽しみなのはなぜですか。",
    "opts": ["新しい音楽を教えてもらえるから", "いっしょに食べる友だちができたから",
             "となりのせきがかわったから", "勉強がかんたんになったから"], "ans": 1,
    "why": "いっしょにお昼を食べる人ができ、好きなものも同じだと分かったからです。"},
 ]},
{
 "id": "r3", "kind": "内容理解（中文）", "tier": "N3", "title": "となりの部屋の犬",
 "body": "となりの部屋に、犬をかっている人が住んでいる。\n"
         "引っこしてきた日、ドアの前でその犬に会った。思ったより大きかったので、わたしは少しこわかった。"
         "しかし、かい主の女の人が「だいじょうぶですよ。やさしい子ですから」と言って、"
         "わたしの手を犬のはなの近くへ持っていった。犬はしずかに手のにおいをかいで、しっぽをふった。\n"
         "それから毎朝、出かける前にその犬にあいさつするようになった。名前はハナという。\n"
         "ある日、仕事でつかれて帰ってきたとき、ハナがドアの前にすわって待っていた。"
         "わたしの顔を見ると、うれしそうに走ってきた。その日のつかれが、急にかるくなった気がした。",
 "en": "Someone who keeps a dog lives in the room next door. On the day I moved in I met the "
       "dog in front of the door. It was bigger than I had expected, so I was a little afraid. "
       "But its owner said, “It's all right, she's gentle,” and brought my hand close to the "
       "dog's nose. The dog quietly sniffed my hand and wagged her tail. After that I began "
       "greeting her every morning before going out. Her name is Hana. One day, when I came "
       "home tired from work, Hana was sitting waiting in front of the door. When she saw my "
       "face she came running happily. My tiredness that day suddenly felt lighter.",
 "qs": [
   {"q": "はじめて犬に会ったとき、わたしはどう思ったか。",
    "opts": ["かわいいと思った", "少しこわいと思った",
             "うるさいと思った", "きたないと思った"], "ans": 1,
    "why": "「思ったより大きかったので、わたしは少しこわかった」とあります。"},
   {"q": "「つかれが急にかるくなった気がした」のはなぜか。",
    "opts": ["仕事が思ったより早く終わったから", "ハナがよろこんでむかえてくれたから",
             "ドアの前でしばらく休んだから", "かい主が手つだってくれたから"], "ans": 1,
    "why": "待っていたハナがうれしそうに走ってきたことで、気もちが軽くなったのです。"},
 ]},
{
 "id": "r4", "kind": "内容理解（中文）", "tier": "N3", "title": "本の読み方",
 "body": "本は速く読むほうがよいと思っていた時期がある。一年に何さつ読んだかを数えて、"
         "多ければ多いほどよいと考えていた。\n"
         "しかし、去年の冬に病気で一週間ほど休んだとき、その考えがかわった。"
         "ほかにすることがなく、同じ本を何度もくり返し読んだ。すると、一度目には気づかなかった言葉が、"
         "二度目、三度目には見えてきた。同じ文なのに、読むたびに感じることがちがうのだ。\n"
         "今は、さつ数を数えるのをやめた。速く読むことより、心に残る一行に出会うことのほうが、"
         "ずっと大切だと思うようになったからだ。",
 "en": "There was a time when I thought it was better to read quickly. I counted how many "
       "books I read in a year and believed the more the better. But last winter, when I was "
       "ill and rested for about a week, that view changed. With nothing else to do, I read "
       "the same book over and over. Words I had not noticed the first time became visible on "
       "the second and third readings. It is the same text, yet what I feel differs each time "
       "I read it. Now I have stopped counting. I have come to think that meeting a single "
       "line that stays in your heart matters far more than reading fast.",
 "qs": [
   {"q": "この文を書いた人は、以前どのように考えていたか。",
    "opts": ["本はゆっくり読むほうがよい", "読んだ本の数が多いほどよい",
             "むずかしい本を読むほうがよい", "同じ本を何度も読むほうがよい"], "ans": 1,
    "why": "「多ければ多いほどよいと考えていた」とあります。"},
   {"q": "この文を書いた人の、今の考えに合うものはどれか。",
    "opts": ["一年に読むさつ数を決めたほうがよい", "病気のときに読むとよく分かる",
             "心に残る言葉に出会うことが大切だ", "速く読むれんしゅうをしたほうがよい"], "ans": 2,
    "why": "「心に残る一行に出会うことのほうが、ずっと大切だ」とあります。"},
 ]},
{
 "id": "r5", "kind": "主張理解（長文）", "tier": "N2", "title": "便利さと引きかえに",
 "body": "最近は、電話一つで何でもできるようになった。道に迷えば地図が教えてくれるし、"
         "知らない言葉もその場で調べられる。たしかに便利である。\n"
         "しかし、便利になった分、失ったものもあるのではないか。\n"
         "以前なら、駅までの道を人にたずねた。相手の顔を見て、礼を言った。今はその必要がない。"
         "画面を見ながら歩いていれば、目的地に着く。早くはなったが、そこに人との関わりはない。\n"
         "①そのことに気づいたのは、祖母と旅行したときだった。祖母は電話を持ち歩かない。"
         "道が分からなくなると、近くの店に入ってたずねる。すると店の人が、"
         "地図にのっていない近道を教えてくれたり、安くておいしい店をすすめてくれたりする。"
         "わたしが調べて得た情報より、ずっと豊かだった。\n"
         "便利な道具を捨てる必要はない。ただ、それに頼りきってしまうと、"
         "本当は手に入るはずだったものを見落としてしまうのかもしれない。",
 "en": "These days you can do almost anything with a phone. If you lose your way, a map tells "
       "you; a word you do not know can be looked up on the spot. It is certainly convenient. "
       "But for all that convenience, is there not something we have lost? Once, you asked "
       "someone the way to the station. You looked at their face and thanked them. Now there "
       "is no need. Walk while watching the screen and you arrive. It is faster, but there is "
       "no contact with another person in it. I noticed this while travelling with my "
       "grandmother. She does not carry a phone. When she loses her way she goes into a nearby "
       "shop and asks. The shopkeeper then tells her a shortcut not on any map, or recommends "
       "somewhere cheap and good to eat. It was far richer than the information I got by "
       "looking things up. There is no need to throw the convenient tools away. But if we come "
       "to rely on them entirely, we may overlook what we could in fact have had.",
 "qs": [
   {"q": "①そのこと とは、どんなことか。",
    "opts": ["電話一つで何でも調べられるということ",
             "便利になったかわりに失ったものがあるということ",
             "祖母が電話を持ち歩かないということ",
             "店の人が近道を教えてくれるということ"], "ans": 1,
    "why": "直前の段落で「便利になった分、失ったものもあるのではないか」と述べ、"
           "人との関わりが失われた例を挙げています。"},
   {"q": "祖母の旅について、筆者はどう感じているか。",
    "opts": ["道に迷うので時間がかかって困る",
             "人にたずねるのは相手にめいわくだ",
             "調べて得た情報よりも中身が豊かだ",
             "若い人にはまねができない方法だ"], "ans": 2,
    "why": "「わたしが調べて得た情報より、ずっと豊かだった」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["便利な道具はできるだけ使わないほうがよい",
             "人にたずねるほうが調べるより早い",
             "便利な道具に頼りきると、得られたはずのものを見落とす",
             "祖母のような昔の生活にもどるべきだ"], "ans": 2,
    "why": "最後の段落で「捨てる必要はない。ただ、頼りきってしまうと…見落としてしまう」"
           "と述べています。1や4のように道具を否定してはいません。"},
 ]},
{
 "id": "r6", "kind": "主張理解（長文）", "tier": "N2", "title": "失敗から学ぶ",
 "body": "子どものころ、失敗するのがこわかった。手をあげて答えを間違えると、"
         "はずかしかったからだ。だから、確実に分かる問題にしか手をあげなかった。\n"
         "働きはじめてから、その考えが変わった。新しい仕事を任されたとき、"
         "わたしは一度も失敗しないように、何度も確認しながら、しんちょうに進めた。"
         "しかし結果は、期待したほどよくなかった。\n"
         "となりの席の同期は、わたしとはちがった。思いついたらすぐ試し、"
         "うまくいかないと分かればすぐにやり方を変える。失敗の数はわたしよりずっと多かったが、"
         "最後にはよい結果を出した。\n"
         "②その差はどこにあったのだろう。わたしは失敗を「さけるもの」と考え、"
         "彼は「早く見つけるもの」と考えていた。大切なのは失敗の数ではなく、"
         "そこから何を学び、どれだけ早く次に生かすかなのだと、そのとき初めて気づいた。",
 "en": "As a child I was afraid of failing. If I raised my hand and got the answer wrong, it "
       "was embarrassing. So I only raised my hand for questions I was certain about. After I "
       "started working, that view changed. When I was given a new job, I went about it "
       "carefully, checking over and over so as never to fail once. But the result was not as "
       "good as I had hoped. The colleague who joined at the same time, sitting next to me, "
       "was different. She tried things as soon as she thought of them, and changed her "
       "approach the moment she saw it was not working. She failed far more often than I did, "
       "yet in the end she produced the better result. Where did that difference lie? I "
       "thought of failure as something to avoid; she thought of it as something to find "
       "early. What matters is not the number of failures but what you learn from them and "
       "how quickly you put it to use. That was when I first realised it.",
 "qs": [
   {"q": "②その差 とは、何と何の差か。",
    "opts": ["仕事の量の差", "失敗に対する考え方の差",
             "経験の長さの差", "性格の明るさの差"], "ans": 1,
    "why": "直後に「わたしは失敗を『さけるもの』と考え、彼は『早く見つけるもの』と考えていた」"
           "と説明されています。"},
   {"q": "筆者は新しい仕事をどのように進めたか。",
    "opts": ["思いついたことをすぐに試した", "同期にやり方を聞きながら進めた",
             "失敗しないように何度も確認した", "期待されたとおりの結果を出した"], "ans": 2,
    "why": "「一度も失敗しないように、何度も確認しながら慎重に進めた」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["失敗はできるだけさけるべきだ",
             "失敗の数が多いほうがよい結果が出る",
             "失敗から学び、早く次に生かすことが大切だ",
             "子どものころの考え方は変えないほうがよい"], "ans": 2,
    "why": "最後に「大切なのは失敗の数ではなく、そこから何を学び、どれだけ早く次に生かすか」"
           "とまとめています。2は「数が多いほうがよい」と言っており誤りです。"},
 ]},
]
