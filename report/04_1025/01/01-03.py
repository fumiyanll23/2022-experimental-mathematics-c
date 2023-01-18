# 1. 次の連立方程式の解を求めよ.
# (3) {x^2+y^2 = 4, 4x = 3y}
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
eqs = [
    x**2 + y**2 - 4,
    4 * x - 3 * y,
]
anss = sp.solve(eqs)
print("(3)")
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")
