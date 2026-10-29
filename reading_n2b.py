# -*- coding: utf-8 -*-
"""Second N2 batch: more of all five 読解 shapes."""

PASSAGES = [
# ---------- 内容理解（短文） ----------
{
 "id": "s1", "tier": "N2", "kind": "内容理解（短文）", "title": "あいさつ",
 "body": "朝、近所の人にあいさつをしても、返ってこないことがある。以前は気になっていたが、"
         "今は気にしないことにしている。\n"
         "相手にも都合があるのだろう。考え事をしているのかもしれないし、"
         "急いでいるのかもしれない。返事がないことに理由を求めると、"
         "こちらの気持ちまで重くなってしまう。\n"
         "あいさつは、返してもらうためにするものではない。"
         "そう思うようになってから、声を出すのが楽になった。",
 "en": "In the morning I sometimes greet a neighbour and get nothing back. It used to bother "
       "me, but now I have decided not to mind. They have their own circumstances. They may be "
       "lost in thought, or in a hurry. If you go looking for a reason behind the lack of a "
       "reply, your own mood grows heavy too. A greeting is not something you do in order to "
       "have it returned. Since I came to think that way, speaking up has become easier.",
 "qs": [
   {"q": "筆者はあいさつについてどう考えているか。",
    "opts": ["返事をしない人にはしないほうがよい",
             "返してもらうためにするものではない",
             "近所の人には必ずするべきだ",
             "急いでいるときはしなくてよい"], "ans": 1,
    "why": "「あいさつは、返してもらうためにするものではない」と述べています。"},
 ]},
{
 "id": "s2", "tier": "N2", "kind": "内容理解（短文）", "title": "メモの取り方",
 "body": "仕事を覚えるのが早い人は、よくメモを取ると言われる。しかし、ただ書けばよい"
         "というわけではない。\n"
         "書くことに集中しすぎると、相手の話の流れを見失ってしまう。"
         "大切なのは、あとで思い出せるだけの印を残し、残りは頭で追うことだ。\n"
         "全部書き取ろうとして、結局何も残らなかった。"
         "そんな経験のある人は、少なくないのではないだろうか。",
 "en": "People who pick up a job quickly are said to take plenty of notes. But it is not simply "
       "a matter of writing. If you concentrate too hard on writing, you lose the thread of "
       "what the other person is saying. What matters is leaving just enough of a mark to "
       "remember by later, and following the rest in your head. Trying to write down "
       "everything and ending up with nothing — there are surely plenty of people who have had "
       "that experience.",
 "qs": [
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["話は全部書き取ったほうがよい",
             "メモを取らないほうが覚えやすい",
             "思い出せる程度に書き、話は頭で追うのがよい",
             "メモを多く取る人ほど仕事を早く覚える"], "ans": 2,
    "why": "「あとで思い出せるだけの印を残し、残りは頭で追うことだ」とあります。"},
 ]},
{
 "id": "s3", "tier": "N2", "kind": "内容理解（短文）", "title": "天気予報",
 "body": "天気予報が外れたと腹を立てる人がいる。しかし予報は、「必ずこうなる」という約束ではなく、"
         "「こうなりやすい」という見通しである。\n"
         "外れることもあると分かったうえで、かさを持つかどうかを自分で決める。"
         "それが予報の正しい使い方だろう。\n"
         "当たるかどうかより、どう使うかのほうが、ずっと大切なのである。",
 "en": "Some people get angry when the weather forecast is wrong. But a forecast is not a "
       "promise that something will certainly happen; it is an outlook saying what is likely. "
       "Understanding that it can be wrong, you decide for yourself whether to take an "
       "umbrella. That, surely, is the right way to use a forecast. How you use it matters far "
       "more than whether it turns out right.",
 "qs": [
   {"q": "筆者は天気予報をどのようなものだと考えているか。",
    "opts": ["必ず当たるようにすべきもの",
             "外れることもある見通し",
             "信じる必要のないもの",
             "かさを持つかどうかを決めてくれるもの"], "ans": 1,
    "why": "「『必ずこうなる』という約束ではなく、『こうなりやすい』という見通しである」"
           "とあります。"},
 ]},
