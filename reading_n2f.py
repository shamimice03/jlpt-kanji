# -*- coding: utf-8 -*-
"""Batch 5: a second test-shaped N2 set. The article types and subject matter
follow the shapes used across the practice tests (問題10-14: 短文 x5, 中文,
統合理解, 長文, 情報検索); the text is original, and the kanji inventory of
those tests is the target. Written to work in the N5-N2 kanji from that
inventory that none of my earlier passages had used."""

PASSAGES = [
# ---------------- 問題10 style: 短文 ----------------
{
 "id": "v1", "tier": "N2", "kind": "内容理解（短文）", "title": "察するということ",
 "body": "「言わなくても察してほしい」と思うことは誰にでもある。"
         "しかし、他人の心の中は見えない。\n"
         "察するというのは、相手の様子から想像してみることであって、"
         "当てることではない。"
         "想像したら、念のため、言葉で確かめたほうがよい。\n"
         "確かめるのを恐れて何も言わずにいると、"
         "相手は「どうでもいいと思われている」と感じてしまう。",
 "en": "Everyone has wished at some point that the other person would understand without being "
       "told. But you cannot see inside another person's mind.\n"
       "To read someone is to imagine, from how they seem, what they may be feeling, not to "
       "guess it correctly. Once you have imagined it, it is better to check in words, just to "
       "be sure.\n"
       "If you are afraid to check and say nothing, the other person ends up feeling that they "
       "are not thought to matter.",
 "qs": [
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["察することは相手の気持ちを当てることである",
             "想像したことは言葉で確かめたほうがよい",
             "言わなくても分かり合えるのがよい関係である",
             "他人の心の中は想像しないほうがよい"], "ans": 1,
    "why": "「想像したら、念のため、言葉で確かめたほうがよい」とあります。"
           "察するのは「当てることではない」とも述べています。"},
 ]},
{
 "id": "v2", "tier": "N2", "kind": "内容理解（短文）", "title": "正面入り口 工事のお知らせ",
 "body": "十一月十日から二十日まで、一号館の正面入り口で工事を行います。\n"
         "期間中、正面入り口はお使いになれません。"
         "建物の北側にある入り口をご利用ください。"
         "駅の方から来られる場合は、本屋の角を左に曲がって、"
         "建物の周囲を回ってください。\n"
         "自転車置き場も、工事の間だけ南の広場へ移します。"
         "入り口の周辺には車を止められませんので、ご注意ください。",
 "en": "From the tenth to the twentieth of November, work will be carried out at the main "
       "entrance of Building 1.\n"
       "During that period the main entrance cannot be used. Please use the entrance on the "
       "north side of the building. If you are coming from the station, turn left at the corner "
       "by the bookshop and go round the building.\n"
       "The bicycle parking will also be moved to the square on the south side for the duration "
       "of the work. Please note that cars cannot be parked near the entrance.",
 "qs": [
   {"q": "工事の間、駅から一号館に入るにはどうすればよいか。",
    "opts": ["正面入り口から入る",
             "本屋の角を右に曲がり、南側の入り口から入る",
             "本屋の角を左に曲がり、北側の入り口から入る",
             "南の広場を通って正面入り口から入る"], "ans": 2,
    "why": "「本屋の角を左に曲がって、建物の周囲を回ってください」"
           "「建物の北側にある入り口をご利用ください」とあります。"
           "南の広場は自転車置き場です。"},
 ]},
{
 "id": "v3", "tier": "N2", "kind": "内容理解（短文）", "title": "はち植えの世話",
 "body": "はち植えの花をすぐにだめにしてしまう人は、水をやりすぎていることが多い。"
         "土の表面がかわいていても、はちの底の方はまだしめっている。"
         "指を少し入れてみて、冷たく感じるなら、その日はやらなくてよい。\n"
         "庭の野菜と同じように考えると失敗する。"
         "庭の土は広くつながっているが、はちの中の土はそれだけで閉じているからだ。\n"
         "緑の葉が元気をなくすのは、水が足りないときだけではない。"
         "根が熱を持って弱っていることもある。",
 "en": "People who quickly kill their potted flowers are usually watering them too much. Even "
       "when the surface of the soil is dry, the soil near the bottom of the pot is still damp. "
       "Put a finger in a little way, and if it feels cold, you can skip that day.\n"
       "You will go wrong if you think of it the way you think of vegetables in a garden. "
       "Garden soil is joined up over a wide area, whereas the soil in a pot is closed off by "
       "itself.\n"
       "Green leaves losing their vigour is not only a sign of too little water. Sometimes the "
       "roots have grown warm and weakened.",
 "qs": [
   {"q": "筆者によると、水をやらなくてよいのはどんなときか。",
    "opts": ["土の表面がかわいているとき",
             "はちの底の方の土が冷たく感じるとき",
             "緑の葉が元気をなくしているとき",
             "庭の野菜に水をやった日"], "ans": 1,
    "why": "「指を少し入れてみて、冷たく感じるなら、その日はやらなくてよい」とあります。"
           "表面がかわいていても底はしめっている、とも述べています。"},
 ]},
{
 "id": "v4", "tier": "N2", "kind": "内容理解（短文）", "title": "ご注文の前に",
 "body": "いつもお世話になっております。雑貨販売課の森田です。\n"
         "先日お話のありましたカップのご注文について、二点お願いがございます。"
         "一つめは、商品の資料をお送りいただきたいことです。"
         "大きさと重さが分かるものがあれば助かります。\n"
         "二つめは、包装についてです。"
         "箱に詰める際、一つずつ紙で包んでいただけますでしょうか。"
         "割れた場合の責任と、送るための費用については、こちらで持ちます。\n"
         "資料は、先日お渡しした名刺の住所へお送りください。",
 "en": "Thank you as always for your help. This is Morita, from the sundries sales section.\n"
       "Regarding the order of cups we discussed the other day, I have two requests. The first "
       "is that I would like you to send the product materials. Anything that shows the size "
       "and weight would help.\n"
       "The second concerns the packing. When you pack them in the box, could you wrap each one "
       "separately in paper? We will bear the responsibility, and the cost of sending, if any "
       "arrive broken.\n"
       "Please send the materials to the address on the business card I gave you the other day.",
 "qs": [
   {"q": "この人が相手に頼んでいることは何か。",
    "opts": ["資料を送り、商品を一つずつ紙で包むこと",
             "割れた商品の費用を払うこと",
             "カップの大きさと重さを変えること",
             "箱に詰めずに送ること"], "ans": 0,
    "why": "お願いは「商品の資料をお送りいただきたい」と「一つずつ紙で包んでいただけますか」"
           "の二点です。割れた場合の責任と費用は「こちらで持ちます」とあります。"},
 ]},
{
 "id": "v5", "tier": "N2", "kind": "内容理解（短文）", "title": "くもの冬",
 "body": "秋の終わりに、庭のすみで一匹のくもが白いふくろを作っていた。中には卵が入っている。\n"
         "くもはそのふくろを糸で木の枝にしっかり結びつけ、"
         "風にも落ちないようにしてから、どこかへ行ってしまった。"
         "親は冬を越さない。"
         "卵だけが、春まで寝ているように静かに保たれる。\n"
         "鳥の群れが庭に来ても、白いふくろは葉の色にまぎれて見つからない。"
         "守るための備えは、親がいなくなってからも働き続けるのだ。",
 "en": "At the end of autumn, in a corner of the garden, a single spider was making a white "
       "sack. Inside it are eggs.\n"
       "The spider tied the sack firmly to a branch with its silk so that not even the wind "
       "would bring it down, and then went off somewhere. The parent does not live through the "
       "winter. Only the eggs are kept quietly, as though asleep, until spring.\n"
       "Even when a flock of birds comes to the garden, the white sack is lost against the "
       "colour of the leaves and goes unfound. A preparation made in order to protect goes on "
       "working after the one who made it is gone.",
 "qs": [
   {"q": "筆者がこの文章で言いたいことは何か。",
    "opts": ["くもは春まで眠って冬を越す",
             "鳥はくもの卵を見つけるのがうまい",
             "親がいなくなっても、その備えは働き続ける",
             "くもは糸で木の枝を守っている"], "ans": 2,
    "why": "最後に「守るための備えは、親がいなくなってからも働き続ける」とあります。"
           "冬を越すのは卵だけで、親は越しません。"},
 ]},
