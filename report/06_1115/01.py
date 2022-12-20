# 1. 次の積分の値を, (i) 厳密な計算, (ii) 中点公式, (iii) 台形公式, (iv) シンプソン公式を用いて求めよ.
import numpy as np
from scipy import integrate


def f(x: float) -> float:
    """
    (1)の被積分関数
    """
    return x**4 + 3 * x**2 + 1


def g(x: float) -> float:
    """
    (2)の被積分関数
    """
    return np.cos(x)


def midpoint(func, xmin: float, xmax: float, n: int = 100000) -> float:
    """中点公式を用いた数値積分

    Args:
        func : 被積分関数
        xmin (float): 積分区間の下端
        xmax (float): 積分区間の上端
        n (int, optional): 分割数. デフォルトは100000.

    Returns:
        float: 定積分
    """
    ret = 0
    h = (xmax - xmin) / n
    for i in range(1, n + 1):
        ret += func(xmin + (2 * i - 1) * h / 2)

    return ret * h


def trapezoidal(func, xmin: float, xmax: float, n: int = 100000) -> float:
    """台形公式を用いた数値積分

    Args:
        func : 被積分関数
        xmin (float): 積分区間の下端
        xmax (float): 積分区間の上端
        n (int, optional): 分割数. デフォルトは100000.

    Returns:
        float: 定積分
    """
    xs = np.linspace(xmin, xmax, n)
    ys = func(xs)

    return integrate.trapz(ys, xs)


def simpson(func, xmin: float, xmax: float, n: int = 100000) -> float:
    """Simpson公式を用いた数値積分

    Args:
        func : 被積分関数
        xmin (float): 積分区間の下端
        xmax (float): 積分区間の上端
        n (int, optional): 分割数. デフォルトは100000.

    Returns:
        float: 定積分
    """
    xs = np.linspace(xmin, xmax, n)
    ys = func(xs)

    return integrate.simps(ys, xs)


# (1)
xmin = 0
xmax = 2
print("(1)")
print(f"(ii) 中点公式: {midpoint(f, xmin, xmax)}")
print(f"(iii) 台形公式: {trapezoidal(f, xmin, xmax)}")
print(f"(iv) Simpson公式: {simpson(f, xmin, xmax)}")

# (2)
xmin = 0
xmax = np.pi / 2
print("(2)")
print(f"(ii) 中点公式: {midpoint(g, xmin, xmax)}")
print(f"(iii) 台形公式: {trapezoidal(g, xmin, xmax)}")
print(f"(iv) Simpson公式: {simpson(g, xmin, xmax)}")
