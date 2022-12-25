# 非線型2元連立方程式の解をNewton法を用いて求める
import math


def f(X, Y):
    return X**2 + Y**2 - 1


def g(X, Y):
    return math.sin(X) - Y


# 関数fのx偏微分
def fx(X, Y):
    return 2.0 * X


# 関数gのx偏微分
def gx(X, Y):
    return math.cos(X)


# 関数fのy偏微分
def fy(X, Y):
    return 2.0 * Y


# 関数gのy偏微分
def gy(X, Y):
    return -1.0


# 初期条件
X0 = 1.0
Y0 = 0.0
# 許容誤差
EPS = 1e-7
# 現在の計算回数
cnt = 0
# 最大計算回数
IMAX = 50
# Newton法
for i in range(IMAX):
    J = fx(X0, Y0) * gy(X0, Y0) - fy(X0, Y0) * gx(X0, Y0)
    DX = (-f(X0, Y0) * gy(X0, Y0) + fy(X0, Y0) * g(X0, Y0)) / J
    DY = (f(X0, Y0) * gx(X0, Y0) - fx(X0, Y0) * g(X0, Y0)) / J
    X0 += DX
    Y0 += DY
    if f(X0, Y0) < EPS and g(X0, Y0) < EPS:
        break
    print(i + 1, X0, Y0)
if cnt == IMAX:
    print("It didn't converged.")
else:
    print("It converged.")
    print(f"X = {X0:.7f}, Y = {Y0:.7f}")
