# 行列の，絶対値が最大の固有値をべき乗法で求める
import numpy as np

# (正方) 行列の行数および列数
N, M = 3, 3
# yはN次ベクトル
y = np.zeros(N)
# 許容誤差
EPS = 1.0e-6
# 行列Aの定義
A = np.array(
    [
        [11.0, 7.0, -5.0],
        [0.0, 10.0, -1.0],
        [2.0, 8.0, 3.0],
    ]
)
# xは成分がすべて1.0であるN次ベクトル
x = np.ones(N)
# 現在の計算回数
cnt = 0
# 最大計算回数
KMAX = 200
lambda1 = 10000.0
lambda2 = 10000.0
# べき乗法
for k in range(1, KMAX + 1):
    err = 0.0
    # y = Ax
    y = A @ x
    sum1 = y @ y
    sum2 = y @ x
    # レイリー商λ1 = ∥y∥ / (y, x)
    lambda1 = sum1 / sum2
    x = y / np.sqrt(sum1)
    err = abs(lambda1 - lambda2) / abs(lambda2)
    lambda2 = lambda1
    if err < EPS:
        break
    print(k, lambda1)
if cnt == KMAX:
    print("It didn't converged.")
else:
    print("It converged.")
    print(f"λ = {lambda1:.6f}")