# ---------------- 問題11 style: 中文 ----------------
{
 "id": "v6", "tier": "N2", "kind": "内容理解（中文）", "title": "上達が止まったとき",
 "body": "何かを練習していると、ある時期から急に上達が感じられなくなる。"
         "能力が落ちたわけではないのに、同じ所をぐるぐる回っているような状況になる。\n"
         "多くの人はここでやり方を変えたくなる。"
         "新しい教え方の本を買い、別の先生を探し、また最初の章から始める。"
         "しかし、変えたとたんに、それまで体にたまっていたものが、"
         "使われないまま終わってしまうことがある。\n"
         "私がすすめたいのは、やり方を変えるより先に、記録を取ることだ。"
         "今日できたことを一行だけ書く。"
         "それを一か月続けると、自分では気づかなかった程度の差が、紙の上に現れる。\n"
         "研究によれば、人は自分の進み方を実際より低く見るという。"
         "止まっていると感じるのは、進み方が小さくなって、"
         "意識に上がらなくなっただけのことが多い。"
         "記録は、その小さな進み方を目に見える形にして、次の準備につなげてくれる。",
 "en": "When you are practising something, there comes a point where you suddenly stop feeling "
       "any improvement. It is not that your ability has fallen, yet you end up in a state of "
       "going round and round the same spot.\n"
       "This is where most people want to change their method. They buy a book with a new way "
       "of teaching, look for a different teacher, and start again from the first chapter. But "
       "the moment you change, what had been accumulating in the body until then can end up "
       "never being used.\n"
       "What I would recommend is to keep a record before changing your method. Write just one "
       "line about what you managed today. Keep that up for a month, and a difference of degree "
       "you had not noticed yourself appears on the paper.\n"
       "Research says that people judge their own rate of progress to be lower than it is. "
       "Feeling that you have stopped is, more often than not, simply progress having grown "
       "small enough not to rise into awareness. A record puts that small progress into visible "
       "form, and joins it up with your next preparation.",
 "qs": [
   {"q": "筆者によると、上達が止まったと感じるのはなぜか。",
    "opts": ["能力が落ちたから",
             "進み方が小さくなって気づきにくくなったから",
             "やり方が自分に合っていないから",
             "練習の時間が足りないから"], "ans": 1,
    "why": "「進み方が小さくなって、意識に上がらなくなっただけのことが多い」とあります。"
           "「能力が落ちたわけではない」とも述べています。"},
   {"q": "筆者がすすめているのは何か。",
    "opts": ["新しい先生を探すこと",
             "最初の章からやり直すこと",
             "できたことを記録すること",
             "しばらく練習を休むこと"], "ans": 2,
    "why": "「やり方を変えるより先に、記録を取ることだ」とあります。"},
 ]},
{
 "id": "v7", "tier": "N2", "kind": "内容理解（中文）", "title": "休むことと体",
 "body": "休むというのは、何もしないことだと思われがちだ。"
         "しかし、一日じゅう横になっていた日の夕方に、かえって体が重いことがある。\n"
         "これは、脳が働きをやめていないからだという。"
         "人の脳は、外から入ってくるものが少なすぎても、落ち着かなくなるらしい。"
         "腕や足を少し動かし、軽い用事をいくつか片付けた日の方が、夜よく寝られる。\n"
         "年齢が上がるほど、この差は大きくなる。"
         "骨やきん肉は使わないとすぐに弱り、"
         "弱ると動くのがつらくなって、さらに使わなくなる。\n"
         "完全に止まるのではなく、普段の半分の速さで動く日を作る。"
         "それが、私の考える休みの日である。",
 "en": "Resting tends to be thought of as doing nothing. But there are days when you have lain "
       "down all day and by evening your body feels heavier instead.\n"
       "This is said to be because the brain has not stopped working. It seems that if too "
       "little comes in from outside, the human brain becomes unsettled. You sleep better at "
       "night after a day of moving your arms and legs a little and getting a few light errands "
       "out of the way.\n"
       "The older you get, the larger this difference becomes. Bones and muscles weaken quickly "
       "when they are not used, and once they weaken, moving becomes hard, so they are used "
       "even less.\n"
       "Rather than stopping completely, make a day on which you move at half your usual speed. "
       "That is what a day of rest means to me.",
 "qs": [
   {"q": "一日じゅう横になっていた日の夕方に体が重いのは、なぜだと言っているか。",
    "opts": ["骨やきん肉が弱ったから",
             "脳が働きをやめていないから",
             "寝る時間が長すぎたから",
             "年齢が上がったから"], "ans": 1,
    "why": "「これは、脳が働きをやめていないからだという」とあります。"},
   {"q": "筆者の考える休みの日とは、どんな日か。",
    "opts": ["何もしないで横になっている日",
             "普段の半分の速さで動く日",
             "普段より多く用事を片付ける日",
             "外に出ないで過ごす日"], "ans": 1,
    "why": "「完全に止まるのではなく、普段の半分の速さで動く日を作る。"
           "それが、私の考える休みの日である」とあります。"},
 ]},
{
 "id": "v8", "tier": "N2", "kind": "内容理解（中文）", "title": "持ち物の数",
 "body": "自宅の居間を片付けていて、同じような布の袋が六つも出てきた。"
         "どれもいつか使うつもりで取っておいたものだ。"
         "だが、六つあることを私は完全に忘れていた。\n"
         "覚えていない持ち物は、持っていないのと変わらない。"
         "人が頭の中で管理できる物の数には限りがある。"
         "その数を超えた分は、家の中に在るだけで、存在していないのと同じになる。\n"
         "退職した父が、衣服を半分に減らしたときに言っていた。"
         "父は服装に気を使う人だったから、これは意外だった。"
         "「少なくすると、一つ一つが宝のように思えてくる。」\n"
         "荷物を減らすのは、がまんすることではなく、"
         "残した物を見えるようにすることなのだろう。"
         "帯や服を箱の底にしまい込んだままにしておくより、"
         "少ない数を毎日使う方が、ずっと楽しい。",
 "en": "Tidying the living room at home, I turned up as many as six cloth bags of much the same "
       "kind. Every one had been kept on the grounds that I would use it one day. But I had "
       "completely forgotten that there were six.\n"
       "A possession you do not remember is no different from one you do not own. There is a "
       "limit to the number of things a person can keep track of in their head. Whatever goes "
       "beyond that number merely exists in the house, which amounts to not existing at all.\n"
       "My father, after he retired, said something when he cut his clothes by half. He had "
       "always been a man who cared about how he dressed, so this surprised me. \"When you have "
       "fewer, each one starts to seem like a treasure.\"\n"
       "Reducing your belongings is probably not a matter of going without, but of making what "
       "you keep visible. Using a small number of things every day is far more enjoyable than "
       "leaving sashes and clothes stowed at the bottom of a box.",
 "qs": [
   {"q": "「覚えていない持ち物は、持っていないのと変わらない」とあるが、なぜか。",
    "opts": ["頭の中で管理できる数を超えた物は、在るだけで存在していないのと同じだから",
             "古い物はいつか使えなくなるから",
             "持ち物はできるだけ減らすべきだから",
             "持ち物の数を覚えておく必要はないから"], "ans": 0,
    "why": "「その数を超えた分は、家の中に在るだけで、存在していないのと同じになる」"
           "と続けて述べています。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["がまんして物を減らすべきだ",
             "物を減らすのは、残した物を見えるようにすることだ",
             "布の袋は六つあれば足りる",
             "衣服は箱の底にしまっておくのがよい"], "ans": 1,
    "why": "「がまんすることではなく、残した物を見えるようにすることなのだろう」とあります。"},
 ]},
