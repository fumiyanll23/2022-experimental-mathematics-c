# 次の (離散) データに対する回帰直線を求めよ．
# (0, 5), (1, 8), (3, 11), (5, 4)
import numpy as np
import sympy as sp
from nptyping import Float, NDArray, Shape


def regression_line(
    x: sp.Symbol, xs: NDArray[Shape["4"], Float], ys: NDArray[Shape["4"], Float], deg: int=1
    ) -> sp.Expr:
    """回帰直線を求める

    Args:
        x (sp.Symbol): 変数
        xs (NDArray[Shape["4"], Float]): x座標
        ys (NDArray[Shape["4"], Float]): y座標

    Returns:
        sp.Expr: 回帰直線
    """
    a, b = np.polyfit(xs, ys, deg=deg)

    return a*x + b


x = sp.Symbol("x")
xys = np.array([(0, 5), (1, 8), (3, 11), (5, 4)])
xs = np.array([x for x, _ in xys])
ys = np.array([y for _, y in xys])
ans = regression_line(x, xs, ys, 1)
print(f"y = {ans}")
