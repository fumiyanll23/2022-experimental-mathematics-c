# 2階線型常微分方程式の初期値問題をRunge-Kutta法で解く
import math


# 関数f1(t, x)の定義
def f1(t, x1, x2):
    return x2


# 関数f2(t, x)の定義
def f2(t, x1, x2):
    return -2.0 * x1 + 3.0 * x2


# 微分方程式の厳密解x1
def x1exact(t):
    return math.exp(t) + math.exp(2.0 * t)


# 微分方程式の厳密解x2．つまり，x1の導関数
def x2exact(t):
    return math.exp(t) + 2.0 * math.exp(2.0 * t)


N = 20
# tは(N+1)個の成分を持つベクトル (数列)
t = [0] * (N + 1)
# x1は(N+1)個の成分を持つベクトル (数列)
x1 = [0] * (N + 1)
# x2は(N+1)個の成分を持つベクトル (数列)
x2 = [0] * (N + 1)
# 時間の刻み幅
h = 0.1
# 初期時刻
t[0] = 0.0
# 初期条件
x1[0] = 2.0
# 初期条件
x2[0] = 3.0
for n in range(N):
    t[n + 1] = t[n] + h
    s1x1 = f1(t[n], x1[n], x2[n])
    s1x2 = f2(t[n], x1[n], x2[n])
    s2x1 = f1(t[n] + h / 2, x1[n] + s1x1 * h / 2, x2[n] + s1x2 * h / 2)
    s2x2 = f2(t[n] + h / 2, x1[n] + s1x1 * h / 2, x2[n] + s1x2 * h / 2)
    s3x1 = f1(t[n] + h / 2, x1[n] + s2x1 * h / 2, x2[n] + s2x2 * h / 2)
    s3x2 = f2(t[n] + h / 2, x1[n] + s2x1 * h / 2, x2[n] + s2x2 * h / 2)
    s4x1 = f1(t[n] + h, x1[n] + s3x1 * h, x2[n] + s3x2 * h)
    s4x2 = f2(t[n] + h, x1[n] + s3x1 * h, x2[n] + s3x2 * h)
    x1[n + 1] = x1[n] + h * (s1x1 + 2 * s2x1 + 2 * s3x1 + s4x1) / 6
    x2[n + 1] = x2[n] + h * (s1x2 + 2 * s2x2 + 2 * s3x2 + s4x2) / 6
    print(
        f"t(n): {t[n]:.2f}, xの近似値: {x1[n]:.6f}, xの厳密値: {x1exact(t[n]):.6f}, Dxの近似値: {x2[n]:.6f}, Dxの厳密値: {x2exact(t[n]):.6f}"
    )