# ---------------- 問題12 style: 統合理解 ----------------
{
 "id": "v9", "tier": "N2", "kind": "統合理解", "title": "間違いを直すとき",
 "body": "Ａ\n"
         "生徒が間違えたとき、私はその場で直す。"
         "間違えたまま先へ進むと、間違いが形になって残ってしまうからだ。"
         "ただし、直すのは答えだけにする。"
         "その人の考え方を否定するような言い方はしない。"
         "打ち消すのではなく、半分だけ折って向きを変える、という感じである。\n"
         "Ｂ\n"
         "間違いに気づいても、私は最後まで言わせる。"
         "途中で止めると、本人がどこで折れたのかが分からなくなる。"
         "全部聞いてから、「ここまでは合っている」と言って、合っている所を先に示す。"
         "すると、生徒は自分で間違いを見つけることが多い。"
         "自分で見つけたときの方が、後の成長が早い。"
         "やる気が散ってしまうのが、一番こわいのだ。",
 "en": "A. When a student makes a mistake, I correct it on the spot. If they go on with the "
       "mistake uncorrected, it takes shape and stays. I confine the correction to the answer, "
       "though. I avoid any wording that denies the person's way of thinking. It is less like "
       "cancelling something out than like bending it halfway to change its direction.\n"
       "B. Even when I notice a mistake, I let the student finish. Stop them partway and you "
       "lose track of where they went off. After hearing it all, I say \"this far is right,\" "
       "showing the correct part first. The student then often finds the mistake themselves. "
       "Growth afterwards is faster when they have found it themselves. What I fear most is "
       "their motivation being scattered.",
 "qs": [
   {"q": "ＡとＢが共通して述べていることは何か。",
    "opts": ["間違いはその場で直すべきだ",
             "生徒の考え方や気持ちをそこなわないようにしている",
             "間違いは最後まで言わせてから直すべきだ",
             "生徒は自分では間違いを見つけられない"], "ans": 1,
    "why": "Ａは「考え方を否定するような言い方はしない」、"
           "Ｂは「やる気が散ってしまうのが、一番こわい」と述べています。"
           "直す時期については二人の意見が違います。"},
   {"q": "間違いを直す時期について、ＡとＢはどう違うか。",
    "opts": ["Ａはその場で直し、Ｂは最後まで聞いてから直す",
             "ＡもＢも最後まで聞いてから直す",
             "Ａは直さず、Ｂはその場で直す",
             "Ａは答えだけを直し、Ｂは考え方を直す"], "ans": 0,
    "why": "Ａは「その場で直す」、Ｂは「最後まで言わせる」「全部聞いてから」とあります。"},
 ]},
