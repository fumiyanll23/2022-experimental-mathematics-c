# 1. 次の連立方程式の解を求めよ.
# (6) {x^2+4x = e^y, x+y = 0}
import math


def f(x: float, y: float) -> float:
    return x**2 + 4 * x - math.exp(y)


def g(x: float, y: float) -> float:
    return x + y


def fx(x: float, y: float) -> float:
    return 2 * x + 4


def gx(x: float, y: float) -> float:
    return 1


def fy(x: float, y: float) -> float:
    return -math.exp(y)


def gy(x: float, y: float) -> float:
    return 1


def newton(
    x0: float, y0: float, eps: float = 1e-7, iter_max: int = 100
) -> tuple[bool, tuple[float, float]]:
    """Newton法

    Args:
        x0 (float): xの初期値
        y0 (float): yの初期値
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        tuple[bool, tuple[float, float]]: 収束したのか?および近似解
    """
    ret = (False, (0, 0))
    for _ in range(iter_max):
        jacobian = fx(x0, y0) * gy(x0, y0) - fy(x0, y0) * gx(x0, y0)
        dx = (-f(x0, y0) * gy(x0, y0) + fy(x0, y0) * g(x0, y0)) / jacobian
        dy = (f(x0, y0) * gx(x0, y0) - fx(x0, y0) * g(x0, y0)) / jacobian
        x0 += dx
        y0 += dy
        if f(x0, y0) < eps and g(x0, y0) < eps:
            ret = (True, (x0, y0))
            break

    return ret


x0 = 0
y0 = 0
flag, (x, y) = newton(x0, y0)
if flag:
    print(f"x = {x}, y = {y}")
else:
    print("It didn't converged :(")
