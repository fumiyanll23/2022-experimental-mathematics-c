# 1. 次の連立方程式の解を求めよ.
# (2) {4x-y+2z = -4, x+5y-2z = 7, -x+y-5z = -2}
import numpy as np
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
A = np.array(
    [
        [4, -1, 2],
        [1, 5, -2],
        [-1, 1, -5],
    ]
)
b = np.array([-4, 7, -2])
anss = np.linalg.solve(A, b)
print(f"(2) x = {anss}")