# ---------------- 問題13 style: 長文 ----------------
{
 "id": "v10", "tier": "N2", "kind": "主張理解（長文）", "title": "古い町を歩く",
 "body": "昨年の秋、電車の線路が終わる所にある小さな村を歩いた。"
         "友人が著者として名前を出している本に、その村のことが紹介されていたからだ。\n"
         "駅を出ると、すぐに田と林が広がり、遠くに森と山が見えた。"
         "道は川に向かって下っていて、途中に古い木の橋がかかっている。"
         "橋の板は白くなるまでかわいていて、歩くと低い音がした。"
         "村の中心には寺があり、その横に小さなお堂が立っていた。"
         "お堂の前には、和紙で作った花が置かれていた。\n"
         "私がおどろいたのは、建物の古さではない。"
         "古い形を残すやり方が、どこも同じ形式ではなかったことだ。"
         "ある家は、昔のままのかべをそのまま使っている。"
         "別の家は、新しい材料で昔と同じ形を作り直している。"
         "さらに別の家は、外から見える側だけ昔のままにして、"
         "中は今の暮らしに合わせて変えている。\n"
         "どれが正しいという話ではない、と村の人は言った。"
         "「残すというのは、写真に映すことじゃないんです。」"
         "「住んでいる人がいなくなったら、形だけ残っても意味がないでしょう。」"
         "言われてみれば、そのとおりだった。"
         "古い町が美しく見えるのは、そこに人の生活が続いているからで、"
         "昔の形そのものが美しいわけではない。\n"
         "村を出る時、橋の上から水を見ると、落ちた葉が流れていた。"
         "この橋も、いつか新しくなるのだろう。"
         "それでも、この村が村であり続けるなら、"
         "それは残ったことになるのだと思った。",
 "en": "Last autumn I walked around a small village at the end of a railway line. It was "
       "because the village had been described in a book my friend's name appears on as "
       "author.\n"
       "Coming out of the station, fields and a wood opened out at once, with forest and "
       "mountains in the distance. The road ran down towards the river, with an old wooden "
       "bridge partway along. The planks of the bridge had dried until they were white, and "
       "they gave a low sound as I walked. At the centre of the village stood a temple, and "
       "beside it a small shrine hall. In front of the hall lay flowers made of Japanese "
       "paper.\n"
       "What surprised me was not how old the buildings were. It was that the way of keeping "
       "the old form was not the same formula everywhere. One house uses its original walls as "
       "they are. Another has rebuilt the same form out of new materials. Yet another has left "
       "only the side visible from outside as it was, and changed the inside to suit life "
       "today.\n"
       "It is not a question of which is right, a villager told me. \"Keeping something is not "
       "the same as capturing it in a photograph.\" \"Once the people living here are gone, "
       "what good is the form on its own?\" Put like that, he was right. An old town looks "
       "beautiful because life carries on in it, not because the old form is beautiful in "
       "itself.\n"
       "As I left the village, looking down at the water from the bridge, fallen leaves were "
       "drifting past. This bridge too will be made new one day. Even so, I thought, if this "
       "village goes on being a village, that will count as having kept it.",
 "qs": [
   {"q": "筆者がおどろいたのは何か。",
    "opts": ["建物がとても古かったこと",
             "古い形を残すやり方が家ごとに違っていたこと",
             "村に住んでいる人がいなかったこと",
             "寺とお堂が並んで立っていたこと"], "ans": 1,
    "why": "「おどろいたのは、建物の古さではない。"
           "古い形を残すやり方が、どこも同じ形式ではなかったことだ」とあります。"},
   {"q": "村の人の言葉から分かる考えはどれか。",
    "opts": ["古い形は写真に残しておくべきだ",
             "住む人がいなければ、形だけ残っても意味がない",
             "新しい材料を使うのはよくない",
             "外から見える側だけ残せばよい"], "ans": 1,
    "why": "「住んでいる人がいなくなったら、形だけ残っても意味がないでしょう」とあります。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["昔の形そのものが美しい",
             "橋は新しくしない方がよい",
             "人の生活が続いていることが、古い町を美しく見せる",
             "村は変わらない方がよい"], "ans": 2,
    "why": "「古い町が美しく見えるのは、そこに人の生活が続いているからで、"
           "昔の形そのものが美しいわけではない」とあります。"},
 ]},
{
 "id": "v11", "tier": "N2", "kind": "主張理解（長文）", "title": "話を聞くということ",
 "body": "人の悩みを聞くのは難しい。"
         "こちらが何かを与えなければならないような気がしてくるからだ。"
         "答えを一つも出せないまま終わると、役に立たなかったように感じる。"
         "しかし、相手が求めているのは答えではないことの方が多い。\n"
         "友人が仕事のことで苦しんでいた時、私は三つほど考えを出した。"
         "どれも悪くなかったと思う。"
         "だが、友人の顔は晴れなかった。"
         "後で聞くと、「自分でも分かっていることを並べられると、よけいにつらい」"
         "と言われた。"
         "そのとき私がしたのは、相手の世界に入ることではなく、"
         "自分の考えを紹介することだった。\n"
         "人を助けようとする時、私たちはつい間に何かを置いてしまう。"
         "本や人から借りた言葉を間に介して話すと、安全ではあるが、相手には届かない。"
         "相談を依頼された時こそ、急いで答えを出さない方がいい。\n"
         "誰かの話を聞くというのは、答えを用意しておくことではなく、"
         "答えがない時間を一緒に過ごす備えをしておくことなのだろう。"
         "言葉を交わさない時間を保てるかどうかで、聞く力は決まるのかもしれない。"
         "何も言わずにいることができず、すぐに「それなら」と言い出してしまうのは、"
         "相手のためではなく、自分が落ち着かないからだ。"
         "それが可能になるのは、相手を変えようとしない時だけだと思う。\n"
         "子供のころ、泣いている私の横に、何も言わずに座っていてくれた人がいた。"
         "他人の時間をそのまま受け取るのは、こわいことでもある。"
         "それでも、そうしてもらえた経験のある人は、きっと覚えているはずだ。"
         "何も解決していないのに、帰り道が少し軽く感じられたことを。",
 "en": "Listening to someone's troubles is difficult. It is because you start to feel you have "
       "to give them something. Finish without having produced a single answer and you feel you "
       "were no use. But what the other person wants is, more often than not, not an answer.\n"
       "When a friend was suffering over work, I offered three or so ideas. None of them was "
       "bad, I think. But my friend's face did not clear. Asking later, I was told, \"Having "
       "things I already know lined up for me only makes it harder.\" What I had done then was "
       "not to enter her world but to introduce my own thinking.\n"
       "When we try to help someone, we tend to put something in between. Speaking through "
       "words borrowed from books or other people is safe, but it does not reach the other "
       "person. It is precisely when you are asked for advice that you should not hurry to an "
       "answer.\n"
       "Listening to someone is probably not a matter of having an answer ready, but of being "
       "ready to spend a stretch of time together in which there is no answer. Perhaps the "
       "power to listen is decided by whether you can hold a stretch of time without exchanging "
       "words. Being unable to stay silent and blurting out \"in that case\" is not for the "
       "other person's sake but because you yourself are uneasy. That becomes possible, I "
       "think, only when you are not trying to change the other person.\n"
       "When I was a child, there was someone who sat beside me while I cried and said nothing. "
       "Taking another person's time just as it is can be frightening. Even so, anyone who has "
       "had that done for them is sure to remember it. That although nothing had been solved, "
       "the walk home felt a little lighter.",
 "qs": [
   {"q": "友人の顔が晴れなかったのはなぜか。",
    "opts": ["筆者の考えがどれも悪かったから",
             "自分でも分かっていることを並べられたから",
             "筆者が何も言わなかったから",
             "仕事の悩みが解決しなかったから"], "ans": 1,
    "why": "「自分でも分かっていることを並べられると、よけいにつらい」と"
           "友人が後で言っています。"},
   {"q": "「間に何かを置いてしまう」とは、どういうことか。",
    "opts": ["相手との間に時間を置くこと",
             "本や人から借りた言葉を通して話すこと",
             "相手の世界に入っていくこと",
             "答えを出すのを急がないこと"], "ans": 1,
    "why": "次の文に「本や人から借りた言葉を間に介して話すと、安全ではあるが、"
           "相手には届かない」とあります。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["聞く人は答えを用意しておくべきだ",
             "答えがない時間を一緒に過ごす備えが大切だ",
             "すぐに考えを出してあげるのが親切だ",
             "人の悩みは聞かない方がよい"], "ans": 1,
    "why": "「答えがない時間を一緒に過ごす備えをしておくことなのだろう」とあります。"},
 ]},
