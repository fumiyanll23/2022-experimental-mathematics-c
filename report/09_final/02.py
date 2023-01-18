# 2. 次の問題のうち, 少なくとも 1 問を解け
import sympy as sp

t = sp.Symbol("t")
x = sp.Function("x")
y = sp.Function("y")

# (i) 次の微分方程式の初期値問題の解を求めよ．
# {x'''-2x''-x'+2x = 0 (t>0), x(0) = -1, x'(0) = 0, x''(0) = 0}
eq = sp.Eq(
    sp.Derivative(x(t), t, 3)
    - 2 * sp.Derivative(x(t), t, 2)
    - sp.Derivative(x(t), t, 1)
    + 2 * x(t),
    0,
)
ics = {
    x(0): -1,
    sp.Derivative(x(t), t, 1).subs(t, 0): 0,
    sp.Derivative(x(t), t, 2).subs(t, 0): 0,
}
ans = sp.dsolve(eq, ics=ics)
print(f"(i) {ans.lhs} = {ans.rhs}")

# (ii) 次の連立微分方程式の初期値問題の解を求めよ.
# {x'' = -3(x-y), y'' = 3(x-y)-2y, x(0) = 5, x'(0) = 0, y(0) = 2, y'(0) = 0}
eq01 = sp.Eq(sp.Derivative(x(t), t, 2), -3 * (x(t) - y(t)))
eq02 = sp.Eq(sp.Derivative(y(t), t, 2), 3 * (x(t) - y(t)) - 2 * y(t))
ics = {
    x(0): 5,
    sp.Derivative(x(t), t, 1).subs(t, 0): 0,
    y(0): 2,
    sp.Derivative(y(t), t, 1).subs(t, 0): 0,
}
anss = sp.dsolve([eq01, eq02], ics=ics)
print("(ii)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")
