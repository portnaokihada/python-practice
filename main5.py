# employees = [
#     {"name": "田中", "type": "時給", "wage": 1200, "hours": 6},
#     {"name": "佐藤", "type": "月給", "wage": 250000},
#     {"name": "鈴木", "type": "時給", "wage": 1000, "hours": 8},
# ]
# for week in employees:
#     if employees[1] == ('type','時給'):
#         print(f'{employees[0]}さんの１週間分給与は{(employees[2]*employees[3]*5)}円です')

# products = [
#     {"name": "ノート", "price": 120},
#     {"name": "ペン", "price": 80},
#     {"name": "バッグ", "price": 2400}
# ]
# tax_rate = 0.1  # 10%
# def calc_price_with_tax(price, tax_rate):
#     outprice == price * tax_rate
#     return outprice
# for outprice in products:
#     print(f'{outprice['name']}の税込価格は{outprice['price']}円です')

# students = [
#     {"name": "山田", "scores": [80, 75, 90]},
#     {"name": "佐藤", "scores": [60, 70, 65]},
#     {"name": "鈴木", "scores": [100, 95, 90]}
# ]
# def calc_average(scores):
#     average = sum(scores) /len(scores)
#     return average

# for item in students:
#     avg_out = calc_average(item["scores"])
#     print(f"{item["name"]}の平均点は{round(avg_out,2)}点です")
# customers = [
#     {"name": "田中", "is_member": True, "total": 6000},
#     {"name": "佐藤", "is_member": False, "total": 4800},
#     {"name": "鈴木", "is_member": True, "total": 4000}
# ]

# def price_off(total,is_member):
#     if is_member == True:
#         total *=0.9
#         if total >= 5000:
#             total *= 0.95
#     return round(total)
    
# for item in customers:
#     kaikei = price_off(item["total"],item["is_member"])
#     print(f"{item["name"]}さんの支払金額は{kaikei}円です")


# try:
#     sahen = int(input('割られたい数を入力してください＞＞'))
#     uhen = int(input('割りたい数を入力してください＞＞'))
#     print(sahen / uhen)
# except ValueError:
#     print('数字以外をにゅうりょくしないでください')
# except ZeroDivisionError:
#     print('０では割れません')

# results = [
#     {"name": "田中", "score": 80},
#     {"name": "佐藤", "score": 90},
#     {"name": "鈴木", "score": 70}
# ]
# file = open('result.txt','a')
# file.write(text + '/f'{results(name): {results(score)}点}'')
# file.close

# import urllib.request

# url = 'https://blog.python.org/'
# req = urllib.request.Request(url)
# with urllib.request.urlopen(req) as res:
#     body = str(res.read())

# if 'security' in body or 'vulnerability' in body:
#     print('セキュリティに関する記述があります')
#     print('https://blog.python.org/を確認してください')
# else:
#     print('調査対象のセキュリティ用語はありませんでした')

import tkinter as tk

root = tk.Tk()
root.geometry('240x240')
root.title('GUI Sample')
button = tk.Button(root, text='Hello, World')
button.pack()
root.mainloop()