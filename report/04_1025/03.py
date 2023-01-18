# 3. 問題2.の行列の最大固有値および最小固有値を, べき乗法・逆べき乗法を用いて求めよ.
import numpy as np


def power_method(
    mat, eigen_init: float = 1000, eps: float = 1e-10, iter_max: int = 100
) -> float | None:
    """べき乗法

    Args:
        mat : 正方行列
        eigen_init (float, optional): 固有値の初期値. デフォルトは1000.
        eps (float, optional): 許容誤差. デフォルトは1e-10.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        float | None: 絶対値最大な固有値 (収束しないとき ==> None)
    """
    ret = None
    n, _ = mat.shape
    xs = np.array([1])
    for _ in range(n - 1):
        xs = np.append(xs, np.array([0]))
    for _ in range(iter_max):
        ys = mat @ xs
        eigen_max = (ys @ ys) / (ys @ xs)
        xs = ys / np.sqrt(ys @ ys)
        if abs(eigen_max - eigen_init) / abs(eigen_init) < eps:
            ret = eigen_max
            break
        eigen_init = eigen_max

    return ret


def inverse_power_method(
    mat, eigen_init: float = 1000, eps: float = 1e-7, iter_max: int = 100
) -> float | None:
    """逆べき乗法

    Args:
        mat : 正則行列
        eigen_init (float, optional): 固有値の初期値. デフォルトは1000.
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        float | None: 絶対値最小な固有値 (収束しないとき ==> None)
    """
    ret = None
    inv_mat = np.linalg.inv(mat)
    n, _ = inv_mat.shape
    xs = np.array([1])
    for _ in range(n - 1):
        xs = np.append(xs, np.array([0]))
    for _ in range(iter_max):
        ys = inv_mat @ xs
        eigen_min = (ys @ xs) / (ys @ ys)
        xs = ys / np.sqrt(ys @ ys)
        if abs(eigen_min - eigen_init) / abs(eigen_init) < eps:
            ret = eigen_min
            break
        eigen_init = eigen_min

    return ret


# (1) [[2,-2], [-1,3]]
A = np.array(
    [
        [2, -2],
        [-1, 3],
    ]
)
print("(1)")
eigen_max = power_method(A)
print("最大固有値:")
if eigen_max:
    print(eigen_max)
else:
    print("It didn't converges :(")
eigen_min = inverse_power_method(A)
print("最小固有値:")
if eigen_min:
    print(eigen_min)
else:
    print("It didn't converges :(")

# (2) [[1,1,2], [0,1,1], [1,1,3]]
A = np.array(
    [
        [1, 1, 2],
        [0, 1, 1],
        [1, 1, 3],
    ]
)
print("(2)")
eigen_max = power_method(A)
print("最大固有値:")
if eigen_max:
    print(eigen_max)
else:
    print("It didn't converges :(")
eigen_min = inverse_power_method(A)
print("最小固有値:")
if eigen_min:
    print(eigen_min)
else:
    print("It didn't converges :(")

# (3)[[1, 1, 1], [1, 1, 0], [1, 0, 0]]
A = np.array(
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 0],
    ]
)
print("(3)")
eigen_max = power_method(A)
print("最大固有値:")
if eigen_max:
    print(eigen_max)
else:
    print("It didn't converges :(")
eigen_min = inverse_power_method(A)
print("最小固有値:")
if eigen_min:
    print(eigen_min)
else:
    print("It didn't converges :(")
