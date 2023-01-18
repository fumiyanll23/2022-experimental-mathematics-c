# 2. 次の方程式の近似解を, Newton法を用いて, 求めよ.
import math


def newton(
    func, derivative_func, x0: float, eps: float = 1e-7, iter_max: int = 100
) -> float | None:
    """Newton法

    Args:
        func: 関数
        derivative_func: 導関数
        x0 (float): xの初期値
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        float | None: 近似解 (収束しないとき ==> None)
    """

    ret = None
    for _ in range(iter_max):
        x = x0 - func(x0) / derivative_func(x0)
        if abs(x - x0) < eps:
            ret = x0
            break
        x0 = x

    return ret


# (1)x^5 - x^4 + 5x^3 + 3x^2 - 4x - 7 = 0
def f_01(x):
    return x**5 - x**4 + 5 * x**3 + 3 * x**2 - 4 * x - 7


def df_01(x):
    return 5 * x**4 - 4 * x**3 + 15 * x**2 + 6 * x - 4


ans = newton(f_01, df_01, 10)
print("(1)")
if ans:
    print(f"x = {ans}")
else:
    print("It didn't converged :(")

# (2)x - log(x) = 0
def f_02(x):
    return x - math.log(x + 1)


def df_02(x):
    return 1 - 1 / (x + 1)


ans = newton(f_02, df_02, 10)
print("(2)")
if ans:
    print(f"x = {ans}")
else:
    print("It didn't converged :(")

# (3)x^2 - 3x + 2 = e^x
def f_03(x):
    return x**2 - 3 * x - math.exp(x)


def df_03(x):
    return 2 * x - 3 - math.exp(x)


ans = newton(f_03, df_03, 10)
print("(3)")
if ans:
    print(f"x = {ans}")
else:
    print("It didn't converged :(")
