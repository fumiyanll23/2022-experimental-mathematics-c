# written by NARITA, Fumiya
# 3. 次の微分方程式の境界値問題の, 計算による厳密解またはプログラムによる近似解を求めよ.
# 必要なモジュールをインポートする
import sympy as sp

# 準備
t = sp.Symbol("t")
x = sp.Function("x")

# (1) {x''+x = 0, x(0) = -1, x(π/2) = 1}
eq = sp.Eq(sp.Derivative(x(t), t, 2) + x(t), 0)
ics = {
    x(0): -1,
    x(sp.pi / 2): 1,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(1) {ans.lhs} = {ans.rhs}")

# (2) {x''+4x = 4t, x(0) = 0, x'(π/4) = 0}
eq = sp.Eq(sp.Derivative(x(t), t, 2) + 4 * x(t), 4 * t)
ics = {
    x(0): 0,
    x(sp.pi / 4): 0,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(2) {ans.lhs} = {ans.rhs}")

# (3) {x''-2x'+2x = 0, x(0) = 0, x(1) = 2}
eq = sp.Eq(sp.Derivative(x(t), t, 2) - 2 * sp.Derivative(x(t), t, 1) + 2 * x(t), 0)
ics = {
    x(0): 0,
    x(1): 2,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(3) {ans.lhs} = {ans.rhs}")
