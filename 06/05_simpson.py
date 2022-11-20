# Written by NARITA, Fumiya
# 定積分∫_{0}^{1} x^3 dx (= 1/4)をSimpsonの公式を用いて解く
# 被積分関数を定義する
def f(x: float) -> float:

    return x**3


# 積分区間の下端と上端を設定する
a, b = 0, 1
# 分割数を設定する
n = 10000000000
# Simpsonの公式を用いて定積分を求める
ans = (b-a) * (f(a) + 4*f((a+b)/2) + f(b)) / 6
print(ans)
