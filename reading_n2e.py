# -*- coding: utf-8 -*-
"""Batch 4: a full test-shaped N2 set (問題10-14 shapes), written to work in
the N5-N2 kanji that appear on the practice test but were not yet used in
any of my passages. Original text; the kanji inventory is the target."""

PASSAGES = [
# ---------------- 問題10 style: 短文 ----------------
{
 "id": "u1", "tier": "N2", "kind": "内容理解（短文）", "title": "図書館からのお願い",
 "body": "みどり図書館では、不要になった本をお寄せいただく「本の寄付」を受け付けています。\n"
         "お寄せいただいた本は、館内のたなに並べるほか、"
         "地域のしせつへお送りする場合もございます。\n"
         "ただし、書きこみのあるもの、汚れのひどいもの、"
         "発行から十年以上たった実用書はお受けできません。"
         "お持ちになる前に、一度ご確認をお願いいたします。",
 "en": "Midori Library is accepting donations of books you no longer need.\n"
       "Donated books are placed on our shelves, and in some cases sent on to facilities in "
       "the area.\n"
       "However, we cannot accept books with writing in them, books that are badly soiled, or "
       "practical books published more than ten years ago. Please check before bringing them in.",
 "qs": [
   {"q": "寄付できない本はどれか。",
    "opts": ["地域のしせつで使われていた本",
             "五年前に発行された小説",
             "書きこみのある本",
             "図書館のたなになかった本"], "ans": 2,
    "why": "「書きこみのあるもの、汚れのひどいもの、発行から十年以上たった実用書は"
           "お受けできません」とあります。小説は十年の決まりの対象ではありません。"},
 ]},
{
 "id": "u2", "tier": "N2", "kind": "内容理解（短文）", "title": "失敗を話すこと",
 "body": "失敗した話を人にするのは、恥ずかしいものだ。だから多くの人はだまっている。\n"
         "しかし、だまっていると、同じ失敗が別の人のところでくり返される。"
         "恥を少しだけ引き受けて話した人のおかげで、"
         "次の人が同じ損をしなくて済むのである。\n"
         "うまくいった話は、聞いていて気持ちがよい。"
         "けれども、本当に役に立つのは、たいてい失敗した話のほうだ。",
 "en": "Telling people about a failure is embarrassing, so most people keep quiet.\n"
       "But when they keep quiet, the same failure happens again to someone else. Thanks to "
       "the person who takes on a little of the shame and talks, the next person avoids the "
       "same loss.\n"
       "Success stories are pleasant to listen to. But what is genuinely useful is usually the "
       "story of a failure.",
 "qs": [
   {"q": "筆者が言いたいことは何か。",
    "opts": ["失敗した話は人にしないほうがよい",
             "うまくいった話のほうが聞く人の役に立つ",
             "失敗した話を話す人が次の人を助ける",
             "恥ずかしい思いをしないようにするべきだ"], "ans": 2,
    "why": "「恥を少しだけ引き受けて話した人のおかげで、次の人が同じ損をしなくて済む」"
           "とあります。"},
 ]},
{
 "id": "u3", "tier": "N2", "kind": "内容理解（短文）", "title": "靴の選び方",
 "body": "靴を買うときは、夕方に店へ行くとよいと言われる。"
         "朝よりも夕方のほうが足がむくんで大きくなっているからだ。\n"
         "朝に合わせて選ぶと、一日の終わりにはきつくなり、歩くのが苦しくなる。"
         "少しゆとりがあるくらいが、結局は疲れにくい。\n"
         "見た目の形だけで決めてしまうと、"
         "せっかく買った靴を、ほとんどはかないまま終わらせることになる。",
 "en": "They say you should go to the shop in the evening when buying shoes, because feet "
       "swell and are larger in the evening than in the morning.\n"
       "If you choose to fit your morning size, they become tight by the end of the day and "
       "walking becomes painful. A little room is in the end less tiring.\n"
       "If you decide on looks alone, you end up with shoes you bought and then barely wore.",
 "qs": [
   {"q": "夕方に靴を買うとよいのはなぜか。",
    "opts": ["夕方のほうが店がすいているから",
             "夕方は足が大きくなっているから",
             "夕方のほうが安く買えるから",
             "夕方のほうが明るくて形がよく見えるから"], "ans": 1,
    "why": "「朝よりも夕方のほうが足がむくんで大きくなっているからだ」とあります。"},
 ]},
{
 "id": "u4", "tier": "N2", "kind": "内容理解（短文）", "title": "遅刻について",
 "body": "待ち合わせに遅れるとき、「あと五分で着きます」と連絡する人がいる。"
         "ところが実際には、十五分かかることが多い。\n"
         "遅れる側は、早く着くと思いたい。"
         "その希望がそのまま数字になって口から出てしまうのだろう。\n"
         "待つ側にとって大切なのは、早い数字ではなく、正しい数字である。"
         "十五分かかるなら、はじめに十五分と伝えてもらったほうが、"
         "本を読むなり、ほかの用事を片づけるなりできる。",
 "en": "When someone is going to be late for a meeting, they sometimes say “I'll be there in "
       "five minutes.” In fact it often takes fifteen.\n"
       "The person running late wants to believe they will arrive soon, and that hope comes "
       "out of their mouth as a number.\n"
       "What matters to the person waiting is not a small number but an accurate one. If it is "
       "going to take fifteen minutes, being told fifteen at the outset means they can read a "
       "book or deal with something else.",
 "qs": [
   {"q": "筆者によると、待つ側にとってよいのはどんな連絡か。",
    "opts": ["できるだけ早い時間を伝える連絡",
             "実際にかかる時間を正しく伝える連絡",
             "何度もくり返して伝える連絡",
             "遅れる理由をくわしく伝える連絡"], "ans": 1,
    "why": "「待つ側にとって大切なのは、早い数字ではなく、正しい数字である」とあります。"},
 ]},
{
 "id": "u5", "tier": "N2", "kind": "内容理解（短文）", "title": "貯金の始め方",
 "body": "貯金を始めようと思っても、余ったお金をためようとすると、たいてい続かない。"
         "月末には、たいてい余っていないからである。\n"
         "うまくいく人は、順番が逆だ。給料が入った日に、"
         "先に決まった額を別の口座へ移してしまう。"
         "残ったお金で暮らすことになるが、不思議と、それで足りるようになる。\n"
         "強い気持ちだけで続けようとせず、"
         "始めに仕組みを作ってしまうほうが、結局は楽なのである。",
 "en": "Even if you decide to start saving, trying to save what is left over usually does not "
       "last, because at the end of the month there is usually nothing left over.\n"
       "People who manage it do it the other way round. On payday they move a set amount into "
       "another account first. They then live on what remains — and oddly, it turns out to be "
       "enough.\n"
       "Rather than relying on willpower to keep it up, building the arrangement at the start "
       "is in the end easier.",
 "qs": [
   {"q": "貯金がうまくいく人は、どのようにしているか。",
    "opts": ["月末に余った分をためている",
             "給料日に先に決まった額を移している",
             "毎日少しずつ現金をためている",
             "買い物の回数を減らしている"], "ans": 1,
    "why": "「給料が入った日に、先に決まった額を別の口座へ移してしまう」とあります。"},
 ]},
# ---------------- 問題11 style: 中文 ----------------
{
 "id": "u6", "tier": "N2", "kind": "内容理解（中文）", "title": "競争と協力",
 "body": "子どものころの運動会では、勝ち負けがはっきりしていた。"
         "走る速さを競い、勝った組が喜び、負けた組はくやしがる。"
         "それが当たり前だと思っていた。\n"
         "大人になって働きはじめると、様子がちがった。"
         "同じ仕事を争って取り合うより、"
         "得意な部分を分け合って進めたほうが、結果がよくなる場面が多い。"
         "①この変化に、はじめはとまどった。\n"
         "よく考えてみると、競争がなくなったわけではない。"
         "相手が変わったのである。となりの人と勝ち負けを決めるのではなく、"
         "去年の自分や、期限や、市場といった、目に見えにくいものと競っている。\n"
         "勢いよく走って一番になる競争と、"
         "仲間と力を合わせて期限までに仕上げる競争。"
         "どちらも努力が要る点は同じだが、"
         "必要な力の種類はずいぶんちがうのだと、今は思う。",
 "en": "At school sports days the winning and losing was clear. You competed on speed, the "
       "winning team was delighted and the losing team frustrated. I thought that was simply "
       "how things were.\n"
       "When I grew up and started working, it looked different. Rather than fighting over the "
       "same piece of work, there were many situations where dividing it by what each person "
       "was good at produced a better result. At first this change confused me.\n"
       "Thinking it over, competition had not disappeared. The opponent had changed. Instead "
       "of deciding who wins against the person beside you, you compete with things that are "
       "hard to see — last year's self, a deadline, the market.\n"
       "The competition of running hard and coming first, and the competition of joining "
       "forces to finish by a deadline. Both require effort, but the kind of strength needed "
       "is, I now think, quite different.",
 "qs": [
   {"q": "①この変化 とは、どんな変化か。",
    "opts": ["勝ち負けがはっきりしなくなったこと",
             "争うより分け合うほうが結果がよいこと",
             "走る速さが問われなくなったこと",
             "努力が必要でなくなったこと"], "ans": 1,
    "why": "直前に「同じ仕事を争って取り合うより、得意な部分を分け合って進めたほうが、"
           "結果がよくなる」とあります。"},
   {"q": "大人になってからの競争について、筆者はどう述べているか。",
    "opts": ["競争はなくなった",
             "競う相手が変わった",
             "勝ち負けがよりはっきりした",
             "競争に勝つ必要がなくなった"], "ans": 1,
    "why": "「競争がなくなったわけではない。相手が変わったのである」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["運動会の競争は役に立たない",
             "仲間と協力すれば努力は要らない",
             "二つの競争は、必要な力の種類がちがう",
             "期限を決めれば競争に勝てる"], "ans": 2,
    "why": "最後に「どちらも努力が要る点は同じだが、必要な力の種類はずいぶんちがう」"
           "とまとめています。"},
 ]},
{
 "id": "u7", "tier": "N2", "kind": "内容理解（中文）", "title": "台所の記録",
 "body": "母は料理の本をほとんど見ない。それでも、同じ菓子を何度作っても味が変わらない。"
         "どうしてかと聞いたら、笑いながら古いノートを出してきた。\n"
         "開くと、作った日と、使った材料の量と、その日の天気が書いてある。"
         "「蒸し時間を二分のばす」「さとうを少し減らす」といった短い言葉が、"
         "何年分も積み重なっていた。\n"
         "②母が覚えていたのは、味そのものではなかった。"
         "うまくいかなかった日に何をどう直したか、という記録のほうである。"
         "失敗が消えずに残っているから、同じ場所でつまずかずに済む。\n"
         "料理に限った話ではないだろう。"
         "続けている人が強いのは、長く続けたからというより、"
         "続けるあいだに直した回数が多いからなのだと思う。",
 "en": "My mother hardly ever looks at a cookbook. Even so, however many times she makes the "
       "same cake, the taste does not change. When I asked how, she laughed and brought out an "
       "old notebook.\n"
       "Opening it, there was the date she made it, the amounts of the ingredients, and the "
       "weather that day. Short notes like “extend the steaming by two minutes” or “reduce "
       "the sugar slightly” had piled up over years.\n"
       "What my mother remembered was not the taste itself. It was the record of what she had "
       "changed, and how, on the days it had not gone well. Because the failures remain rather "
       "than vanishing, she does not stumble in the same place.\n"
       "This is surely not limited to cooking. People who keep at something are strong, I "
       "think, less because they kept at it for long than because of how many times they "
       "corrected course while doing so.",
 "qs": [
   {"q": "ノートには何が書いてあったか。",
    "opts": ["料理の本から写した作り方",
             "作った日と材料の量と天気",
             "家族の感想と点数",
             "買い物をした店の名前"], "ans": 1,
    "why": "「作った日と、使った材料の量と、その日の天気が書いてある」とあります。"},
   {"q": "②母が覚えていたのは、味そのものではなかった とあるが、何を覚えていたのか。",
    "opts": ["うまくいかなかった日の直し方",
             "一番うまくできた日の作り方",
             "菓子を作った回数",
             "家族が好きな味の種類"], "ans": 0,
    "why": "「うまくいかなかった日に何をどう直したか、という記録のほうである」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["料理には記録が欠かせない",
             "長く続けた人ほど強い",
             "続けるあいだに直した回数が人を強くする",
             "失敗は早く忘れたほうがよい"], "ans": 2,
    "why": "「長く続けたからというより、続けるあいだに直した回数が多いから」と"
           "まとめています。"},
 ]},
