# written by NARITA, Fumiya
# 常微分方程式{y'' = -9y (0<x<π), y(0) = y(π) = 0}を解く
# 必要なモジュールをインポート
import sympy as sp
from sympy.plotting import plot

# 変数xおよび関数yを定義する
x = sp.Symbol("x")
y = sp.Function("y")
# 常微分方程式を与える
eq = sp.Eq(y(x).diff(x, 2), -9 * y(x))
# 一般解を求める
ans_gen = sp.dsolve(eq)
print(f"一般解: {ans_gen.lhs} = {ans_gen.rhs}")
# 境界値条件代入して特殊解を求める
ans_sp = sp.dsolve(eq, ics={y(0): 0, y(sp.pi): 0})
print(f"特殊解: {ans_sp.lhs} = {ans_sp.rhs}")
# 任意定数を指定して、特殊解のグラフを描画する
plotted = plot(sp.sin(3 * x), (x, 0, sp.pi), show=False, label="sin(3x)", legend=True)
for c in range(2, 6):
    plotted.append(
        plot(
            c * sp.sin(3 * x),
            (x, 0, sp.pi),
            show=False,
            label=f"{c}*sin(3x)",
            legend=True,
        )[0]
    )
plotted.save("./08/img/02-01.png")
plotted.show()
