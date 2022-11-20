#必要なモジュールをインポート
import sympy as sym
from sympy.plotting import plot

#f,gを関数、xを変数として定義
x = sym.Symbol('x')
f = sym.Function('f')
g = sym.Function('g')
#与えられた連立方程式を入力
eq1 = sym.Eq(f(x).diff(x,1),-3*f(x)-2*g(x)+2*x)
eq2 = sym.Eq(g(x).diff(x,1),2*f(x)+g(x)-sym.sin(x))
#一般解を求める
ans = sym.dsolve([eq1, eq2])
print(ans)
#初期条件などを入力し特殊解を求める
ans_2 = sym.dsolve([eq1, eq2],ics={f(0):4.5, g(0):-6.5})
print(ans_2)
#グラフを描画f(x)が青、g(x)がオレンジ
plot(ans_2[0].rhs,ans_2[1].rhs,(x,0,10))
