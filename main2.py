'''リスト'''
# menmbers=['工藤','マツダ','ささき']
# print(menmbers[2])

# scores = [88,90,95]
# total = sum(scores)
# avg = total/len(scores)
# print(f'合計{total}点、平均{avg}点')

# menmbers=['工藤','マツダ','ささき']
# menmbers.remove('工藤')
# print(menmbers)

# menmbers=['工藤','マツダ','ささき']
# menmbers[0]=('トヨタ')
# print(menmbers)
'''スライスによる範囲指定'''
# a = [10,20,30,40,50]
# print(a[1:3])
# print(a[-3])
# print(a[:3])

'''ディクショナリ　{}値とキーを格納する'''
# scores = {'network':60,'datebase':60,'security':50}
# print(scores)

# scores = {'network':60,'datebase':80,'security':50}
# print(scores['datebase'])


# scores = {'network':60,'datebase':60,'security':50}
# scores ['programming'] = 65
# scores ['security'] = 65
# print(scores)

# scores = {'network':60,'datebase':60,'security':50}
# scores ['programming'] = 65
# del scores ['security']
# print(scores)

# scores = {'network':60,'datebase':60,'security':50}
# total = sum(scores.values())
# print(total)

'''※リストは[]　タプルは（）'''

# menmbers=(70,80,55)
# print(menmbers)
# print(menmbers[0])
# print(f'要素数は{len(menmbers)}')
# print(f'合計は{sum(menmbers)}')

#エラーになるタプルは値の変更不可
# menmbers=(70,80,55)
# menmbers[0] = 80
# print(f'要素数は{len(menmbers)}')
# print(f'合計は{sum(menmbers)}')

'''セット
（重複した値はNG、添え字やキーの概念なし、append関数じゃなくaddでついか、
種類の管理に向いている）'''
# scores = {70,80,55,80}
# scores.add(80)
# print(scores)
# print(f'要素数は{len(scores)}')
# print(f'合計は{sum(scores)}')

#コンテナの相互変換
'''
scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))       # リストmembersをタプルに変換して表示
print(list(scores))         # scoresのキーをリストに変換して表示
print(set(scores.values())) # scoresの値をセットに変換して表示
'''
#コンテナ（ディクショナリ）に二重構造で管理できる
#メンバーごとの趣味の管理に向いている
'''
matsuda_scores = {'network':60, 'database':80, 'security':50}
asagi_scores = {'network':80, 'database':75, 'security':92}
member_scores = {
    '松田': matsuda_scores,
    '浅木': asagi_scores
}
'''
#ディクショナリの中にセットをネスト（構文に同じ構文を入れること）
'''
member_hobbies = {
'松田': {'SNS', '麻雀', '自転車'},
'浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
# 全員の趣味一覧を表示する
print(member_hobbies)
# 松田くんの趣味一覧を表示する
print(member_hobbies['松田'])
# 浅木さんの趣味一覧を表示する
print(member_hobbies['浅木'])
'''

#リストの中にリストを入れた構造は２次元リストとも言われる
#さらにリストを入れていき多重構造にすることも可能、本格的なデータ分析ではネストしたコンテナの活用はかかせない
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]     # aを0番目、bを1番目とする2次元リストcを定義

print(c)       # リストc全体を参照
print(c[0])    # リストcの0番目(リストa)だけを参照
print(c[1][2]) # リストcの1番目(リストb)の2番目だけを参照
'''
#集合演算（積集合）　セットの共通項を求める
'''
member_hobbies = {
    '松田': {'SNS', '麻雀', '自転車'},
    '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies) # 2人に共通する趣味一覧を表示す
'''
#集合演算（４つ）　セットの共通項を求める
'''
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)#和集合
print(A & B)#積集合
print(A - B)#差集合
print(A ^ B)#対象差
'''

#2.7練習問題
'''
2-1
(1)ディクショナリ
(2)リスト
(3)セット
(4)セット
(5)ディクショナリ
'''
#2-2
'''
scores = []
scores.append(int(input('国語の点数を入力してください')))
scores.append(int(input('算数の点数を入力してください')))
scores.append(int(input('理科の点数を入力してください')))
scores.append(int(input('社会の点数を入力してください')))
scores.append(int(input('英語の点数を入力してください')))
print(f'合計点は{sum(scores)}')
print(f'平均点は{sum(scores)/len(scores)}')
'''

#2-3

#100%
# one_hobby = {'game','anime','show','world','japan'}
# two_hobby = {'TV','anime','show','world','japan'}
# print(input('心の順ができたEneerキーを押してください'))
# print(f'相性度{len(one_hobby&two_hobby)/len(one_hobby|two_hobby)*100}%')

# one_hobby = {'game','anime','show','world','japan'}
# two_hobby = {'TV','anime','show','world','japan'}
# print(input('心の準備ができたEneterキーを押してください'))
# seki = one_hobby&two_hobby
# wa = one_hobby|two_hobby
# sekiwa = len(seki)/len(wa)*100
# print(f'相性度は{sekiwa}%でした')

# player1 = {'読書', '昼寝', '映画鑑賞', '散歩', '料理'}
# player2 = {'テニス', '将棋', '料理', '読書1', '旅行'}
# input('心の準備ができたらEnterキーを押してください')
# common = player1 & player2
# total = player1 | player2
# compatibility_rate = len(common) / len(total) * 100
# print(f'相性度は{compatibility_rate}パーセントでした')


'''
ざっくりまとめ
用途・場面	よく使われる方法	説明
エンタメ相性診断（趣味・恋愛など）	あなたの考え方（一致数 ÷ 固定数）	直感的で分かりやすい
データ分析・レコメンド	Jaccard係数（積集合 ÷ 和集合）	柔軟かつ理論的に妥当