# ---------------- 問題12 style: 統合理解 ----------------
{
 "id": "u8", "tier": "N2", "kind": "統合理解", "title": "都会に住むか、いなかに住むか",
 "body": "Ａ\n"
         "若いうちは都会に住んだほうがよいと思う。"
         "仕事の選び方が広く、学べる場所も多い。"
         "美術館でも、夜の教室でも、行こうと思えばその日のうちに行ける。"
         "やちんは高く、部屋はせまいが、"
         "外に出れば足りないものはたいてい手に入る。"
         "選べる数が多いということ自体が、若い時期には大きな意味を持つ。\n"
         "Ｂ\n"
         "都会には確かに何でもある。しかし、"
         "あるということと、使っているということは別である。"
         "近くに美術館があっても、忙しくて一度も入らないまま一年が過ぎる人は多い。"
         "いなかに移ってから、かえって野山を歩くようになったという話もよく聞く。"
         "何があるかより、何をする時間が残っているか。"
         "住む場所を決めるときに見るべきは、そちらではないだろうか。",
 "en": "A. I think it is better to live in the city while you are young. The range of work to "
       "choose from is wide and there are many places to learn. A gallery, an evening class — "
       "if you decide to go, you can go that same day. Rent is high and rooms are small, but "
       "step outside and most of what you lack is there to be had. That there are many options "
       "is itself significant when you are young.\n"
       "B. The city certainly has everything. But having something and using it are different. "
       "There are plenty of people who have a gallery nearby and let a year pass without once "
       "going in. You often hear of people who moved to the countryside and started walking in "
       "the hills precisely then. Not what is there, but how much time is left to do anything "
       "— surely that is what to look at when deciding where to live.",
 "qs": [
   {"q": "都会について、ＡとＢが共通して認めていることは何か。",
    "opts": ["やちんが高く部屋がせまいこと",
             "選べるものや場所が多いこと",
             "忙しくて時間が残らないこと",
             "若い人に向いていること"], "ans": 1,
    "why": "Ａは「選べる数が多い」、Ｂも「都会には確かに何でもある」と認めています。"
           "1と3はＡ・Ｂ一方だけの内容です。"},
   {"q": "住む場所の選び方について、Ｂはどう述べているか。",
    "opts": ["いなかに住むほうがよい",
             "若いうちは都会に住むべきだ",
             "何があるかより、何をする時間が残っているかを見るべきだ",
             "やちんの安さで決めるべきだ"], "ans": 2,
    "why": "「何があるかより、何をする時間が残っているか…そちらではないだろうか」"
           "とあります。Ｂは田舎を勧めているわけではありません。"},
 ]},
