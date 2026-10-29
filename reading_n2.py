# -*- coding: utf-8 -*-
"""N2 passages across all five 読解 formats. Checked by reading_check.py:
every kanji must be in the N2-or-below set."""

PASSAGES = [
{
 "id": "n1", "tier": "N2", "kind": "内容理解（短文）", "title": "社内のお知らせ",
 "body": "社員のみなさんへ\n"
         "来月から、会議室の使い方が変わります。これまでは当日に空いている部屋を自由に"
         "使えましたが、今後は前日までに申し込みが必要になります。\n"
         "申し込みは社内の画面から行ってください。急な用事で当日に使いたい場合は、"
         "総務部に直接連絡してください。空いていれば使えますが、"
         "前日までに申し込んだ人が優先されます。",
 "en": "To all staff. From next month the way meeting rooms are used will change. Until now "
       "you could freely use any room that was free on the day, but from now on an application "
       "must be made by the day before. Apply through the internal screen. If something urgent "
       "comes up and you want a room on the day itself, contact the General Affairs "
       "department directly. You may use a room if one is free, but people who applied by the "
       "previous day take priority.",
 "qs": [
   {"q": "当日に急に会議室を使いたくなったとき、どうすればよいか。",
    "opts": ["画面から申し込んで、空くのを待つ",
             "総務部に連絡し、空いていれば使う",
             "前日に申し込んだ人に代わってもらう",
             "会議室を使わずに別の場所を探す"], "ans": 1,
    "why": "「急な用事で当日に使いたい場合は、総務部に直接連絡してください。空いていれば使えます」"
           "とあります。"},
 ]},
{
 "id": "n2", "tier": "N2", "kind": "内容理解（短文）", "title": "道具と腕前",
 "body": "新しい道具を買えば上手になれると考える人は多い。しかし、実際に上達する人を見ていると、"
         "道具を変えたから伸びたのではなく、同じ道具を長く使って、"
         "そのくせを知りつくしているように思う。\n"
         "もちろん、体に合わない道具を無理に使い続ける必要はない。"
         "ただ、うまくいかない原因をいつも道具のせいにしていると、"
         "自分のどこを直せばよいのかが、いつまでも見えてこない。",
 "en": "Many people think that buying new equipment will make them better. But watching people "
       "who actually improve, it seems they did not get better because they changed equipment "
       "— rather, they used the same tools for a long time and came to know their quirks "
       "inside out. Of course there is no need to force yourself to keep using equipment that "
       "does not suit you. But if you always blame your tools when things go badly, you will "
       "never come to see what it is in yourself that needs fixing.",
 "qs": [
   {"q": "筆者が言いたいことは何か。",
    "opts": ["よい道具を選ぶことが上達の近道だ",
             "体に合わない道具は使わないほうがよい",
             "道具のせいにしていると自分の問題が見えない",
             "同じ道具を長く使えば必ず上手になる"], "ans": 2,
    "why": "最後に「いつも道具のせいにしていると、自分のどこを直せばよいのかが、いつまでも"
           "見えてこない」と述べています。4は「必ず」が言いすぎです。"},
 ]},
{
 "id": "n3", "tier": "N2", "kind": "内容理解（中文）", "title": "言葉は変わる",
 "body": "若い人の言葉づかいが乱れていると言われることがある。新しい言い方を聞くたびに、"
         "正しい日本語が失われていくと心配する人も少なくない。\n"
         "しかし、言葉は昔から変わり続けてきた。今では正しいとされている表現の中にも、"
         "かつては誤りだとされたものが数多くある。①そう考えると、"
         "今の変化だけを特別に問題だと考えるのは公平ではないだろう。\n"
         "とはいえ、どんな変化も認めればよいというわけでもない。"
         "言葉の役割は、相手に自分の考えを正確に伝えることである。"
         "仲間うちでしか通じない言い方を、初めて会った人や目上の人に向かって使えば、"
         "伝わらないばかりか、相手を不快にさせることもある。\n"
         "大切なのは、変化を止めることではなく、相手と場面に合わせて使い分ける力を"
         "身につけることではないだろうか。",
 "en": "People sometimes say that young people's language is deteriorating. Each time they "
       "hear a new expression, many worry that correct Japanese is being lost. But language "
       "has always been changing. Among expressions now regarded as correct there are many "
       "that were once criticised as errors. Seen that way, it is hardly fair to treat only "
       "today's changes as a special problem. That said, it does not follow that every change "
       "should be accepted. The role of language is to convey your thoughts to the other "
       "person accurately. If you use wording that only works among friends with someone you "
       "have just met, or with a senior, it may not only fail to get through but leave them "
       "uncomfortable. What matters, surely, is not stopping change but acquiring the ability "
       "to use language differently according to the person and the situation.",
 "qs": [
   {"q": "①そう考えると とあるが、どう考えるのか。",
    "opts": ["若い人の言葉づかいは乱れているということ",
             "正しい日本語が失われつつあるということ",
             "今正しいとされる表現も昔は誤りとされたということ",
             "新しい言い方は仲間うちでしか通じないということ"], "ans": 2,
    "why": "直前の「今では正しいとされている表現の中にも、かつては誤りだとされたものが"
           "数多くある」を指しています。"},
   {"q": "筆者は、どんな言い方が問題だと述べているか。",
    "opts": ["新しく生まれた言い方そのもの",
             "場面に合わない相手に向けて使う言い方",
             "昔から使われてきた古い言い方",
             "目上の人だけが使う難しい言い方"], "ans": 1,
    "why": "「仲間うちでしか通じない言い方を、初めて会った人や目上の人に向かって使えば」"
           "問題になると述べています。言い方そのものを否定してはいません。"},
   {"q": "筆者の考えに最も近いものはどれか。",
    "opts": ["言葉の変化は止めなければならない",
             "どんな変化も受け入れるべきだ",
             "相手と場面によって使い分ける力が必要だ",
             "正しい日本語を学校で教え直すべきだ"], "ans": 2,
    "why": "最後の段落で「相手と場面に合わせて使い分ける力を身につけること」が大切だと"
           "述べています。"},
 ]},
{
 "id": "n4", "tier": "N2", "kind": "内容理解（中文）", "title": "待つ時間",
 "body": "注文したものが翌日に届くのが当たり前になった。早く届くのはありがたいが、"
         "そのせいで失われたものもあるように思う。\n"
         "子どものころ、父に本を頼むと、届くまでに二週間ほどかかった。"
         "その間、わたしは何度も表紙を想像した。どんな絵がかかれているのか、"
         "どんな手ざわりなのか。実際に届いたときの喜びは、"
         "想像していた時間の長さに支えられていたように思う。\n"
         "②今はどうだろう。注文した翌日には箱が届き、開けて、確かめて、"
         "それで終わってしまう。手に入るまでの時間がないぶん、"
         "手に入れたあとの気持ちも、どこか薄い。\n"
         "便利さを手放すつもりはない。ただ、何でもすぐに手に入る生活の中で、"
         "待つことがくれていた豊かさを、わたしたちは少しずつ忘れているのかもしれない。",
 "en": "It has become normal for what you order to arrive the next day. Fast delivery is "
       "welcome, but it seems to me something has been lost because of it. As a child, when I "
       "asked my father for a book it took about two weeks to arrive. During that time I "
       "imagined the cover over and over — what picture was on it, how it would feel in my "
       "hands. The joy when it actually arrived was, I think, held up by the length of time I "
       "had spent imagining. And now? The box arrives the day after you order, you open it, "
       "check it, and that is that. With no time before getting it, the feeling after getting "
       "it is somehow thinner too. I have no intention of giving up convenience. But in a life "
       "where anything can be had at once, we may be slowly forgetting the richness that "
       "waiting used to give us.",
 "qs": [
   {"q": "子どものころの喜びについて、筆者はどう考えているか。",
    "opts": ["本の内容がすばらしかったから生まれた",
             "待つ間に想像した時間が支えていた",
             "父が買ってくれたことがうれしかった",
             "二週間も待たされて腹が立っていた"], "ans": 1,
    "why": "「実際に届いたときの喜びは、想像していた時間の長さに支えられていた」とあります。"},
   {"q": "②今はどうだろう とあるが、今について筆者はどう述べているか。",
    "opts": ["品物の質が昔より落ちている",
             "届くのが遅くて困ることが多い",
             "手に入れたあとの気持ちが薄い",
             "想像する楽しみが増えている"], "ans": 2,
    "why": "「手に入れたあとの気持ちも、どこか薄い」と述べています。"},
   {"q": "筆者の考えに合うものはどれか。",
    "opts": ["便利な生活はやめたほうがよい",
             "早く届くのはよくないことだ",
             "待つことの豊かさを忘れかけている",
             "昔の生活のほうがすべてよかった"], "ans": 2,
    "why": "「便利さを手放すつもりはない」としたうえで、「待つことがくれていた豊かさを"
           "忘れている」と述べています。1・4は否定が強すぎます。"},
 ]},
{
 "id": "n5", "tier": "N2", "kind": "統合理解", "title": "子どもにけいたい電話を持たせるか",
 "body": "Ａ\n"
         "小学生にけいたい電話を持たせることに反対する声は根強い。確かに、"
         "長時間使えば勉強の時間が減るし、知らない相手とつながる危険もある。"
         "しかし、だからといって持たせないという判断が、子どもを守ることになるだろうか。"
         "危険があるからこそ、親が見ていられるうちに、使い方を一緒に学ぶべきだと思う。"
         "家を出てから困ったときに連絡が取れるという安心も小さくない。\n"
         "Ｂ\n"
         "けいたい電話は便利な道具だが、小学生にはまだ早い。"
         "使い方を教えればよいという意見もあるが、"
         "大人でさえ使う時間を自分で決められずにいるのが現実である。"
         "判断する力が十分に育っていない時期に持たせれば、"
         "友人との関係の中で、断れないまま夜まで続けてしまうことになりやすい。"
         "連絡の手段が必要なら、電話だけができる簡単な機械で足りるのではないか。",
 "en": "A. Opposition to giving primary-school children mobile phones runs deep. Certainly, "
       "long hours of use cut into study time, and there is the danger of connecting with "
       "strangers. But does deciding not to give them one really protect the child? Precisely "
       "because there are dangers, I think parents should learn how to use it together with "
       "the child while they can still watch over them. The reassurance of being able to make "
       "contact when something goes wrong after leaving the house is no small thing.\n"
       "B. A mobile phone is a useful tool, but it is too early for primary-school children. "
       "Some say you need only teach them how to use it, but the reality is that even adults "
       "cannot decide their own screen time. Give one to a child whose judgement has not yet "
       "matured, and within the pressures of friendship they will easily end up unable to "
       "refuse, carrying on late into the night. If a means of contact is needed, surely a "
       "simple device that only makes calls would be enough.",
 "qs": [
   {"q": "ＡとＢが共通して認めていることは何か。",
    "opts": ["小学生にはけいたい電話がまだ早いということ",
             "けいたい電話の使い方は親が教えるべきだということ",
             "けいたい電話には危険な面があるということ",
             "連絡の手段として簡単な機械で足りるということ"], "ans": 2,
    "why": "Ａは「知らない相手とつながる危険」、Ｂは「夜まで続けてしまう」ことを挙げ、"
           "どちらも危険な面を認めています。1はＢのみ、4もＢのみの意見です。"},
   {"q": "ＡとＢの意見の違いはどこにあるか。",
    "opts": ["危険があるかどうかについて",
             "危険があるとき、持たせて教えるか、持たせないかについて",
             "勉強の時間が減るかどうかについて",
             "親が子どもを見ているべきかどうかについて"], "ans": 1,
    "why": "Ａは「危険があるからこそ…一緒に学ぶべき」、Ｂは「判断する力が育っていない時期に"
           "持たせれば」よくないとしており、危険への対応が分かれています。"},
 ]},
{
 "id": "n6", "tier": "N2", "kind": "主張理解（長文）", "title": "教わらない力",
 "body": "新人の指導を任されたとき、わたしは何でもていねいに教えようとした。"
         "手順を細かく書いた紙を用意し、分からないことがあればいつでも聞きにくるように伝えた。"
         "新人はすなおによく聞き、一つずつ正確にこなしていった。"
         "最初の数か月は、うまくいっているように見えた。\n"
         "ところが半年ほどたったころ、気になることが出てきた。"
         "紙に書いていない場面になると、手が止まってしまうのである。"
         "少し考えれば分かりそうなことでも、まず「これはどうすればいいですか」と聞きにくる。"
         "わたしが答えると、その通りに動く。正確ではあるが、"
         "自分で判断した形跡がどこにもない。\n"
         "①原因は本人ではなく、わたしの側にあった。"
         "分からない時間をなるべく短くしてやろうとした結果、"
         "考える機会まで一緒に取り上げてしまっていたのだ。\n"
         "そこでやり方を変えた。質問が来ても、すぐには答えず、"
         "「あなたならどうしますか」と聞き返すようにした。"
         "初めのうちは困った顔をしていたが、やがて「たぶんこうだと思うのですが」"
         "と自分の考えをそえて聞きにくるようになった。"
         "間違っていることもあったが、そういうときのほうが、"
         "説明したあとの理解は深かった。\n"
         "教えるとは、答えを渡すことだと思っていた。"
         "しかし本当に渡すべきなのは、答えのない場面で動き出せる力のほうだろう。"
         "そのためには、教える側が少しだけ待つ必要がある。"
         "待つのは、教えるよりずっと難しい。",
 "en": "When I was put in charge of training a new member of staff, I tried to teach "
       "everything carefully. I prepared a sheet setting out the steps in detail and told them "
       "to come and ask whenever anything was unclear. They listened well and worked through "
       "each task accurately. For the first few months it seemed to be going well. But after "
       "about six months something began to bother me. Whenever a situation arose that was not "
       "on the sheet, they froze. Even for things they could have worked out with a little "
       "thought, they would come and ask “how should I do this?” I would answer, and they "
       "would do exactly that. Accurate, but with no trace anywhere of their own judgement. "
       "The cause lay not with them but with me. In trying to keep the time they spent not "
       "knowing as short as possible, I had taken away the chance to think along with it. So I "
       "changed my approach. When a question came, instead of answering at once I would ask "
       "back, “what would you do?” At first they looked troubled, but before long they began "
       "coming with their own view attached: “I think it is probably this.” Sometimes they "
       "were wrong, but on those occasions their understanding after my explanation was "
       "deeper. I had thought teaching meant handing over answers. But what really ought to be "
       "handed over is the ability to start moving where there is no answer. For that, the one "
       "teaching has to wait a little. Waiting is far harder than teaching.",
 "qs": [
   {"q": "半年ほどたったころ、筆者は何が気になったのか。",
    "opts": ["新人が紙を読まなくなったこと",
             "新人が質問をしなくなったこと",
             "書いていない場面で新人が自分で判断しないこと",
             "新人の仕事が正確でなくなったこと"], "ans": 2,
    "why": "「紙に書いていない場面になると、手が止まってしまう」「自分で判断した形跡が"
           "どこにもない」とあります。"},
   {"q": "①原因は本人ではなく、わたしの側にあった とあるが、どういうことか。",
    "opts": ["教え方がくわしすぎて新人が困っていた",
             "早く答えを与えたことで考える機会をなくしていた",
             "紙の手順に間違いが含まれていた",
             "新人を指導する時間が足りていなかった"], "ans": 1,
    "why": "「分からない時間をなるべく短くしてやろうとした結果、考える機会まで一緒に"
           "取り上げてしまっていた」と説明されています。"},
   {"q": "やり方を変えたあと、どのような変化があったか。",
    "opts": ["新人が質問をまったくしなくなった",
             "新人が自分の考えをそえて聞きにくるようになった",
             "新人の答えが間違わなくなった",
             "指導に必要な時間が短くなった"], "ans": 1,
    "why": "「『たぶんこうだと思うのですが』と自分の考えをそえて聞きにくるようになった」"
           "とあります。間違うこともあったので3は誤りです。"},
   {"q": "筆者が最も言いたいことは何か。",
    "opts": ["手順を紙に書いて渡すことが指導の中心だ",
             "新人には正確さよりも速さを求めるべきだ",
             "答えを与えるより、自分で動ける力を育てることが大切だ",
             "指導者は新人の質問にすぐ答えるべきだ"], "ans": 2,
    "why": "最後に「本当に渡すべきなのは、答えのない場面で動き出せる力」と述べています。"},
 ]},
{
 "id": "n7", "tier": "N2", "kind": "情報検索", "title": "市民センター 講座のご案内",
 "body": "みどり市民センター　春の講座のご案内\n"
         "■申し込み方法\n"
         "窓口または電話で、三月十日までにお申し込みください。"
         "定員を超えた場合はちゅうせんとなり、結果は三月十五日までに郵便でお知らせします。\n"
         "■料金\n"
         "各講座とも三千円です。市内にお住まいの方、または市内にお勤めの方は二千円になります。"
         "お申し込みの際に、住所または勤務先が確認できるものをお持ちください。\n"
         "料金は初回の講座の日にお支払いください。\n"
         "■講座\n"
         "１　やさしい料理　　毎週火曜　午前十時〜十二時　全六回　定員二十名\n"
         "２　書道入門　　　　毎週木曜　午後二時〜四時　　全八回　定員十五名\n"
         "３　写真のとり方　　第二・第四土曜　午後一時〜三時　全四回　定員十名\n"
         "※２の書道入門のみ、筆と紙の代金として別に千円が必要です。\n"
         "※中止になった回は、後日おぎないます。",
 "en": "Midori Community Centre, spring courses. Applications: apply at the counter or by "
       "phone by 10 March. If applications exceed capacity a lottery will be held and results "
       "sent by post by 15 March. Fees: 3,000 yen for each course; 2,000 yen for those living "
       "in the city or working in the city. Bring something confirming your address or place "
       "of work when applying. Pay on the day of the first session. Courses: 1. Easy Cooking, "
       "Tuesdays 10am–12pm, 6 sessions, 20 places. 2. Introduction to Calligraphy, Thursdays "
       "2–4pm, 8 sessions, 15 places. 3. How to Take Photographs, 2nd and 4th Saturdays, "
       "1–3pm, 4 sessions, 10 places. Note: course 2 requires an additional 1,000 yen for "
       "brush and paper. Cancelled sessions will be made up at a later date.",
 "qs": [
   {"q": "市内の会社に勤めているが、別の市に住んでいる人が書道入門を申し込む場合、"
         "全部でいくら必要か。",
    "opts": ["二千円", "三千円", "四千円", "五千円"], "ans": 1,
    "why": "市内に勤めているので受講料は二千円。書道入門のみ筆と紙の代金が別に千円必要なので、"
           "合わせて三千円です。"},
   {"q": "申し込みについて、正しいものはどれか。",
    "opts": ["人数が多い場合は、先に申し込んだ人から順に決まる",
             "結果は三月十五日までに郵便で知らされる",
             "料金は申し込みの日に支払う",
             "申し込みは窓口でのみ受け付けている"], "ans": 1,
    "why": "「結果は三月十五日までに郵便でお知らせします」とあります。多い場合はちゅうせんで、"
           "料金は初回の講座の日、申し込みは窓口または電話です。"},
 ]},
]
