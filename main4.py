# count = 0
# while count < 3:
#     count += 1
#     print(f"ひつじが{count}匹")
# print("おやすみなさい")
#無限ループになる可能性があるから処理を中断できるショートカットを覚えておくといいかも

# is_awake = True
# count = 0
# while is_awake == True:
#     count += 1
#     print(f'ひつじが{count}匹')
#     key = input('もう眠りそうですか?(y/n)>>')
#     if key =='y':
#         is_awake = False
# print("おやすみなさい")

#bool型でフラグを表す
#　ある事柄や状態を二者択一であらすには、bool型を利用する。フラグを意味する変数名は「is_xxx」とするが一般的

#4.1.4 コンテナは繰り返しと組み合わせて使うのが一般的
# count = 0
# student_num = int(input('学生の人数を入力>>'))
# score_list = list()
# while count < student_num:
#     count += 1
#     score = int(input(f'{count}人目の試験の得点を入力>>'))
#     score_list.append(score)
# print(score_list)
# total = sum(score_list)
# print(f'平均点は{total / student_num}点です')

# scores =[80,20,75,60]
# count = 0
# while count < len(scores):
#     if scores[count] >=60:
#         print('合格')
#     else:
#         print('不合格')
#     count += 1

#for文　リストなどのデータのある集まりについて先頭から末尾まで順に参照する場合にはより安全かつエレガントなfor文がよく利用される
# scroes =[80,20,75,60]
# for data in scroes:
#     if data >=60:
#         print('OK')
#     else:
#         print('NG') 


#for文やwhile文を使うときのセットは要注意？　決まった回数を繰り返す場合はfor文を利用すると楽にループ記述できる
# for num in range(3): #range（用意された関数）は整数列を作る(０から指定数より１小さい整数までの要素を持つものまで)
#     print('yesdoit')

'''
使い分けについて
while文：繰り返す回数の目処が立たないときにつかう
for文　：繰り返す回数の目処が立つときにつかう
'''
#4.3 繰り返しの強制修了

#必要のない繰り返しまで行っている（膨大なデータの時は処理が終わらず次の処理に行けないユーザーが使いにくい）
# ages = [28,50,8,20,78,25,22,10,27,33]
# num = 5
# samples = list()
# for age in ages:
#     if 20 <= age < 30:
#         if len(samples) < num:
#             samples.append(age)
# print(samples)

#break文を入れることで抽出が終わったときに繰り返しをとめいている
# ages = [28,50,8,20,78,25,22,10,27,33]
# num = 5
# samples = list()
# for age in ages:
#     if 20 <= age < 30:
#         if len(samples) < num:
#             samples.append(age)
#             if len(samples) == num:
#                 break
# print(samples)

#不要な回のループだけでスキップする　continue文
# ages = [28,50,'ひみつ',20,78,25,22,10,'無回答',33]
# samples = list()
# for date in ages:
#     if not isinstance(date,int): #insinstance関数は(データ,データ型)と記載し一致していたらTrueに置き換わる
#         continue
#     if date <20 or date >=30:
#             continue
#     samples.append(date)
# print(samples)

'''
1　5回
2　4回
3　5回
4　5回
5　1回
6　1回
7　1回
8　2回
'''
#4-2
# okawari = True
# count = 1
# print('カレーを召し上がれ')
# while okawari == True:
#     print(f'{count}皿のカレーを食べました')
#     key = (input('おかわりはいかがですか？(y/n)>>'))
#     if key == 'y':
#        count += 1
#        else:
#         okawari = False
# print('ごちそうさまでした。')

#4-3

# for num in [10,9,8,7,6,5,4,3,2,1]:
#     print(f'{num}、', end = '')
# print('letgo')
'''
for n in range(10):
    print(f'{10 - n}、', end='')
print('Lift off!')
'''
#4-4

# for sahen in [1,2,3,4,5,6,7,8,9] :
#     for uhen in [1,2,3,4,5,6,7,8,9] :
#         if len(sahen) % 2 == 0:
#             continue
#             if (sahen * uhen) >= 50:
#                 continue
#                 print(sahen*uhen)
            
#4-5
# temp = {8:7.8,9:9.1,10:10.2,11:11.0,12:12.5,13:12.4,15:13.8,16:12.9,17:12.4}
# for temp in range():
#     print(temp)

# #練習問題5
# #1
# def weather():
#     print('今日は晴れです')

# #2
# def calc_circle_area(clac_circle):
#     print(clac_circle * clac_circle *3.14)
# calc_circle_area(int(input('半径を入力してください>>')))

# #3
# def nowstr(how,min,sec):
#     zikoku = (f'{how}時{min}分{sec}秒')
#     return zikoku
# #4
# def nowint(how,min,sec)
#     return  how,min,sec
# #5
# def is_leaptear(year):
#     if year % 400 == 0:
#         print(f'{year}はうるう年です')
# #2-1
# def is_leaptear(year):
#     if year % 400 == 0:
#         print(f'西暦{year}年はうるう年です')
#     elif year % 4 ==0:
#         print(f'西暦{year}年はうるう年です')
#     else:
#         year % 100 ==0
#         print(f'西暦{year}年はうるう年ではない')

# is_leaptear(year(input('現在の西暦を入力してください>>')))

# def int_input(messge):
#     messge = (int(input(f'{messge}を入力してください')))
#     return messge
'''６章'''

#foamt関数の謎
# tpl = '3人目は{}さん'
# names = ['松田','浅木']
# names.append('工藤')
# message = tpl.format(names[2])
# print(message)

# num = 10
# print(num.bit_length())
# names = ['matuda','asagi']
# names.append('kudou')

import matplotlib.pyplot as plt

weight = [68.4, 68.0, 69.5, 68.4, 68.6, 70.2, 71.4, 70.8, 68.5, 68.6, 68.3, 68.4]
plt.plot(weight)
plt.show()
import requests

response = requests.get('https://www.python.org/downloads/')
text = response.text
print(text)