# 常微分方程式の初期値問題をHeun法で解く
import math


# 関数f(t, x)の定義
def f(t, x):
    return 3 * x


# 微分方程式の厳密解
def exact(t):
    return math.exp(3 * t)


N = 20
# tは(N+1)個の成分を持つベクトル (数列)
t = [0] * (N + 1)
# xは(N+1)個の成分を持つベクトル (数列)
x = [0] * (N + 1)
# 時間の刻み幅
h = 0.1
# 初期時刻
t[0] = 0.0
# 初期条件
x[0] = 1.0
# Heun法
for n in range(N):
    t[n + 1] = t[n] + h
    s1 = f(t[n], x[n])
    x[n + 1] = x[n] + h * (s1 + f(t[n] + h, x[n] + h * s1)) / 2
    print(f"t(n): {t[n]:.2f}, calculated: {x[n]:.6f}, exact: {exact(t[n]):.6f}")
