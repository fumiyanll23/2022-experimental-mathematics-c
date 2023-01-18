# 1. 次の連立方程式の解を求めよ.
# (4) {x^3-3x^2+4x-y = 0, 4x+y-6 = 0}
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
eqs = [
    x**3 - 3 * x**2 + 4 * x - y,
    4 * x + y - 6,
]
anss = sp.solve(eqs)
print("(4)")
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")
