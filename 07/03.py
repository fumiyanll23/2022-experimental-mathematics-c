#必要なモジュールをインポート
import sympy as sym
from sympy.plotting import plot

sym.init_printing(use_unicode=True)
#fを関数、xを変数として定義
f = sym.Function('f')
x = sym.Symbol('x')
#一般解を求める
eq = sym.Eq( f(x).diff(x,1) + (2*x+1) * f(x) + f(x)**2-(x**2+x+1))
ans = sym.dsolve(eq)
print(ans)
#初期条件などを入力して特殊解を求める
ans_2 = sym.dsolve(eq, ics={f(0):0.5})
print(ans_2)
ans_2
#グラフを描画
#plot(ans_2.rhs, (x, 0, 1))
