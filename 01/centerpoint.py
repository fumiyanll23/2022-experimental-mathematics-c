# written by TAGAWA, Takara
# 円周率の近似値を中点公式を用いて求める
#必要なモジュールをインポート
import math
#関数f(x)を定義
def f(x):
    return  math.sqrt(1-x*x)
#nを大きくすることで∞の表現に近づける
n=100
total = 0
for k in range (1,n):
    total += f((2*k-1)/(2*n))

pi=  total*4/n
print(pi)
