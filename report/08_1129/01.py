# written by NARITA, Fumiya
# 1. 次の微分方程式の初期値問題の, 計算による厳密解またはプログラムによる近似解を求めよ．
# 必要なモジュールをインポートする
import sympy as sp

# 準備
t = sp.Symbol("t")
x = sp.Function("x")

# (1) {x''-x = 0, x(0) = -1, x'(0) = 2}
eq = sp.Eq(sp.Derivative(x(t), t, 2) - x(t), 0)
ics = {
    x(0): -1,
    sp.Derivative(x(t), t, 1).subs(t, 0): 2,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(1) {ans.lhs} = {ans.rhs}")

# (2) {x''+3x'+2x = 0, x(0) = 1, x'(0) = 0}
eq = sp.Eq(sp.Derivative(x(t), t, 2) + 3 * sp.Derivative(x(t), t, 1) + 2 * x(t), 0)
ics = {
    x(0): 1,
    sp.Derivative(x(t), t, 1).subs(t, 0): 0,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(2) {ans.lhs} = {ans.rhs}")

# (3) {x''+2x'-3x = 0, x(0) = 0, x'(0) = 2}
eq = sp.Eq(sp.Derivative(x(t), t, 2) + 2 * sp.Derivative(x(t), t, 1) - 3 * x(t), 0)
ics = {
    x(0): 0,
    sp.Derivative(x(t), t, 1).subs(t, 0): 2,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(3) {ans.lhs} = {ans.rhs}")
