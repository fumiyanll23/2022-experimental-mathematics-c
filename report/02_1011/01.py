# 1. 次の方程式の厳密解を求めよ. さらに次の初期区間Ij, j = 1, 2, 3に対する2分法を用いて, 近似解を有効数字4桁で求めよ. 不適な初期区間である場合は指摘せよ.
def bisection(
    func, lower: float, upper: float, eps: float = 1e-7, iter_max: int = 100
) -> float | None:
    """二分法

    Args:
        func : 関数
        lower (float): 区間の下端
        upper (float): 区間の上端
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        float | None: 近似解 (収束しないとき ==> None)
    """
    ret = None
    for _ in range(iter_max):
        middle = (lower + upper) / 2
        if abs(func(middle)) < eps:
            ret = middle
            break
        if func(lower) * func(middle) > 0:
            lower = middle
        else:
            upper = middle

    return ret


# (1)x^2 - 2 = 0
# I1 = [0, 2], I2 = [-2, -1], I3 = [0, 1]
def f_01(x):
    return x**2 - 2


intervals = [[0, 2], [-2, -1], [0, 1]]
anss = []
for l, u in intervals:
    anss.append(bisection(f_01, l, u))
print("(1)")
for i, (interval, ans) in enumerate(zip(intervals, anss)):
    if ans:
        print(f"区間I{i + 1} = {interval}: {ans}")
    else:
        print("There are no answer in this interval.")


# (2)x^3 - 3x^2 + 2 = 0
# I1 = [0.25, 1.25], I2 = [-2, -1], I3 = [-1, 0]
def f_02(x):
    return x**3 - 3 * x**2 + 2


intervals = [[0.25, 1.25], [-2, -1], [-1, 0]]
anss = []
for l, u in intervals:
    anss.append(bisection(f_02, l, u))
print("(2)")
for i, (interval, ans) in enumerate(zip(intervals, anss)):
    if ans:
        print(f"区間I{i + 1} = {interval}: {ans}")
    else:
        print("There are no answer in this interval.")