# ---------------- 問題14 style: 情報検索 ----------------
{
 "id": "v12", "tier": "N2", "kind": "情報検索", "title": "みどり公園 貸し自転車のご案内",
 "body": "みどり公園では、園内と周辺の道路を走れる貸し自転車をご用意しています。"
         "受付は南口の案内所で、営業時間は午前九時から午後五時までです。"
         "返す時刻が午後五時を過ぎた場合は、規則により追加の料金をいただきます。\n"
         "遠くまで行かれる方には、軽い車体の二号車が適しています。"
         "二号車は数が少ないため、前の日までのお申し込みが可能です。"
         "小学生以下は専用の子供用のみで、大人の方とご一緒にご参加ください。\n"
         "雨の日は、園内に設けた屋根の下の道だけ走れます。"
         "一度返したあとで再び借りる場合も、同じ料金がかかります。"
         "こわれた時の処理については、案内所にお申し出ください。\n"
         "なお、園内の草取りを手伝ってくださる方を募っています。"
         "お手伝いいただいた方は、その日の料金が無料になります。"
         "ご苦労をおかけしますが、ご協力をお願いします。"
         "公園の駐車場は有料です。",
 "table": {"head": ["車の種類", "一時間", "一日", "そのほか"],
           "rows": [["一号車（ふつう）", "三百円", "千円", "数に限りあり"],
                    ["二号車（軽い車体）", "四百円", "千四百円", "前日までの申し込み可"],
                    ["子供用", "二百円", "六百円", "大人とご一緒に"]]},
 "en": "At Midori Park we have rental bicycles that can be ridden inside the park and on the "
       "surrounding roads. The desk is at the information office by the south gate, open from "
       "nine in the morning until five in the afternoon. If the time you return it is later "
       "than five in the afternoon, the rules require us to charge an additional fee.\n"
       "For those going a long way, the number 2 bicycle, with its light frame, is suitable. "
       "Because there are few number 2 bicycles, applications are accepted up to the day "
       "before. Primary school children and younger may use only the dedicated children's "
       "bicycles, and must take part together with an adult.\n"
       "On rainy days, only the paths under the roof built inside the park can be ridden. The "
       "same fee applies when you borrow again after returning once. For how breakages are "
       "handled, please speak to the information office.\n"
       "We are also looking for people to help with weeding inside the park. Anyone who helps "
       "has their fee for that day waived. We are sorry for the trouble, and ask for your "
       "cooperation. The park car park is paid.",
 "qs": [
   {"q": "二号車について、正しいものはどれか。",
    "opts": ["一日借りると千円かかる",
             "車体が軽く、前の日までに申し込める",
             "小学生以下でも一人で借りられる",
             "雨の日は借りられない"], "ans": 1,
    "why": "「遠くまで行かれる方には、軽い車体の二号車が適しています」"
           "「前の日までのお申し込みが可能です」とあります。一日は千四百円です。"},
   {"q": "料金がかからないのは、どんな場合か。",
    "opts": ["一度返したあとで再び借りた場合",
             "午後五時を過ぎて返した場合",
             "園内の草取りを手伝った日",
             "子供用を大人と一緒に借りた場合"], "ans": 2,
    "why": "「お手伝いいただいた方は、その日の料金が無料になります」とあります。"
           "再び借りる場合は「同じ料金がかかります」とあります。"},
 ]},
