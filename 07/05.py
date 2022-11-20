# written by TAGAWA, Takara and NARITA, Fumiya
# 常微分方程式{x' = -3x - 2y + 2t (t > 0), y' = 2x + y - sin(t) (t > 0), x(0) = 4.5, y(0) = -6.5}を解く
# 必要なモジュールをインポート
import sympy as sp
from sympy.plotting import plot

# tを変数、x,yを関数として定義
t = sp.Symbol("t")
x = sp.Function("x")
y = sp.Function("y")
# 与えられた連立方程式を入力
eq1 = sp.Eq(x(t).diff(t,1), -3*x(t) - 2*y(t) + 2*t)
eq2 = sp.Eq(y(t).diff(t,1), 2*x(t) + y(t) - sp.sin(t))
# 一般解を求める
anss_gen = sp.dsolve([eq1, eq2])
print("一般解:")
print(f"{anss_gen[0].lhs} = {anss_gen[0].rhs}")
print(f"{anss_gen[1].lhs} = {anss_gen[1].rhs}")
# 初期条件などを入力して特殊解を求める
anss_sp = sp.dsolve([eq1, eq2], ics={x(0): 4.5, y(0): -6.5})
print("特殊解:")
print(f"{anss_sp[0].lhs} = {anss_sp[0].rhs}")
print(f"{anss_sp[1].lhs} = {anss_sp[1].rhs}")
# グラフを描画。x(t)が青、y(t)がオレンジ
plot_x = plot(anss_sp[0].rhs, (t,0,10), show=False, line_color="blue", label="x(t)", legend=True)
plot_y = plot(anss_sp[1].rhs, (t,0,10), show=False, line_color="orange", label="y(t)", legend=True)
plot_x.append(plot_y[0])
plot_x.save("./07/img/05.png")
plot_x.show()
