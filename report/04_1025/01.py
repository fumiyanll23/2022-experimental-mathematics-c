# 1. 次の連立方程式の解を求めよ.
import numpy as np
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")

# (1)
A = np.array([
    [3, 1, 1],
    [1, 3, 1],
    [1, 1, 3],
])
b = np.array([8, 10, 12])
anss = np.linalg.solve(A, b)
print(f"(1) x = {anss}")

# (2)
A = np.array([
    [4, -1, 2],
    [1, 5, -2],
    [-1, 1, -5],
])
b = np.array([-4, 7, -2])
anss = np.linalg.solve(A, b)
print(f"(2) x = {anss}")

# (3)
eqs = [
    x**2 + y**2 - 4,
    4*x - 3*y,
]
# 2次連立方程式なので、sympyを用いて解く
anss = sp.solve(eqs)
print("(3)")
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")

# (4)
eqs = [
    x**3 - 3*x**2 + 4*x - y,
    4*x + y - 6,
]
anss = sp.solve(eqs)
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")

# (5) solverが実装されていないため、解くことはできない
eqs = [
    x - sp.cos(y),
    x - y,
]
anss = sp.solve(eqs)
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")

# (6) solverが実装されていないため、解くことはできない
eqs = [
    x**2 + 4*x - sp.E**y,
    x + y,
]
anss = sp.solve(eqs)
for ans in anss:
    print(f"x = {ans[x]}, y = {ans[y]}")
