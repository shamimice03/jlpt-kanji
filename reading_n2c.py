# -*- coding: utf-8 -*-
"""Third N2 batch, written to the shape of the official 2018 reading section:
a conditions notice, two abstract-concept essays, a contrast essay, a long
experience-to-principle piece, and an information page with a real table."""

PASSAGES = [
{
 "id": "t1", "tier": "N2", "kind": "内容理解（短文）", "title": "十一月の割引のお知らせ",
 "body": "いつもご利用いただき、ありがとうございます。\n"
         "十一月は、会員の皆様に二つの割引をご用意しました。\n"
         "新商品「冬のブレンド」を十一月中にご注文いただくと、二割引きになります。"
         "それ以外の商品は、三千円以上のご注文で一割引きです。\n"
         "なお、二つの割引を合わせてお使いいただくことはできません。"
         "十二月からは、いつものねだんにもどります。",
 "en": "Thank you for your continued custom.\n"
       "For November we have prepared two discounts for members.\n"
       "Order the new product “Winter Blend” during November and you receive 20% off. "
       "Other products are 10% off on orders of 3,000 yen or more.\n"
       "Please note that the two discounts cannot be combined. "
       "From December, prices return to normal.",
 "qs": [
   {"q": "十一月にこの店で買い物をする場合、正しいものはどれか。",
    "opts": ["新商品を注文すれば、どの商品も二割引きになる",
             "三千円以上注文すれば、新商品も二割引きと一割引きの両方が受けられる",
             "新商品は二割引き、それ以外は三千円以上で一割引きになる",
             "十二月に注文しても、同じ割引が受けられる"], "ans": 2,
    "why": "新商品は二割引き、それ以外は三千円以上で一割引きです。"
           "「二つの割引を合わせて…できません」とあるので2は誤り、"
           "十二月からはもとのねだんにもどります。"},
 ]},
{
 "id": "t2", "tier": "N2", "kind": "内容理解（中文）", "title": "「ふつう」ということ",
 "body": "「ふつうでいい」と人はよく言う。しかし、ふつうとは何だろうか。\n"
         "ふつうは、多くの人がそうしているという意味で使われることが多い。"
         "だが、多いというだけでは、それが正しいとも、自分に合っているとも言えない。\n"
         "①ここにおとしあながある。ふつうを目指しているつもりで、"
         "実は「人と同じ」を目指してしまうのだ。"
         "同じであれば安心できるが、安心と満足は別のものである。\n"
         "ふつうという言葉には、もう一つの意味がある。"
         "無理をしていない、という意味だ。こちらのふつうなら、目指すねうちがある。\n"
         "人と同じかどうかではなく、自分が無理をしていないかどうか。"
         "同じ言葉でも、どちらの意味で使っているかによって、生き方は大きく変わってくる。",
 "en": "People often say “ordinary is fine.” But what is ordinary?\n"
       "Ordinary is most often used to mean that many people do it that way. Yet being common "
       "alone does not make something right, or make it suit you.\n"
       "Here is the pitfall. You think you are aiming at ordinary, when in fact you are aiming "
       "at being the same as other people. Sameness is reassuring, but reassurance and "
       "satisfaction are different things.\n"
       "The word ordinary has another sense: not forcing yourself. That ordinary is worth "
       "aiming at.\n"
       "Not whether you are the same as others, but whether you are forcing yourself. With the "
       "same word, which of the two senses you mean changes how you live a great deal.",
 "qs": [
   {"q": "①ここにおとしあながある とあるが、どんなおとしあなか。",
    "opts": ["ふつうを目指すと、人より下になってしまうこと",
             "ふつうを目指すつもりで、人と同じを目指してしまうこと",
             "ふつうという言葉の意味が人によってちがうこと",
             "安心を求めると、無理をしてしまうこと"], "ans": 1,
    "why": "直後に「ふつうを目指しているつもりで、実は『人と同じ』を目指してしまう」"
           "と説明されています。"},
   {"q": "筆者は「ふつう」の二つの意味をどう考えているか。",
    "opts": ["どちらも目指す値うちがない",
             "どちらも同じ意味で使ってよい",
             "人と同じという意味より、無理をしていないという意味のほうがよい",
             "無理をしていないという意味は使われなくなった"], "ans": 2,
    "why": "「こちらのふつうなら、目指すねうちがある」と、"
           "無理をしていないという意味のほうを認めています。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["ふつうという言葉は使わないほうがよい",
             "人と同じであれば安心できる",
             "どちらの意味で使うかで生き方が変わる",
             "多くの人がしていることは正しい"], "ans": 2,
    "why": "最後に「どちらの意味で使っているかによって、生き方は大きく変わってくる」"
           "とまとめています。"},
 ]},
{
 "id": "t3", "tier": "N2", "kind": "内容理解（中文）", "title": "手紙とメール",
 "body": "メールは早い。思いついたときに書いて、すぐに送れる。"
         "相手も、都合のよいときに読めばよい。便利な道具である。\n"
         "では、手紙はもう必要ないのかというと、そうではないと思う。"
         "手紙には、メールにはない時間が入っているからだ。\n"
         "便せんを選び、万年筆を出し、書き間違えればはじめからやり直す。"
         "書き終えても、すぐには届かない。その間、"
         "書いた人は相手のことを思い続けることになる。\n"
         "②受け取る側も、それを感じ取る。封を開けるとき、"
         "そこに使われた時間ごと受け取っているのである。\n"
         "早く伝えたいことはメールで送ればよい。"
         "しかし、時間をかけたという事実そのものを伝えたいとき、"
         "手紙にかなうものは、今のところない。",
 "en": "Email is fast. You write when it occurs to you and send it at once, and the other "
       "person can read it whenever suits them. It is a useful tool.\n"
       "Does that mean letters are no longer needed? I do not think so. A letter contains time "
       "that email does not.\n"
       "You choose the paper, take out the pen, and start again from the beginning if you make "
       "a mistake. Even when you have finished, it does not arrive at once. During that "
       "interval, the writer goes on thinking about the person.\n"
       "The receiver senses it too. When they open the envelope, they are receiving the time "
       "spent on it along with the words.\n"
       "Anything you want to convey quickly can go by email. But when what you want to convey "
       "is the very fact that you spent time, nothing yet matches a letter.",
 "qs": [
   {"q": "筆者はメールをどのようなものだと考えているか。",
    "opts": ["便利だが心がこもらないもの",
             "早く送れて相手も都合よく読める便利な道具",
             "手紙より失礼になりやすいもの",
             "もう使う必要のないもの"], "ans": 1,
    "why": "「思いついたときに書いて、すぐに送れる…便利な道具である」と述べています。"
           "心がこもらないとは言っていません。"},
   {"q": "②受け取る側も、それを感じ取る とあるが、何を感じ取るのか。",
    "opts": ["書いた人の字のうまさ",
             "便せんや万年筆のよさ",
             "手紙にかけられた時間",
             "すぐに返事をすべきだということ"], "ans": 2,
    "why": "「そこに使われた時間ごと受け取っている」とあります。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["手紙よりメールのほうがすぐれている",
             "大事な用件は必ず手紙で送るべきだ",
             "時間をかけたこと自体を伝えたいときは手紙がよい",
             "メールは急ぎの用件にしか使えない"], "ans": 2,
    "why": "「時間をかけたという事実そのものを伝えたいとき、手紙にかなうものは…ない」"
           "と述べています。2のように「必ず」とは言っていません。"},
 ]},
{
 "id": "t4", "tier": "N2", "kind": "統合理解", "title": "図書館は何を置くべきか",
 "body": "Ａ\n"
         "人気のある本を図書館が何冊も買うことに、反対する人がいる。"
         "しかし、読みたい本が半年も待たないと借りられないのでは、"
         "図書館に足を運ぶ人は減ってしまう。まず来てもらうことが先ではないか。"
         "人気の本をきっかけに通いはじめた人が、"
         "やがて本だなの奥の一冊に手を伸ばすこともある。"
         "入り口を広くすることは、けっしてむだではない。\n"
         "Ｂ\n"
         "同じ本を何冊も並べれば、そのぶん別の本が買えなくなる。"
         "人気の本は書店でも手に入るし、少し待てば順番も回ってくる。"
         "図書館にしか置けないのは、売れないけれども必要な本のほうである。"
         "待つ人を減らすことより、"
         "ほかのどこにもない一冊を残すことに、"
         "公共の図書館の役目があると思う。",
 "en": "A. Some people object to libraries buying many copies of popular books. But if you have "
       "to wait half a year to borrow the book you want, fewer people will come to the library "
       "at all. Surely getting them through the door comes first. Someone who starts visiting "
       "because of a popular book may in time reach for a volume at the back of the shelves. "
       "Widening the entrance is by no means wasted effort.\n"
       "B. Line up many copies of the same book and you cannot buy other books with that money. "
       "Popular books can be had in bookshops, and wait a little and your turn comes round "
       "anyway. What only a library can hold is the book that does not sell but is needed. The "
       "role of a public library lies, I think, in keeping the one volume that exists nowhere "
       "else, rather than in reducing the number of people waiting.",
 "qs": [
   {"q": "人気の本を何冊も置くことについて、ＡとＢはどう考えているか。",
    "opts": ["ＡもＢも、置くべきだと考えている",
             "Ａは置くべきだと考え、Ｂは別の本に使うべきだと考えている",
             "Ａは置くべきでないと考え、Ｂは置くべきだと考えている",
             "ＡもＢも、書店で買えばよいと考えている"], "ans": 1,
    "why": "Ａは「入り口を広くすることは、けっしてむだではない」、"
           "Ｂは「そのぶん別の本が買えなくなる」と述べています。"},
   {"q": "図書館の役目について、Ｂはどう述べているか。",
    "opts": ["多くの人に本を読んでもらうこと",
             "書店にない本を安く貸し出すこと",
             "ほかのどこにもない一冊を残すこと",
             "待つ人の数をできるだけ減らすこと"], "ans": 2,
    "why": "「ほかのどこにもない一冊を残すことに、公共の図書館の役目がある」とあります。"
           "4はＢが否定している内容です。"},
 ]},
{
 "id": "t5", "tier": "N2", "kind": "主張理解（長文）", "title": "直せる人",
 "body": "祖父は、こわれたものを何でも直す人だった。"
         "いすの足がぐらつけば裏を見て、時計が止まれば裏ぶたを開ける。"
         "子どものわたしには、それがふしぎな力のように見えた。\n"
         "大人になって、自分でも少し直せるようになって分かったことがある。"
         "祖父が特別な技術を持っていたわけではない。"
         "ただ、こわれたものを前にしたとき、"
         "「直せるかもしれない」と最初に思うかどうかがちがっていたのだ。\n"
         "わたしたちは、こわれたものを見ると、"
         "まず新しいものの値段を調べる。直すという道があることを、"
         "考える前に通り過ぎてしまう。①その差は技術ではなく、順番の差である。\n"
         "もちろん、直らないものもある。直すより買うほうが安いことも多い。"
         "それでも、一度は中を見てみる。その習慣があるかどうかで、"
         "身の回りのものとの付き合い方は、ずいぶん変わってくる。\n"
         "祖父の道具箱は、今はわたしの部屋にある。"
         "特別なものは何も入っていない。"
         "入っているのは、開けてみるという習慣のほうだったのだと、今は思う。",
 "en": "My grandfather was a man who repaired anything that broke. If a chair leg wobbled he "
       "looked underneath; if a clock stopped he opened the back. To me as a child it looked "
       "like a strange kind of power.\n"
       "Having grown up and become able to fix a few things myself, I have understood "
       "something. It was not that my grandfather had special skill. It was that, faced with "
       "something broken, what differed was whether “maybe this can be fixed” was the first "
       "thought.\n"
       "When we see something broken, we first look up the price of a new one. We pass by the "
       "existence of repair as an option before we have considered it. That difference is not "
       "skill but order.\n"
       "Of course some things cannot be repaired, and often buying is cheaper than fixing. Even "
       "so, look inside once. Whether or not you have that habit changes a great deal about how "
       "you live with the things around you.\n"
       "My grandfather's toolbox is in my room now. There is nothing special in it. What was in "
       "it, I now think, was the habit of opening things up.",
 "qs": [
   {"q": "子どものころ、筆者は祖父をどう見ていたか。",
    "opts": ["道具を大切にする人だと見ていた",
             "ふしぎな力を持っているように見えた",
             "古いものを捨てられない人だと見ていた",
             "何でも自分でやりたがる人だと見ていた"], "ans": 1,
    "why": "「子どものわたしには、それがふしぎな力のように見えた」とあります。"},
   {"q": "①その差は技術ではなく、順番の差である とあるが、どういうことか。",
    "opts": ["直す技術を学ぶ順番がちがうということ",
             "直せるかどうかを先に考えるか、値段を先に調べるかのちがい",
             "古いものから先に直すか、新しいものから直すかのちがい",
             "祖父のほうが早く直せたということ"], "ans": 1,
    "why": "祖父は「直せるかもしれない」と最初に思い、わたしたちは「まず新しいものの値段を"
           "調べる」。何を先に考えるかの差だと述べています。"},
   {"q": "筆者は、直らないものについてどう述べているか。",
    "opts": ["直らないものはないと考えている",
             "直らないものもあるが、一度は中を見てみるとよい",
             "直らないとわかったらすぐ買うべきだ",
             "直らないものを直そうとするのはむだだ"], "ans": 1,
    "why": "「直らないものもある…それでも、一度は中を見てみる」とあります。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["祖父の道具箱は特別なものだった",
             "こわれたものは買いかえたほうが安い",
             "開けてみるという習慣が、ものとの付き合い方を変える",
             "直す技術を学ぶべきだ"], "ans": 2,
    "why": "最後に「入っていたのは、開けてみるという習慣のほうだった」と述べ、"
           "その習慣が「付き合い方」を変えるとしています。"},
 ]},
{
 "id": "t6", "tier": "N2", "kind": "情報検索", "title": "さつき温泉 ご利用案内",
 "body": "さつき温泉　ご利用案内\n"
         "■ご利用料金（下の表をご確認ください）\n"
         "■タオルについて\n"
         "大きいタオルは二百円で貸し出しています。小さいタオルは無料です。\n"
         "■回数券\n"
         "回数券は十一枚つづりで、大人十枚分の料金です。"
         "回数券は、どなたでもお使いいただけます。ただし、夜間料金にはお使いになれません。\n"
         "■夜間料金\n"
         "午後八時以降は、大人・子どもとも二百円引きになります。"
         "（三歳以下は、もともと無料です。）\n"
         "■お願い\n"
         "小学生以下の方だけでのご利用はできません。必ず大人とお越しください。",
 "table": {
   "head": ["", "平日", "土・日・祝日"],
   "rows": [["大人（中学生以上）", "八百円", "千円"],
            ["子ども（四歳〜小学生）", "四百円", "五百円"],
            ["三歳以下", "無料", "無料"]]},
 "en": "Satsuki Onsen — user guide\n"
       "■ Fees (see the table below)\n"
       "■ Towels\n"
       "Large towels are available to hire for 200 yen. Small towels are free.\n"
       "■ Multi-use tickets\n"
       "Eleven visits are sold for the price of ten adult admissions. Anyone may use them. "
       "However, they cannot be used against the evening rate.\n"
       "■ Evening rate\n"
       "From 8pm, both adults and children receive 200 yen off. (Children of three and under "
       "are free anyway.)\n"
       "■ Please note\n"
       "Those of primary school age and under may not use the baths on their own. Please always "
       "come with an adult.",
 "qs": [
   {"q": "日曜日の午後九時に、大人一人と六歳の子ども一人で行き、"
         "大人だけ大きいタオルを借りる場合、全部でいくらか。",
    "opts": ["千百円", "千三百円", "千五百円", "千七百円"], "ans": 1,
    "why": "日曜なので大人千円・子ども五百円。午後八時以降なので二人とも二百円引きで、"
           "八百円と三百円。大きいタオル二百円を足して千三百円です。"},
   {"q": "回数券について、正しいものはどれか。",
    "opts": ["子どもは使うことができない",
             "十一枚つづりを大人十枚分の料金で買える",
             "午後八時以降も使うことができる",
             "土・日・祝日には使えない"], "ans": 1,
    "why": "「十一枚つづりで、大人十枚分の料金」「どなたでも」使えますが、"
           "夜間料金には使えません。土日に使えないとは書かれていません。"},
 ]},
{
 "id": "t7", "tier": "N2", "kind": "内容理解（短文）", "title": "一つだけ決める",
 "body": "旅行の前に、行きたい場所をいくつも書き出すのが好きだった。"
         "地図に印をつけ、移動にかかる時間を調べ、朝から晩までの予定を組む。"
         "計画を立てている間がいちばん楽しい、とさえ思っていた。\n"
         "ところが実際に出かけてみると、予定を守ることに気を取られて、"
         "目の前の景色をほとんど見ていないことに気づいた。写真をとり、次の場所へ急ぐ。"
         "帰ってきて思い出せるのは、駅から駅への道ばかりだった。\n"
         "それ以来、行き先は一つだけ決めて、あとは決めないことにしている。"
         "残った時間に何をするかは、その日の気分と天気に任せる。"
         "予定の少ない旅のほうが、ふしぎと覚えていることは多い。",
 "en": "Before a trip I used to enjoy writing out all the places I wanted to go. I would mark "
       "a map, look up how long each journey took, and build a schedule from morning to night. "
       "I even thought the time spent planning was the best part.\n"
       "But when I actually set off, I found I was so taken up with keeping to the schedule "
       "that I was barely seeing the scenery in front of me. Take a photo, hurry to the next "
       "place. What I could recall afterwards was only the route from station to station.\n"
       "Since then I decide on one destination and leave the rest undecided. What to do with "
       "the time left over I leave to the mood and the weather of the day. Oddly enough, I "
       "remember more from the trips with less planned.",
 "qs": [
   {"q": "筆者は旅行についてどう考えるようになったか。",
    "opts": ["計画を立てている時間がいちばん楽しい",
             "写真を多くとったほうが思い出に残る",
             "行き先を一つだけ決め、あとは決めないほうがよい",
             "移動にかかる時間を正確に調べておくべきだ"], "ans": 2,
    "why": "「行き先は一つだけ決めて、あとは決めないことにしている」"
           "「予定の少ない旅のほうが…覚えていることは多い」とあります。"
           "1は以前の考えです。"},
   {"q": "以前の旅行で、筆者は何に気づいたか。",
    "opts": ["思ったより移動に時間がかかること",
             "予定に気を取られて景色を見ていないこと",
             "写真が思ったようにとれないこと",
             "一日で回れる場所は少ないこと"], "ans": 1,
    "why": "「予定を守ることに気を取られて、目の前の景色をほとんど見ていないことに気づいた」"
           "とあります。"},
 ]},
]
