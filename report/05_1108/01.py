# 1. 次の (離散) データに対する最小2乗近似 1 次式 g(x) = a_1 + a_2 x を求めよ.
import numpy as np
import sympy as sp
from nptyping import Float, NDArray, Shape

x = sp.Symbol("x")


def regression(
    xs: NDArray[Shape["5"], Float], ys: NDArray[Shape["5"], Float]
) -> sp.Expr:
    a2, a1 = np.polyfit(xs, ys, 1)

    return a1 + a2 * x


xys = np.array(
    [
        [14, 42],
        [15, 41],
        [17, 45],
        [18, 47],
        [20, 50],
    ]
)
xs = [x for x, _ in xys]
ys = [y for _, y in xys]
func = regression(xs, ys)
print(func)
