# coding:utf-8

import sys #コマンドライン引数用
import random #乱数用

#コマンドライン引数の必要なところのみコピーする
#スライスを使って、1つ目の要素から最後までを切り出して、input_listという名前を付けている。
input_list = sys.argv[1:]

#からの辞書を作る
jisho={}

#サイコロの目
data=[1,2,3,4,5,6]

#input_list.sort()

#一人目
#サイコロを振る
data_choice = random.choice(data)
#表示
print(input_list[0]+'さんは、'+str(data_choice)+'です。')
#辞書にいれる
jisho[input_list[0]]=data_choice #キーがinput_list[0]、値がdata_choice

#二人目
#サイコロを振る（同じサイコロを使いまわす）
data_choice = random.choice(data)
#表示
print(input_list[1]+'さんは、'+str(data_choice)+'です。')
#辞書にいれる
jisho[input_list[1]]=data_choice

#三人目
#サイコロを振る（同じサイコロを使いまわす）
data_choice = random.choice(data)
#表示
print(input_list[2]+'さんは、'+str(data_choice)+'です。')
#辞書にいれる
jisho[input_list[2]]=data_choice

#四人目
#サイコロを振る（同じサイコロを使いまわす）
data_choice = random.choice(data)
#表示
print(input_list[3]+'さんは、'+str(data_choice)+'です。')
#辞書にいれる
jisho[input_list[3]]=data_choice

#最後に、登録した辞書を全部表示する
print('辞書にいれると,'+str(jisho)+'となります。')