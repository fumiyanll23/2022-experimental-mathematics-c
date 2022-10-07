# written by TAGAWA, Takara
#x-cosxをscipyを用いてプログラム
import scipy as sc
from scipy import optimize
def f(x):
    return x
def g(x):
    return sc.cos(x)
def h(x):
    return f(x)-g(x)
T=(optimize.fsolve(h,0))
print(T)
