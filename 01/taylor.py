# coding: utf-8
# 円周率の近似値をTaylor展開を用いて求める
#必要なモジュールをインポート
from decimal import *
#表示する円周率の桁数
getcontext().prec = 100
#arctanの定義
def arctan(x,N):
    s = Decimal(0)
    p = x
    for n in range(N):
        k = Decimal(2*n+1)
        if n%2==0:
            s = s + Decimal(1)/k * p
        else:
            s = s - Decimal(1)/k * p
        p = p * x * x
    return s
#mを大きくすることで精度が上がる
m = 10000
pi = Decimal(4)*arctan(Decimal(1), 3*m+2)

print(pi)
