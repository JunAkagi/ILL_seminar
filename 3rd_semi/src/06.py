# coding: UTF-8
'''
Created on 2016/11/17

@author: JUN_AKAGI
'''
import sys
import math

#コマンドライン引数を読み込み、文字列から小数に変換する。
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

#判別式を計算する。
D=b**2-4*a*c

if D>0:  #判別式が正の場合
    #解が２つある。
    x0=(-b-math.sqrt(D))/(2.0*a)
    x1=(-b+math.sqrt(D))/(2.0*a)

    #表示するときは文字列に直して、連結して表示する。
    print('('+str(a)+')x**2+('+str(b)+')x+('+str(c)+')=0の解は、('+str(x0)+')と('+str(x1)+')です。')

elif D==0: #判別式が0の場合
    #解はひとつ
    x= -b/(2.0*a)
    print('('+str(a)+')x**2+('+str(b)+')x+('+str(c)+')=0の解は、('+str(x)+')です。')

elif D<0:
    #解は複素数
    xR=-b/(2.0*a)
    xI=math.sqrt(-D)/(2.0*a)
    print('('+str(a)+')x**2+('+str(b)+')x+('+str(c)+')=0の解は、('+str(xR)+'-'+str(xI)+'i'+')と('+str(xR)+'+'+str(xI)+'i'+')です。')