# ---------- 内容理解（中文） ----------
{
 "id": "m1", "tier": "N2", "kind": "内容理解（中文）", "title": "町の自転車",
 "body": "わたしの住む町では、数年前から自転車の貸し出しが始まった。駅前や公園など、"
         "町のあちこちに置き場があり、どこで借りてどこで返してもよい。\n"
         "始まったころは、利用する人が少なかった。料金が高いわけでもないのに、"
         "なぜ広がらないのか、①不思議に思っていた。\n"
         "理由が分かったのは、自分で使ってみたときだった。借りるのは簡単だが、"
         "返そうとすると、置き場がいっぱいで入らないのである。"
         "別の置き場を探して走り回ることになり、かえって時間がかかってしまう。\n"
         "その後、どこが空いているかが画面で分かるようになると、利用者は急に増えた。"
         "よい仕組みを作っても、使う人の不安を減らさなければ広がらない。"
         "そのことを、この町の自転車が教えてくれた。",
 "en": "In the town where I live, a bicycle-hire scheme started a few years ago. There are "
       "stands all over town — by the station, in the parks — and you may borrow at one and "
       "return at any other. When it began, few people used it. The price was not high, so I "
       "wondered why it was not catching on. I understood the reason when I tried it myself. "
       "Borrowing is easy, but when you go to return it the stand is full and there is no "
       "space. You end up riding around looking for another one, which takes longer than it "
       "would have. Later, once you could see on screen which stands had space, users suddenly "
       "increased. You can build a good system, but it will not spread unless you reduce the "
       "anxiety of the people using it. That is what this town's bicycles taught me.",
 "qs": [
   {"q": "①不思議に思っていた とあるが、何が不思議だったのか。",
    "opts": ["置き場が町のあちこちにあること",
             "料金が高くないのに利用者が少ないこと",
             "どこで返してもよいという仕組み",
             "借りるのが簡単だということ"], "ans": 1,
    "why": "直前に「料金が高いわけでもないのに、なぜ広がらないのか」とあります。"},
   {"q": "利用者が急に増えたのはなぜか。",
    "opts": ["料金が安くなったから",
             "置き場の数が増えたから",
             "空いている置き場が分かるようになったから",
             "自転車の数が増えたから"], "ans": 2,
    "why": "「どこが空いているかが画面で分かるようになると、利用者は急に増えた」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["よい仕組みは作れば自然に広がる",
             "町の自転車は便利な乗り物だ",
             "使う人の不安を減らさなければ広がらない",
             "借りる前に置き場を調べておくべきだ"], "ans": 2,
    "why": "最後に「使う人の不安を減らさなければ広がらない」とまとめています。"},
 ]},
{
 "id": "m2", "tier": "N2", "kind": "内容理解（中文）", "title": "古い写真",
 "body": "引っ越しの用意をしていて、古い写真の入った箱が出てきた。"
         "手が止まり、気がつくと一時間ほどながめていた。\n"
         "写っているのは、特別な日の写真ばかりではない。"
         "台所で母が何かを切っているうしろ、父の机の上に置かれた新聞。"
         "どうしてこんなものをとったのか、自分でも思い出せない。\n"
         "②しかし、心に残っているのはそういう一枚のほうだった。"
         "旅行先で笑って並んだ写真は、どこでとったかさえあいまいなのに、"
         "何でもない台所の写真には、その日の音やにおいまでついてくる。\n"
         "大事な日を残そうとして、わたしたちは写真をとる。"
         "けれども後で助けてくれるのは、たまたま写してしまった何でもない時間の"
         "ほうなのかもしれない。",
 "en": "While getting ready to move I came across a box of old photographs. My hands stopped, "
       "and before I knew it I had spent about an hour looking at them. What is in them is not "
       "only special days. My mother's back as she cuts something in the kitchen; the "
       "newspaper left on my father's desk. I cannot even remember why I took such pictures. "
       "And yet it was those ones that had stayed with me. In the photographs where we stood "
       "laughing on a trip, I am no longer sure even where they were taken, while the "
       "ordinary kitchen picture brings the sounds and smells of that day along with it. We "
       "take photographs meaning to keep hold of important days. But what helps us later may "
       "be the nothing-in-particular hours we happened to capture.",
 "qs": [
   {"q": "②しかし とあるが、何に対して「しかし」と言っているのか。",
    "opts": ["一時間もながめてしまったこと",
             "なぜとったのか思い出せないこと",
             "特別な日の写真が多いこと",
             "引っ越しの用意が進まないこと"], "ans": 1,
    "why": "直前の「どうしてこんなものをとったのか、自分でも思い出せない」を受けています。"},
   {"q": "旅行先の写真について、筆者はどう述べているか。",
    "opts": ["よくとれていて今でも気に入っている",
             "どこでとったかさえはっきりしない",
             "音やにおいまで思い出せる",
             "特別な日なので大切にしている"], "ans": 1,
    "why": "「どこでとったかさえあいまいなのに」とあります。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["特別な日の写真こそ残すべきだ",
             "写真はとらないほうが心に残る",
             "何でもない時間の写真が後で助けてくれる",
             "古い写真は早く片づけたほうがよい"], "ans": 2,
    "why": "最後に「後で助けてくれるのは…何でもない時間のほう」と述べています。"},
 ]},
{
 "id": "m3", "tier": "N2", "kind": "内容理解（中文）", "title": "駅前の本屋",
 "body": "駅前に、三十年続いている小さな本屋がある。広くはないし、"
         "品ぞろえが特別よいわけでもない。それでも客が絶えない。\n"
         "理由は、店主にある。何度か通うと、その人がどんな本を手に取るかを覚えていて、"
         "次に行ったとき「これ、好きだと思いますよ」と一冊すすめてくれる。"
         "すすめられた本が外れることは、ほとんどない。\n"
         "同じことを機械がしようとすれば、過去に買った本から似た本を選ぶだろう。"
         "だが店主がすすめるのは、似た本とはかぎらない。"
         "「そろそろ別の種類も読んでみては」と、"
         "こちらが思いつきもしなかった一冊を差し出してくることがある。\n"
         "買った記録から分かるのは、その人の過去である。"
         "店主が見ているのは、たぶんその先だ。",
 "en": "By the station there is a small bookshop that has lasted thirty years. It is not "
       "large, and its selection is nothing special. Even so, the customers keep coming. The "
       "reason is the owner. Visit a few times and he remembers what sort of books you pick "
       "up, and the next time you come he recommends one: “I think you'd like this.” What he "
       "recommends is almost never wrong. If a machine tried to do the same, it would choose "
       "books similar to ones you had bought before. But what the owner recommends is not "
       "necessarily similar. Sometimes he holds out a book you would never have thought of, "
       "saying, “perhaps it's time you tried another kind.” What a purchase record reveals is "
       "a person's past. What the owner is looking at is, I suspect, what comes after it.",
 "qs": [
   {"q": "客が絶えないのはなぜか。",
    "opts": ["店が広くて品ぞろえがよいから",
             "店主が客に合う本をすすめてくれるから",
             "駅前にあって通いやすいから",
             "三十年続いている古い店だから"], "ans": 1,
    "why": "「理由は、店主にある」として、客に合う一冊をすすめてくれることを挙げています。"},
   {"q": "機械と店主のちがいは何か。",
    "opts": ["機械のほうが早く本を選べる",
             "機械は似た本を選ぶが、店主はそうとはかぎらない",
             "店主は過去に買った本を覚えていない",
             "機械のほうが多くの本を知っている"], "ans": 1,
    "why": "「機械は…似た本を選ぶ」のに対し「店主がすすめるのは、似た本とはかぎらない」"
           "とあります。"},
   {"q": "最後の段落で筆者が言いたいことは何か。",
    "opts": ["買った記録を残しておくことが大切だ",
             "店主はその人のこれからを見ている",
             "機械には本の良さが分からない",
             "過去を知らなければ本はすすめられない"], "ans": 1,
    "why": "「記録から分かるのは…過去」「店主が見ているのは、たぶんその先」とあります。"},
 ]},
