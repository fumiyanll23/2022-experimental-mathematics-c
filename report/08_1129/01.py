# 1. 次の微分方程式の初期値問題の, 計算による厳密解またはプログラムによる近似解を求めよ．
import numpy as np
import sympy as sp
from nptyping import Float, NDArray, Shape

t = sp.Symbol("t")
x = sp.Function("x")

def solve_diff_eq(
    coeffs: NDArray[Shape["4"], Float],
    condss: NDArray[Shape["2, 2"], Float],
    ) -> sp.Equality:
    """微分方程式の初期値問題を解く

    Args:
        coeffs (NDArray[Shape[&quot;4&quot;], Float]): 係数
        condss (list[list[float]]): 初期条件

    Returns:
        sp.Equality: 特解
    """
    vars = np.array([sp.Derivative(x(t), t, 2), sp.Derivative(x(t), t, 1), x(t), 1])
    eq = sp.Eq(np.dot(coeffs, vars), 0)
    ics = {}
    for i, (k, v) in enumerate(condss):
        if i == 0:
            ics[x(k)] = v
        else:
            ics[sp.Derivative(x(t), t, 1).subs(t, k)] = v

    return sp.dsolve(eq, ics=ics)


# (1) {x''-x = 0, x(0) = -1, x'(0) = 2}
coeffs = np.array([1, 0, -1, 0])
condss = np.array([
    [0,-1],
    [0, 2],
])
ans =solve_diff_eq(coeffs, condss)
print(f"(1) {ans.lhs} = {ans.rhs}")

# (2) {x''+3x'+2x = 0, x(0) = 1, x'(0) = 0}
coeffs = np.array([1, 3, 2, 0])
condss = np.array([
    [0,1],
    [0,0],
])
ans = solve_diff_eq(coeffs, condss)
print(f"(2) {ans.lhs} = {ans.rhs}")

# (3) {x''+2x'-3x = 0, x(0) = 0, x'(0) = 2}
coeffs = np.array([1, 2, -3, 0])
condss = np.array([
    [0,0],
    [0,2],
])
ans = solve_diff_eq(coeffs, condss)
print(f"(3) {ans.lhs} = {ans.rhs}")
