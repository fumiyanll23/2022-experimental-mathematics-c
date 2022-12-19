# 2. 次の連立微分方程式の初期値問題の, 計算による厳密解またはプログラムによる近似解を求めよ．
import numpy as np
import sympy as sp
from nptyping import Float, NDArray, Shape

t = sp.Symbol("t")
x = sp.Function("x")
y = sp.Function("y")

def solve_diff_eq(
    coeffss: NDArray[Shape["2, 2"], Float],
    condss: NDArray[Shape["2, 2"], Float],
    )-> sp.Equality:
    """連立微分方程式を解く

    Args:
        coeffss (NDArray[Shape[&quot;2, 2&quot;], Float]): 係数
        condss (NDArray[Shape[&quot;2, 2&quot;], Float]): 初期条件

    Returns:
        sp.Equality: 特解
    """
    vars = np.array([x(t), y(t)])
    eqs = [
        sp.Eq(sp.Derivative(x(t), t, 1), np.dot(coeffss[0], vars)),
        sp.Eq(sp.Derivative(y(t), t, 1), np.dot(coeffss[1], vars)),
    ]
    ics = {}
    for i, (k, v) in enumerate(condss):
        if i == 0:
            ics[x(k)] = v
        else:
            ics[y(k)] = v

    return sp.dsolve(eqs, ics=ics)


# (1) {x' = y, y' = x, x(0) = -1, y(0) = 2}
coeffss = np.array([
    [0, 1],
    [1, 0],
])
condss = np.array([
    [0, -1],
    [0, 2],
])
anss = solve_diff_eq(coeffss, condss)
print("(1)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")

# (2) {x' = -2x+y, y' = -y, x(0) = 1, y(0) = 2}
coeffss = np.array([
    [-2, 1],
    [0, -1],
])
condss = np.array([
    [0, 1],
    [0, 2],
])
anss = solve_diff_eq(coeffss, condss)
print("(2)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")

# (3) {x' = -4x-5y, y' = x+2y, x(0) = 0, y(0) = -2/5}
coeffss = np.array([
    [-4, -5],
    [1, 2],
])
condss = np.array([
    [0, 0],
    [0, -2/5],
])
anss = solve_diff_eq(coeffss, condss)
print("(3)")
for ans in anss:
    print(f"{ans.lhs} = {ans.rhs}")