# ---------- 統合理解 ----------
{
 "id": "g1", "tier": "N2", "kind": "統合理解", "title": "家で働くこと",
 "body": "Ａ\n"
         "家で働けるようになって、通勤の時間がなくなった。その分を家族と過ごしたり、"
         "休んだりできるようになり、体も楽になった。会社にいると、"
         "話しかけられて作業が止まることが多かったが、家ではそれがない。"
         "集中できる時間が増えた分、同じ仕事を短い時間で終えられるようになったと感じている。"
         "もちろん相談しにくい場面はあるが、それは連絡の取り方をくふうすれば足りることだ。\n"
         "Ｂ\n"
         "家で働くことには、見えにくい問題がある。仕事と生活の境目がなくなることだ。"
         "机がそのまま食事の場所である以上、画面を閉じても仕事の続きが頭に残る。"
         "通勤は面倒だが、あの時間が気持ちを切りかえる役目を果たしていたのだと、"
         "なくなってから気づいた。"
         "また、困っている様子が人の目に入らないので、"
         "一人で抱えこんだまま時間が過ぎてしまうこともある。",
 "en": "A. Since I have been able to work from home, commuting time has disappeared. I can "
       "spend that time with my family or resting, and physically it is easier. At the office "
       "I was often interrupted mid-task, which does not happen at home. With more time to "
       "concentrate, I feel I now finish the same work in less time. There are of course "
       "moments when it is harder to consult someone, but that can be handled by being "
       "thoughtful about how you keep in touch.\n"
       "B. Working from home has a problem that is hard to see: the boundary between work and "
       "life disappears. When your desk is also where you eat, closing the screen does not "
       "stop work carrying on in your head. Commuting is a nuisance, but I realised only after "
       "losing it that those minutes served to switch my mind over. Also, because nobody can "
       "see that you are struggling, time can pass with you carrying it alone.",
 "qs": [
   {"q": "ＡとＢが共通して述べていることは何か。",
    "opts": ["家で働くと仕事が早く終わる",
             "通勤の時間がなくなったこと",
             "一人で問題を抱えこみやすいこと",
             "家族と過ごす時間が増えたこと"], "ans": 1,
    "why": "Ａは「通勤の時間がなくなった」、Ｂも「通勤…あの時間が…なくなってから」と"
           "述べています。他はどちらか一方だけの内容です。"},
   {"q": "Ａと比べたときのＢに見られる考え方はどれか。",
    "opts": ["家で働くことの利点を多くあげている",
             "通勤の時間をむだだと考えている",
             "失われたものに目を向けている",
             "連絡の取り方をくふうすべきだとしている"], "ans": 2,
    "why": "Ｂは「境目がなくなる」「切りかえる役目」「人の目に入らない」と、"
           "失われたものに注目しています。4はＡの内容です。"},
 ]},
{
 "id": "g2", "tier": "N2", "kind": "統合理解", "title": "店に案内の人は必要か",
 "body": "Ａ\n"
         "最近は、店に入っても店員が声をかけてこない店が増えた。"
         "わたしはこのほうがありがたい。ゆっくり見たいだけなのに話しかけられると、"
         "買わなければいけないような気がして、落ち着かない。"
         "必要なときはこちらから聞けばよいのだから、だまって待っていてくれるほうが助かる。"
         "選ぶ時間をじゃまされないことも、よい買い物のじょうけんだと思う。\n"
         "Ｂ\n"
         "声をかけられたくない客がいるのは分かる。しかし、"
         "何も知らない客にとっては、どこから見ればよいのかさえ分からないことがある。"
         "自分から聞けると言うが、何を聞けばよいか分かる客は、すでにくわしい客である。"
         "必要なのは、声をかけないことではなく、"
         "客の様子を見て、必要なときにだけ近づける店員ではないだろうか。",
 "en": "A. These days more shops leave you alone when you walk in. I am grateful for this. "
       "When I only want to look around slowly and someone speaks to me, I feel I am obliged "
       "to buy, which is unsettling. I can ask when I need to, so I would rather they waited "
       "quietly. Not having your time to choose interrupted is part of what makes shopping "
       "good.\n"
       "B. I understand that some customers do not want to be approached. But for a customer "
       "who knows nothing, it can be unclear even where to start looking. People say you can "
       "ask, but a customer who knows what to ask already knows a good deal. What is needed is "
       "not staying away, but staff who watch how a customer is doing and come over only when "
       "they are needed.",
 "qs": [
   {"q": "Ａが店員に望んでいることはどれか。",
    "opts": ["必要なときにだけ近づいてくること",
             "だまって待っていてくれること",
             "くわしく商品を説明してくれること",
             "客の様子をよく見ていること"], "ans": 1,
    "why": "Ａは「だまって待っていてくれるほうが助かる」と述べています。1と4はＢの考えです。"},
   {"q": "Ｂは、Ａのどの点に疑問を示しているか。",
    "opts": ["買わなければいけない気がするという点",
             "必要なときは自分から聞けばよいという点",
             "ゆっくり選びたいという点",
             "店員が声をかける店が減ったという点"], "ans": 1,
    "why": "Ｂは「何を聞けばよいか分かる客は、すでにくわしい客である」と、"
           "自分から聞けばよいという考えに疑問を示しています。"},
 ]},