# ---------------- 問題13 style: 長文 ----------------
{
 "id": "u9", "tier": "N2", "kind": "主張理解（長文）", "title": "舞台の裏側",
 "body": "学生のころ、演劇の部に入っていた。役者をやりたくて入ったのだが、"
         "体が固く、声も通らず、一年目で裏方に回された。"
         "正直に言えば、くやしかった。\n"
         "担当になったのは照明である。"
         "どの場面でどの明かりをどれだけ落とすか、"
         "台本を読みこんで決めていく。"
         "初めのうちは、ただ指示どおりに手を動かしていた。\n"
         "変わったのは、ある場面で明かりを一秒遅らせてみた日だ。"
         "役者がだまったまま立っている時間が、わずかに長くなる。"
         "それだけで、客席の空気が変わった。"
         "息をのむ音が、裏にいる自分のところまで届いたのである。\n"
         "①そのとき初めて分かった。舞台を作っているのは役者だけではない。"
         "明かり、音、まくの上げ下げ。どれも、見ている人の心の動き方を変えている。"
         "観客の目は役者に向いているが、"
         "その目の前の景色は、裏にいる人たちが一緒に作っている。\n"
         "卒業して別の仕事に移ったが、この経験はずっと残っている。"
         "どんな場所にも、前に立つ人と、見えないところで支える人がいる。"
         "そして支える側の小さな判断が、全体の印象を決めてしまうことがある。\n"
         "目立つかどうかと、効いているかどうかは、別のことなのだ。",
 "en": "At university I was in the drama society. I joined wanting to act, but my body was "
       "stiff and my voice did not carry, and in the first year I was moved behind the scenes. "
       "To be honest, it stung.\n"
       "I was put in charge of lighting — reading the script closely to decide which lights to "
       "bring down, how far, and in which scene. At first I simply moved my hands as "
       "instructed.\n"
       "What changed things was the day I tried delaying a light by one second in a certain "
       "scene. The time the actor stood there in silence grew very slightly longer. That alone "
       "changed the air in the auditorium. The sound of an indrawn breath reached me, "
       "backstage.\n"
       "That was when I first understood. It is not only the actors who make a performance. "
       "The lights, the sound, the raising and lowering of the curtain — each changes how the "
       "watcher's mind moves. The audience's eyes are on the actors, but the scene in front of "
       "those eyes is made together with the people behind.\n"
       "I graduated and took a different job, but the experience has stayed with me. In any "
       "setting there are people who stand at the front and people who support from out of "
       "sight. And a small judgement by the one supporting can decide the impression of the "
       "whole.\n"
       "Being noticed and having an effect are two different things.",
 "qs": [
   {"q": "一年目に裏方に回されたとき、筆者はどう感じたか。",
    "opts": ["ほっとした", "くやしかった", "楽しみだった", "気にならなかった"], "ans": 1,
    "why": "「正直に言えば、くやしかった」とあります。"},
   {"q": "明かりを一秒遅らせたとき、何が起きたか。",
    "opts": ["役者がせりふを間違えた",
             "客席の空気が変わった",
             "舞台が暗くなりすぎた",
             "役者が声を上げた"], "ans": 1,
    "why": "「それだけで、客席の空気が変わった」「息をのむ音が…届いた」とあります。"},
   {"q": "①そのとき初めて分かった とあるが、何が分かったのか。",
    "opts": ["照明の仕事のほうが役者より難しいこと",
             "舞台を作っているのは役者だけではないこと",
             "観客は明かりをよく見ていること",
             "台本を読みこむ必要があること"], "ans": 1,
    "why": "直後に「舞台を作っているのは役者だけではない」と続きます。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["裏方の仕事のほうが大切だ",
             "前に立つ人になるべきだ",
             "目立つことと効いていることは別だ",
             "学生のうちに演劇を経験すべきだ"], "ans": 2,
    "why": "最後の一文「目立つかどうかと、効いているかどうかは、別のことなのだ」が"
           "主張です。1のように裏方が上だとは言っていません。"},
 ]},
