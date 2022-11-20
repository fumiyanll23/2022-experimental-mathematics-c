# written by TAGAWA, Takara and NARITA, Fumiya
# 常微分方程式{x' = (t^{2}+t+1) - (2t+1)x - x^{2} (t > 0), x(0) = 0.5}を解く
# 必要なモジュールをインポート
import sympy as sp
from sympy.plotting import plot

# tを変数、xを関数として定義
t = sp.Symbol("t")
x = sp.Function("x")
# 一般解を求める
eq = sp.Eq(x(t).diff(t,1), (t**2+t+1) - (2*t+1)*x(t) - x(t)**2)
ans_gen = sp.dsolve(eq, func=x(t))
print(f"一般解: {ans_gen.lhs} = {ans_gen.rhs}")
# 初期条件などを入力して特殊解を求める
ans_sp = sp.dsolve(eq, ics={x(0): 0.5})
print(f"特殊解: {ans_sp.lhs} = {ans_sp.rhs}")
# グラフを描画
plot(ans_sp.rhs, (t,0,5)).save("./07/img/03.png")
# Warning: これは動かないプログラムです!!
