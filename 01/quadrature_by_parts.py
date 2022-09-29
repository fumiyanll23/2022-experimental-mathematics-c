# 円周率の近似値を区分求積法 (最小値) を用いて求める
# 必要なモジュールをインポートする
import math


# 被積分関数f(x) = √(1-x^2)を定義する
def f(x: float) -> float:
    return math.sqrt(1 - x*x)


# 微小区間の幅 (小さくするほど精度が高くなる)
step = 0.01
