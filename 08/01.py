# written by TAGAWA, Takara
# 常微分方程式{y'' = sinx (0<x<π), y(0) = y(π) = 0}を解く
# 必要なモジュールをインポート
import sympy as sp
from sympy.plotting import plot

# 変数xおよび関数yを定義する
x = sp.Symbol("x")
y = sp.Function("y")
# 常微分方程式を与える
eq = sp.Eq(y(x).diff(x, 2), sp.sin(x))
# 一般解を求める
ans_gen = sp.dsolve(eq)
print(f"一般解: {ans_gen.lhs} = {ans_gen.rhs}")
# 境界値条件代入して特殊解を求める
ans_sp = sp.dsolve(eq, ics={y(0): 0, y(sp.pi): 0})
print(f"特殊解: {ans_sp.lhs} = {ans_sp.rhs}")
# 特殊解のグラフを描画する
plot(ans_sp.rhs, (x, 0, sp.pi)).save("./08/img/01.png")