# ---------------- 問題14 style: 情報検索 ----------------
{
 "id": "u10", "tier": "N2", "kind": "情報検索", "title": "みどり旅館 ご宿泊案内",
 "body": "みどり旅館　ご宿泊のご案内\n"
         "■お部屋と料金（お一人様・一泊二食付き）\n"
         "※下の表をご確認ください。\n"
         "■お子様について\n"
         "小学生は大人料金の半額、三歳以下は無料です。"
         "（三歳以下のお子様にはお食事とおふとんは付きません。）\n"
         "■お食事\n"
         "夕食は午後六時から、朝食は午前七時からです。"
         "苦手な材料がございましたら、三日前までにお知らせください。\n"
         "■ご予約の変更・取り消し\n"
         "前日までは無料です。当日の取り消しは、料金の三割をいただきます。\n"
         "■送迎\n"
         "駅から宿までの送迎は無料ですが、前日までのご予約が必要です。",
 "table": {
   "head": ["お部屋", "平日", "土曜・休前日"],
   "rows": [["和室（庭が見えます）", "一万二千円", "一万五千円"],
            ["洋室", "一万円", "一万三千円"],
            ["和室（広め・六名まで）", "一万四千円", "一万七千円"]]},
 "en": "Midori-so — accommodation guide\n"
       "■ Rooms and rates (per person, one night with two meals)\n"
       "Please see the table below.\n"
       "■ Children\n"
       "Primary school children are half the adult rate; children of three and under are free. "
       "(Children of three and under are not provided with meals or bedding.)\n"
       "■ Meals\n"
       "Dinner is from 6pm and breakfast from 7am. If there are ingredients you dislike, please "
       "let us know at least three days in advance.\n"
       "■ Changes and cancellations\n"
       "Free up to the day before. Cancellation on the day incurs 30% of the rate.\n"
       "■ Transfers\n"
       "Transfers between the station and the inn are free, but must be booked by the day "
       "before.",
 "qs": [
   {"q": "土曜日に、大人二人と小学生一人が洋室に泊まる場合、"
         "全部でいくらか。",
    "opts": ["三万三千円", "三万二千五百円", "二万六千円", "三万九千円"], "ans": 1,
    "why": "洋室の土曜は一人一万三千円。大人二人で二万六千円、"
           "小学生はその半額の六千五百円。合わせて三万二千五百円です。"},
   {"q": "この宿について、正しいものはどれか。",
    "opts": ["駅からの送迎は当日でも頼める",
             "苦手な材料は前日までに伝えればよい",
             "前日までの取り消しなら料金はかからない",
             "三歳以下の子どもにも食事が付く"], "ans": 2,
    "why": "「前日までは無料です」とあります。送迎も食事の連絡も前もって必要で、"
           "三歳以下に食事は付きません。"},
 ]},
]