# ---------------- extra 短文 ----------------
{
 "id": "v13", "tier": "N2", "kind": "内容理解（短文）", "title": "写真コンクールのお知らせ",
 "body": "今年のコンクールの題は「光」です。\n"
         "朝日が昇るところでも、台所の窓に映る夕方の光でもかまいません。"
         "人の作った光を使った作品も受け付けます。\n"
         "賞は三つで、選ばれた作品は会館の一階に並べます。"
         "お一人二点までお出しいただけます。",
 "en": "The subject of this year's competition is \"light.\"\n"
       "The sun coming up is fine, and so is evening light reflected in a kitchen window. Works "
       "using light that people have made are also accepted.\n"
       "There are three prizes, and the chosen works will be displayed on the ground floor of "
       "the hall. Each person may submit up to two works.",
 "qs": [
   {"q": "このコンクールに出せる作品はどれか。",
    "opts": ["夕方の台所を写した、光の入っていない写真",
             "店の明かりを写した写真",
             "去年の賞に選ばれた作品",
             "一人で三点出した作品"], "ans": 1,
    "why": "「人の作った光を使った作品も受け付けます」とあります。"
           "出せるのは一人二点までです。"},
 ]},
{
 "id": "v14", "tier": "N2", "kind": "内容理解（中文）", "title": "川のそばに住む",
 "body": "私の育った町は、大きな川のすぐそばにあった。"
         "水は町の暮らしを支えていたが、同じ水が町をこわすこともあった。\n"
         "子供のころ、台風のあとで水が道まで上がってきたことがある。"
         "青いバケツが道の上を浮いて流れていくのを、二階の窓から見ていた。"
         "その後、町は川のきしに高いかべを築いた。水を防ぐためである。"
         "おかげで、突然の雨でも水が上がってくることはなくなった。\n"
         "けれども、かべができてから、川は町から見えなくなった。"
         "風の音は聞こえるのに、水の面が見えない。"
         "風の強い日に立つ小さな波も、もう見えない。"
         "銀色に光る水の面を、私たちは失ったことになる。\n"
         "今は、かべの上に細い遊歩道が作られ、歩きながら川が見えるようになっている。"
         "管理する人の話では、これを作るかどうかで長く話し合ったそうだ。"
         "夕方には、遊歩道で近所の人が和やかに話している。"
         "安全か、水の見える暮らしか。"
         "どちらかを選ぶ話にしてしまうと、答えは出ない。"
         "両方を少しずつ満たす形を探すほうが、世界のどこでもうまくいっているように思う。\n"
         "川の水は今も飲めない。"
         "それでも、水の見える町であることは、私には大事なことだ。",
 "en": "The town I grew up in was right beside a large river. The water supported the life of "
       "the town, but the same water sometimes wrecked it.\n"
       "When I was a child, the water once rose as far as the road after a typhoon. I watched "
       "from a second-floor window as a blue bucket floated away along the road. After that, "
       "the town built a high wall along the river. It was in order to keep the water out. "
       "Thanks to it, the water no longer rises even in sudden rain.\n"
       "But since the wall went up, the river cannot be seen from the town. You can hear the "
       "sound of the wind, yet the surface of the water is not visible. The small waves that "
       "rise on a windy day can no longer be seen either. We have lost the "
       "surface of the water shining silver.\n"
       "Now a narrow walkway has been built on top of the wall, so that you can see the river "
       "as you walk. According to the person who manages it, there was a long discussion over "
       "whether to build it. In the evenings, people from the neighbourhood talk amiably on the "
       "walkway. Safety, or a life with the water in view. Make it a matter of choosing one of "
       "the two and no answer comes. Looking for a form that satisfies both a little seems to "
       "work better, anywhere in the world.\n"
       "The river water still cannot be drunk. Even so, being a town with the water in view "
       "matters to me.",
 "qs": [
   {"q": "高いかべを築いた結果、どうなったか。",
    "opts": ["水が上がってこなくなったが、川が見えなくなった",
             "水が上がってくるのを防げなくなった",
             "風の音が聞こえなくなった",
             "川の水が飲めるようになった"], "ans": 0,
    "why": "「突然の雨でも水が上がってくることはなくなった」"
           "「壁ができてから、川は町から見えなくなった」とあります。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["安全の方が水の見える暮らしより大事だ",
             "かべは作らない方がよかった",
             "どちらかを選ぶのではなく、両方を少しずつ満たす形を探す方がよい",
             "遊歩道は必要なかった"], "ans": 2,
    "why": "「どちらかを選ぶ話にしてしまうと、答えは出ない。"
           "両方を少しずつ満たす形を探すほうが…うまくいっている」とあります。"},
 ]},
]
