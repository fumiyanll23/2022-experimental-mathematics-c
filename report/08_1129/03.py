# 3. 次の微分方程式の境界値問題の, 計算による厳密解またはプログラムによる近似解を求めよ.
import numpy as np
import sympy as sp
from nptyping import Float, NDArray, Shape

t = sp.Symbol("t")
x = sp.Function("x")

def solve_diff_eq(
    coeffs: NDArray[Shape["4"], Float],
    condss: NDArray[Shape["2, 2"], Float],
    ) -> sp.Equality:
    """微分方程式の境界値問題を解く

    Args:
        coeffs (NDArray[Shape[&quot;4&quot;], Float]): 係数
        condss (NDArray[Shape[&quot;2, 2&quot;], Float]): 境界条件

    Returns:
        sp.Equality: 特解
    """
    vars = np.array([sp.Derivative(x(t), t, 2), sp.Derivative(x(t), t, 1), x(t), 1])
    eq = sp.Eq(np.dot(coeffs, vars), 0)
    ics = {}
    for k, v in condss:
        ics[x(k)] = v

    return sp.dsolve(eq, ics=ics)


# (1) {x''+x = 0, x(0) = -1, x(π/2) = 1}
coeffs = np.array([1, 0, 1, 0])
condss = np.array([
    [0, -1],
    [sp.pi/2, 1],
])
ans = solve_diff_eq(coeffs, condss)
print(f"(1) {ans.lhs} = {ans.rhs}")

# (2) {x''+4x = 4t, x(0) = 0, x'(π/4) = 0}
coeffs = np.array([1, 0, 1, -4*t])
condss = np.array([
    [0, 0],
    [sp.pi/4, 0],
])
ans = solve_diff_eq(coeffs, condss)
print(f"(2) {ans.lhs} = {ans.rhs}")

# (3) {x''-2x'+2x = 0, x(0) = 0, x(1) = 2}
coeffs = np.array([1, -2, 2, 0])
condss = np.array([
    [0, 0],
    [1, 2],
])
ans = solve_diff_eq(coeffs, condss)
print(f"(3) {ans.lhs} = {ans.rhs}")