どちらを使うべきか？
ユーザーにわかりやすくしたい → あなたの方法
　**「お互いの趣味がどれだけ一致したか？」**を感覚的に示したいとき

　質問数や趣味数が事前に固定されているとき（例：お互い5個ずつ選ぶなど）

　恋愛診断、友達との相性診断、心理テストなど

選択数がバラバラ・数が多い → Jaccard係数

　アイテムや好みの比較を柔軟にしたいとき（選択数が人によって異なる）

　SNS・ECサイト・音楽アプリなどで「似たユーザー」を探すとき

　統計的・数学的な比較が必要なとき

「類似度」や「相性」を測る指標は、使うデータのタイプ（集合／数値／ベクトルなど）によっていくつかの定番があります。

A. 集合ベース（Jaccard係数と近い仲間）
Jaccard係数
> 共通する要素 ÷ 全体の要素数

Dice係数（Sørensen-Dice係数）
> 2 × |共通要素数| ÷ (|集合A| + |集合B|)
→ Jaccardより共通要素を強調する

B. 数値・ベクトルデータベース
たとえば、性格診断・スコア比較・アンケートの回答など数値情報を使う場合：

ユークリッド距離（直線距離）
→ 距離が近いほど似ている

コサイン類似度
> ベクトルの角度の違いを計算。傾向（方向性）の近さを測る
→ 0.0～1.0で表す（0: 無関係、1: 完全一致）

ピアソン相関係数
→ 相関が高い＝似ている（-1～1の範囲）

C. 特化型・実用型
Levenshtein距離（編集距離）
→ 文字列の違い（例：名前の類似度、タイプミス検出など）

ハミング距離
→ 同じ長さの文字列・ビット列の違いを数える（機械学習でよく使う）

補足：実際には「組み合わせて使う」ことも多い
例：

Jaccard係数＋重み付き（重要な項目を強調）

数値と集合を混ぜてハイブリッドなスコアにする

② プログラミングを学ぶ中で、こういう指標は都度覚えるべきか？
結論：原則として「必要になった時に調べる」でOKです。

ただし、以下のような考え方がおすすめです：
【おすすめ学習スタンス】
ポイント	内容
名前と特徴だけ軽く知る	「Jaccardは集合の重なり」「コサインはベクトルの角度」など、ざっくり意味を知っておく
使いどころの感覚を持つ	「これは集合の比較だな」→「Jaccardで調べてみようかな」くらいの感覚で十分
プロジェクトで使うときに深掘り	実装の際に公式や例を調べて、正確な数式・意味を理解する
使ったらメモる（学習ログ化）	何かの指標を使ったら、自分のノートやNotionに残しておくと再利用しやすい

今後のための最小セット（おすすめ指標）
データの種類	指標名	覚え方（ざっくり）
集合（趣味など）	Jaccard / Dice	共通してるかどうか
数値（点数など）	ユークリッド距離	距離が近い = 似てる
ベクトル	コサイン類似度	傾向が似てるかを見る
文字列	編集距離	名前などの「スペルの違い」

最後に
プログラミング学習においては、すべての理論を最初から覚える必要は全くありません。
ただし、「似たものを判定したい」ような問題に出くわしたときに、どんな考え方があるかを知っておくと、設計・実装の引き出しが増えます。

あなたの今回のような好奇心と問題意識を持っておくことが、非常に大きな強みになりますよ！

'''