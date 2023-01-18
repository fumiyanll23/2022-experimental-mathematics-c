# 1. 次の連立方程式の解を求めよ.
# (1) {3x+y+z = 8, x+3y+z = 10, x+y+3z = 12}
import numpy as np
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
A = np.array(
    [
        [3, 1, 1],
        [1, 3, 1],
        [1, 1, 3],
    ]
)
b = np.array([8, 10, 12])
anss = np.linalg.solve(A, b)
print(f"(1) x = {anss}")
