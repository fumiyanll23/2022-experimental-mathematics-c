# 4元連立方程式の解をJacobi法を用いて求める
import numpy as np

# 標準出力に関する設定
np.set_printoptions(precision=7, floatmode="fixed", suppress=True)
# 変数のリスト
vs = ["x", "y", "z", "w"]
# 許容誤差
EPS = 1e-7
# 現在の計算回数
cnt = 0
# 最大計算回数
IMAX = 50
# 4元連立方程式
N = 4
# 行列Aの定義
A = np.array(
    [
        [9.0, 2.0, 1.0, 1.0],
        [2.0, 8.0, -2.0, 1.0],
        [-1.0, -2.0, 7.0, -2.0],
        [1.0, -1.0, -2.0, 6.0],
    ]
)
# 定ベクトルbの定義
B = np.array([20.0, 16.0, 8.0, 17.0])
# 未知ベクトルxの定義
X = np.zeros(N)
# xを更新したベクトルの定義
XN = np.zeros(N)
# Jacobi法
for i in range(IMAX):
    err = 0.0
    for j in range(N):
        XN[j] = B[j]
        for k in range(N):
            if j != k:
                XN[j] -= A[j][k] * X[k]
        XN[j] /= A[j][j]
        err += abs(XN[j] - X[j])
    if err < EPS:
        break
    cnt += 1
    for j in range(N):
        X[j] = XN[j]
    print(i, X)
if cnt == IMAX:
    print("It did not converged.")
else:
    print("It converged.")
    for v, x in zip(vs, X):
        print(f"{v} = {x}")
