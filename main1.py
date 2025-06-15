# print('hello,world')
'''
複数行コメント ここからコードを書く練習
                ２行目
'''
#単行コメント　ここからコードを書く練習
'''
# 演算子　operator
print(10+10)
print(10-1)
print(2*5)
print(10/2)
print(10//3)
print(7%4)
print(2**3)
print('1' + '1')
print('go ' * 3)
#エスケープシーケンス（/ or ￥をつかった物）

print('初めまして羽田です猪突猛進しがちです。')#基本文
print('初めまして\n羽田です\\猪突猛進しがちです。')#改行とバックスラッシュの表示
print('初めまして\'羽田です\"猪突猛進しがちです。')#シングル・ダブルクォーテーションを表示させる
'''

# # （複数行コメントにするヒアドキュメントと.strip()を'''のあとに使用すると前後の行も改行できる）
# #エスケープシーケンスだと見にくい下記の形にすると直感的にわかりやすい
# print('''
#     初めまして
# 羽田です
# 猪突猛進しがちです。
#     '''.strip())#一番わかりやすい形
# print('''初めまして
# 羽田です
# 猪突猛進しがちです。''')#stripを書かないパターン

'''
式について
関数内のものをプログラミングでは式と呼び、数学などの式とは若干異なる
また演算子の式には優先順位があり、**、*/％、+-の順になる
※特定箇所の優先順位を上げた場合は()を使用すれば最高順位となる
'''

#変数
'''
name = '羽田'
age = 30

print(name)
print(age)
print('半径が3cmの円の直径は、')
dia = 3 * 2
print(dia)
print('その円の円周の長さは、')

print(dia * 3.14)
'''
#変数名にはルールがある ※変数などに使用する文字や数字は識別子という
#1:予約語(keyword)35種ほどありそのキーワードは変数名として使えない（if,for,global,with...etc)
#2:数字を先頭にする変数名(× 1name,2name 〇 name1,name2)
#3:アンダースコアを先頭に2つつけた名前は使用しない 
#4:大文字小文字全角半角などの違いは完全に区別される　例　Name　name　では別の変数になる
#5:pythonでは変数名に小文字で始まる名詞形の名前をつける慣習がある

#変数の上書き
#変数の上書きは何度でも可能
#※予期せぬ不具合回避のため、原則変数の使いまわしはしない(再利用)
#pythonでは中身を書き換えられたくない変数は目立つように大文字の変数名をつける慣習がある
#大文字の変数名を見かけたらその変数には代入しないように注意（例　TAX_RATEなど)

#変数はまとめて代入出来る(アンパック代入)
#※一度に多くの変数定義を行うと、どの変数にどの値が入っているかわかりずらくなり、また変数と値の数が一致せず
#　エラーが起こりやすいので注意が必要
'''name,age,male = 'hada' , 30 ,'man'
print(age)
print(male)'''

'''
#変数自体への代入
#失敗例
age = 20
print('2025の年齢')
print(age)
age + 1
print('2026の年齢')
print(age)
age + 1
print('2026の年齢')
print(age)
age + 1
#成功例
age = 20
print('2025の年齢')
print(age)
age = age + 1
print('2026の年齢')
print(age)
age = age + 1
print('2026の年齢')
print(age)
age = age + 1
'''

#演算子は複合できる　
# 例　price = 100 price += 10 出力はprice100に10足したものが代入される
# +=　右辺の値と左辺の変数の値を足し算して変数に代入
# -=　右辺の値と左辺の変数の値を引き算して変数に代入
# *=　右辺の値と左辺の変数の値を掛け算して変数に代入
# /=　右辺の値と左辺の変数の値を割り算して変数に代入


'''
#input = ※変数名に代入する値をユーザーが決めた値にすることも可能
name = input('あなたの名前を入力してください >>')
print('おお'+ name + 'よ、そなたの到着を待っていた！')  
'''
# #input応用 失敗例(原因inputで入ったデータ形がstrのため計算ができない）
# price = input('料金を入力してください>>')
# number = input('人数を入力してください>>')
# payment + price / number
# print('お支払いは' + payment + '円です')

#主なデータ形　
# int　整数（100、-100）　
# float　少数(3.14,-0.5) 
# str　文字列（"hello"、'カレー'）　
# bool　真偽値（True False）

'''
pythonでは変数自体にデータ形の定めがない
※javaだとint型の変数ageはint型の値しか入力できない
なのでtype関数を使いどのデータ型か調べることができる        

'''
# x = 10
# print(type(x))

#input応用 
'''
price = input('料金を入力してください>>')
number = input('人数を入力してください>>')
price = int(price)
number = int(number)
payment = price / number
payment = str(payment)
print('お支払いは' + payment + '円です')
'''

#format
# name = 'hada'
# age = 24
# height = 170.4
# print('私の名前は{}で、年齢は{}歳で、身長は{}cmです'.format(name,age,height))

#input応用 fomat
# price = int(input('料金を入力してください>>'))
# number = int(input('人数を入力してください>>'))
# payment = int(price / number)
# print('お支払いは{}円です'.format(payment))

#f-string python3.6から対応　3.5以前では使えない
# name = 'hada'
# age = 24
# height = 170.4
# print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです')

#練習

#1-1
'''
print( 2+ 10 *5)
print( '7' * (3 + 4))
print(f'version{3 + 2 *0.1 +9 *0.01}')
print( 4 *'num' +'回目のTypeError')
'''
#1-2
# num =2
# print(type(num))
# var = 35+ num
# print(var)
# # num +='5' #TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# GLOBAL ='世界'+str(num)+'か国'
# print(GLOBAL)
# check_cpde = num *(9/3)
# print(check_cpde)

# weight = int(input('体重を入力してください'))
# height = int(input('身長を入力してください'))/100
# BMI = weight /height/height
# print(f'あなたのBMIは{BMI}になります')

