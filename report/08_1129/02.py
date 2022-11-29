# written by NARITA, Fumiya
# 2. 次の連立微分方程式の初期値問題の, 計算による厳密解またはプログラムによる近似解を求めよ．
# 必要なモジュールをインポートする
import sympy as sp

# 準備
t = sp.Symbol("t")
x = sp.Function("x")
y = sp.Function("y")

# (1) {x' = y, y' = x, x(0) = -1, y(0) = 2}
eq01 = sp.Eq(sp.Derivative(x(t), t, 1), y(t))
eq02 = sp.Eq(sp.Derivative(y(t), t, 1), x(t))
ics = {
    x(0): -1,
    y(0): 2,
}
anss = sp.dsolve([eq01, eq02], ics=ics)
print("(1)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")

# (2) {x' = -2x+y, y' = -y, x(0) = 1, y(0) = 2}
eq01 = sp.Eq(sp.Derivative(x(t), t, 1), -2 * x(t) + y(t))
eq02 = sp.Eq(sp.Derivative(y(t), t, 1), -y(t))
ics = {
    x(0): 1,
    y(0): 2,
}
anss = sp.dsolve([eq01, eq02], ics=ics)
print("(2)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")

# (3) {x' = -4x-5y, y' = x+2y, x(0) = 0, y(0) = -2/5}
eq01 = sp.Eq(sp.Derivative(x(t), t, 1), -4 * x(t) - 5 * y(t))
eq02 = sp.Eq(sp.Derivative(y(t), t, 1), x(t) + 2 * y(t))
ics = {
    x(0): 0,
    y(0): -2 / 5,
}
anss = sp.dsolve([eq01, eq02], ics=ics)
print("(3)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")
