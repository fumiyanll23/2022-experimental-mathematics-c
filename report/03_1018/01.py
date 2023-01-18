# 1. 次の連立方程式を, 手計算またはプログラム (Gaussの消去法またはヤコビ法) を組んで解け.
import numpy as np
from nptyping import Float, NDArray, Shape


def gauss_seidel(
    mat: NDArray[Shape["3, 3"], Float],
    vec: NDArray[Shape["3"], Float],
    eps: float = 1e-7,
    iter_max: int = 100,
) -> NDArray[Shape["3"], Float] | None:
    """Gauss-Seidel法

    Args:
        mat (NDArray[Shape["3, 3"], Float]): 係数行列
        vec (NDArray[Shape["3"], Float]): 定数ベクトル
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        NDArray[Shape["3"], Float] | None: 近似解 (収束しないとき ==> None)
    """
    n = len(vec)
    xs = np.zeros(n)
    xns = np.zeros(n)
    ret = None
    for _ in range(iter_max):
        err = 0
        for j in range(n):
            xns[j] = vec[j]
            for k in range(n):
                if j != k:
                    xns[j] -= mat[j][k] * xns[k]
            xns[j] /= mat[j][j]
            err += abs(xns[j] - xs[j])
        if err < eps:
            ret = xs
            break
        for j in range(n):
            xs[j] = xns[j]

    return ret


def jacobi(
    mat: NDArray[Shape["3, 3"], Float],
    vec: NDArray[Shape["3"], Float],
    eps: float = 1e-7,
    iter_max: int = 100,
) -> NDArray[Shape["3"], Float] | None:
    """Jacobi法

    Args:
        mat (NDArray[Shape["3, 3"], Float]): 係数行列
        vec (NDArray[Shape["3"], Float]): 定数ベクトル
        eps (float, optional): 許容誤差. デフォルトは1e-7.
        iter_max (int, optional): 最大反復回数. デフォルトは100.

    Returns:
        NDArray[Shape["3"], Float] | None: 近似解 (収束しないとき ==> None)
    """
    n = len(vec)
    xs = np.zeros(n)
    xns = np.zeros(n)
    ret = None
    for _ in range(iter_max):
        err = 0
        for j in range(n):
            xns[j] = vec[j]
            for k in range(n):
                if j != k:
                    xns[j] -= mat[j][k] * xs[k]
            xns[j] /= mat[j][j]
            err += abs(xns[j] - xs[j])
        if err < eps:
            ret = xs
            break
        for j in range(n):
            xs[j] = xns[j]

    return ret


# (1){3x1+x2+2x3 = 13, 5x1+x2+3x3 = 20, 4x1+2x2+x3 = 13}
ass = np.array(
    [
        [3, 1, 2],
        [5, 1, 3],
        [4, 2, 1],
    ]
)
bs = np.array([13, 20, 13])
vs = ["x1", "x2", "x3"]
anss_gauss = gauss_seidel(ass, bs)
anss_jacobi = jacobi(ass, bs)
print("(1)")
print("Gauss-Seidel法:")
if anss_gauss is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_gauss):
        print(f"{v} = {ans}")
print("Jacobi法:")
if anss_jacobi is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_jacobi):
        print(f"{v} = {ans}")

# (2){3x1+12x2+9x3 = 3, 2x1+5x2+4x3 = 4, -x1+3x2+2x3 = 5}
ass = np.array(
    [
        [3, 12, 9],
        [2, 5, 4],
        [-1, 3, 2],
    ]
)
bs = np.array([3, 4, 5])
vs = ["x1", "x2", "x3"]
anss_gauss = gauss_seidel(ass, bs)
anss_jacobi = jacobi(ass, bs)
print("(2)")
print("Gauss-Seidel法:")
if anss_gauss is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_gauss):
        print(f"{v} = {ans}")
print("Jacobi法:")
if anss_jacobi is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_jacobi):
        print(f"{v} = {ans}")

# (3){x2+2x3 = -1, x1-3x3 = 2, 2x1+3x2 = 1}
ass = np.array(
    [
        [0, 1, 2],
        [1, 0, -3],
        [2, 3, 0],
    ]
)
bs = np.array([-1, 2, 1])
vs = ["x1", "x2", "x3"]
anss_gauss = gauss_seidel(ass, bs)
anss_jacobi = jacobi(ass, bs)
print("(3)")
print("Gauss-Seidel法:")
if anss_gauss is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_gauss):
        print(f"{v} = {ans}")
print("Jacobi法:")
if anss_jacobi is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_jacobi):
        print(f"{v} = {ans}")

# (4){2x1+x2+x3 = 3, x1+2x2+x3 = 2, x1+x2+2x3 = 6}
ass = np.array(
    [
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
    ]
)
bs = np.array([3, 2, 6])
vs = ["x1", "x2", "x3"]
anss_gauss = gauss_seidel(ass, bs)
anss_jacobi = jacobi(ass, bs)
print("(4)")
print("Gauss-Seidel法:")
if anss_gauss is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_gauss):
        print(f"{v} = {ans}")
print("Jacobi法:")
if anss_jacobi is None:
    print("It didn't converged.")
else:
    for v, ans in zip(vs, anss_jacobi):
        print(f"{v} = {ans}")