# ---------- 主張理解（長文） ----------
{
 "id": "l1", "tier": "N2", "kind": "主張理解（長文）", "title": "数で測るということ",
 "body": "何かを良くしようとするとき、まず数で測ろうとする。"
         "売り上げ、人数、点数。数にすれば、増えたか減ったかがはっきりする。"
         "話し合いも早く進む。だから数で測ること自体は、悪いことではない。\n"
         "問題は、測りやすいものだけが残っていくことである。\n"
         "以前、ある図書館で本の貸し出し数を増やす取り組みが行われた。"
         "もくひょうを決め、毎月の数を全員で確かめる。半年後、数は確かに増えた。"
         "しかし、職員に話を聞くと、表情は明るくなかった。"
         "①数は増えたが、大事にしていたものが減ったというのである。\n"
         "その図書館では、本を探している人に時間をかけて話を聞き、"
         "ときには一冊も借りずに帰る人とも長く話していた。"
         "その時間は数に表れない。貸し出し数を追ううちに、"
         "すぐに借りてもらえそうな本をすすめるようになり、"
         "長い相談は後回しになっていった。\n"
         "測れないものに、重みがないわけではない。"
         "ただ、数の横に並べて比べることができないだけである。"
         "にもかかわらず、比べられるものだけを見て判断を続ければ、"
         "比べられないものは、静かに消えていく。\n"
         "数で測るなと言いたいのではない。測った数の外に何があるかを、"
         "ときどき思い出すべきだと言いたいのである。",
 "en": "When we try to improve something, we first try to measure it. Sales, head counts, "
       "scores. Turn it into a number and it is clear whether it rose or fell; discussion moves "
       "faster. So measuring in numbers is not itself a bad thing. The problem is that only "
       "what is easy to measure survives. Some time ago, a library ran a drive to increase the "
       "number of loans. They set a target and checked the monthly figure together. Six months "
       "later the number had indeed risen. But when I spoke to the staff, their faces were not "
       "bright. The number had gone up, they said, but something they valued had gone down. At "
       "that library, they used to take time listening to people looking for a book, sometimes "
       "talking at length with someone who left without borrowing anything. That time does not "
       "show up in a figure. As they chased the loan count, they began recommending books "
       "likely to be borrowed straight away, and long consultations were pushed to later. It "
       "is not that unmeasurable things carry no weight. It is only that they cannot be lined "
       "up beside a number and compared. And yet if we keep judging by looking only at what "
       "can be compared, what cannot be compared quietly disappears. I do not mean that we "
       "should stop measuring. I mean we should remember, now and then, what lies outside the "
       "number we measured.",
 "qs": [
   {"q": "筆者は、数で測ることをどう考えているか。",
    "opts": ["すぐにやめるべきだ",
             "それ自体は悪いことではない",
             "正しいねらいがなければ意味がない",
             "図書館には合わない方法だ"], "ans": 1,
    "why": "「だから数で測ること自体は、悪いことではない」とあります。"},
   {"q": "①数は増えたが、大事にしていたものが減った とあるが、減ったものは何か。",
    "opts": ["図書館に置かれている本の数",
             "本を借りずに帰る人の数",
             "人の相談にゆっくり時間をかけること",
             "職員どうしで話し合う時間"], "ans": 2,
    "why": "「時間をかけて話を聞き…長く話していた」時間が、"
           "「長い相談は後回しになっていった」と述べられています。"},
   {"q": "「比べられないものは、静かに消えていく」とあるが、なぜか。",
    "opts": ["数で表せないものには重みがないから",
             "比べられるものだけを見て判断が続くから",
             "職員が必要だと考えていないから",
             "ねらいを決めることができないから"], "ans": 1,
    "why": "「比べられるものだけを見て判断を続ければ」そうなる、という流れです。"
           "1は「重みがないわけではない」と本文が否定しています。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["数で測るのはやめたほうがよい",
             "ねらいは低めに決めたほうがよい",
             "測った数の外にあるものを忘れてはいけない",
             "図書館は貸し出し数を増やすべきではない"], "ans": 2,
    "why": "最後に「測った数の外に何があるかを、ときどき思い出すべきだ」とまとめています。"},
 ]},
