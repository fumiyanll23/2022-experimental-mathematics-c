# written by TAGAWA, Takara
#x-cosxをscipyを用いてプログラム
#scipyのインストール
import scipy as sc
#最適化関数のインストール
from scipy import optimize
def f(x):
    return x#f(x)=xの定義
def g(x):
    return sc.cos(x)#g(x)=cos(x)の定義
def h(x):
    return f(x)-g(x)#h(x)=f(x)-g(x)の定義
T=(optimize.fsolve(h,0))#h(x)=0を解く
print(T)
