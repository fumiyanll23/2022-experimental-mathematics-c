# 円周率の近似値を台形公式を用いて求める
# 必要なモジュールをインポートする
import math


# 被積分関数f(x) = √(1-x^2)を定義する
def f(x: float) -> float:
    return math.sqrt(1 - x*x)


# 分割数 (大きくするほど精度が高くなる)
n = 1000000

total = 0
for k in range(1, n+1):
    total += f((k-1) / n) + f(k / n)

print(2 * total / n)