# ---------- 情報検索 ----------
{
 "id": "i1", "tier": "N2", "kind": "情報検索", "title": "ごみの出し方のご案内",
 "body": "さくら町　ごみの出し方\n"
         "■出す時間\n"
         "収集日の朝八時までに出してください。前の日の夜に出すことはできません。\n"
         "■もえるごみ（月・木）\n"
         "台所のごみ、紙くずなど。町の指定ぶくろに入れてください。\n"
         "■もえないごみ（第一・第三水曜）\n"
         "こわれたしょっき、小さな金ぞくなど。中身が見えるふくろに入れてください。\n"
         "■新聞・雑誌（第二・第四水曜）\n"
         "ひもでしばって出してください。ふくろに入れたものは収集できません。\n"
         "■大きなごみ（たんす・自転車など）\n"
         "収集日はありません。前もって町の係に電話で申し込み、"
         "コンビニで券を買ってはってから、指定された日に出してください。"
         "一点につき五百円から二千円です。\n"
         "※引っ越しで一度に多く出す場合は、大きなごみと同じく、電話でご相談ください。",
 "en": "Sakura Town rubbish guide. Times: put rubbish out by 8am on the collection day; it may "
       "not be put out the night before. Burnable (Mon/Thu): kitchen waste, paper scraps; use "
       "the town's designated bags. Non-burnable (1st and 3rd Wed): broken crockery, small "
       "metal items; use a bag whose contents are visible. Newspapers and magazines (2nd and "
       "4th Wed): tie with string; bagged items cannot be collected. Large items (chests of "
       "drawers, bicycles, etc.): no collection day. Apply in advance by telephone to the town "
       "office, buy a ticket at a convenience store and attach it, then put the item out on "
       "the day specified. 500 to 2,000 yen per item. Note: if you are moving and need to "
       "dispose of a large amount at once, please telephone, as with large items.",
 "qs": [
   {"q": "古い自転車を捨てたい人は、まず何をしなければならないか。",
    "opts": ["コンビニで券を買う",
             "町の係に電話で申し込む",
             "第一水曜の朝に出す",
             "中身が見えるふくろに入れる"], "ans": 1,
    "why": "「前もって町の係に電話で申し込み、コンビニで券を買って」とあり、"
           "電話が先です。"},
   {"q": "ごみの出し方として、正しいものはどれか。",
    "opts": ["雑誌はふくろに入れて第二水曜に出す",
             "もえるごみは前の日の夜に出してもよい",
             "新聞はひもでしばって第四水曜に出す",
             "こわれたしょっきは月曜に出す"], "ans": 2,
    "why": "新聞・雑誌は第二・第四水曜、ひもでしばって出します。"
           "ふくろに入れたものは収集できず、夜に出すこともできません。"},
 ]},
{
 "id": "i2", "tier": "N2", "kind": "情報検索", "title": "スポーツセンター 利用案内",
 "body": "みなと区スポーツセンター　ご利用案内\n"
         "■開いている時間\n"
         "平日　午前九時〜午後九時／土日　午前九時〜午後六時／毎月第三月曜は休みです。\n"
         "■料金（二時間まで）\n"
         "大人　四百円／中学生・高校生　二百円／小学生以下　無料\n"
         "区内にお住まいの方、または区内にお勤め・通学の方は、それぞれ半額になります。\n"
         "受付で、住所・勤務先・学校が確認できるものをお見せください。\n"
         "■二時間を超える場合\n"
         "三十分ごとに百円が加わります。（小学生以下は加わりません。）\n"
         "■貸し出し\n"
         "くつ　二百円／ラケット　三百円　※タオルの貸し出しはありません。\n"
         "■注意\n"
         "小学生以下の方だけでのご利用はできません。必ず大人とお越しください。",
 "en": "Minato Ward Sports Centre guide. Opening hours: weekdays 9am–9pm; weekends 9am–6pm; "
       "closed the third Monday of each month. Fees (up to two hours): adults 400 yen; junior "
       "and senior high school students 200 yen; primary school age and younger free. Those "
       "living, working or studying in the ward pay half of each. Show proof of address, "
       "workplace or school at reception. Beyond two hours: 100 yen per additional 30 minutes "
       "(not charged for primary age and younger). Hire: shoes 200 yen, racket 300 yen. Towels "
       "are not available for hire. Note: primary-age children and younger may not use the "
       "centre alone and must come with an adult.",
 "qs": [
   {"q": "区内に住む大人が、ラケットを借りて三時間利用する場合、全部でいくらか。",
    "opts": ["五百円", "七百円", "九百円", "千百円"], "ans": 1,
    "why": "区内在住なので二時間まで二百円。超えた一時間で百円が二回、合わせて二百円。"
           "ラケット三百円を足して七百円です。"},
   {"q": "利用について、正しいものはどれか。",
    "opts": ["日曜日は午後九時まで利用できる",
             "小学生だけでも利用できる",
             "第三月曜日は休みである",
             "タオルは受付で借りられる"], "ans": 2,
    "why": "「毎月第三月曜は休み」とあります。土日は午後六時まで、"
           "小学生以下だけの利用はできず、タオルの貸し出しもありません。"},
 ]},
]
