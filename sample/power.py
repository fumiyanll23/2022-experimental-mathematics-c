# 行列の，絶対値が最大の固有値をべき乗法で求める
import numpy as np

# (正方) 行列の行数および列数
N, M = 3, 3
# yはN次ベクトル
y = np.zeros(N)
# 許容誤差
EPS = 1.0e-6
# 行列Aの定義
a = np.array(
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
    for i in range(N):
        y[i] = 0.0
        for j in range(N):
            y[i] += a[i][j] * x[j]
    sum1 = 0.0
    sum2 = 0.0
    # レイリー商λ1 = ∥y∥ / (y, x)
    for i in range(N):
        sum1 += y[i] * y[i]
        sum2 += y[i] * x[i]
        lambda1 = sum1 / sum2
    for i in range(N):
        x[i] = y[i] / np.sqrt(sum1)
    err = abs(lambda1 - lambda2) / abs(lambda2)
    lambda2 = lambda1
    if err < EPS:
        break
    print(k, lambda1)
if cnt == KMAX:
    print("It didn't converged.")
else:
    print("It converged.")
    print(f"λ = {lambda1:10.6f}")
