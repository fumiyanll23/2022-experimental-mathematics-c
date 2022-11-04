# written by NARITA, Fumiya
# 必要なモジュールをインポート
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def lix(xs, i, x):
    """Lagrange補間で用いるl_i(x)関数

    Args:
        xs: x座標のリスト
        x: 変数
        i: 添え字

    Returns: l_i(x)
    """
    numerator, denominator = 1.0, 1.0
    for k in range(len(xs)):
        if k != i:
            numerator *= x - xs[k]
            denominator *= xs[i] - xs[k]

    return numerator / denominator


def lagrange(x, xs, ys):
    """Lagrange補間を用いて(n-1)次多項式を求める

    Args:
        xs: x座標のリスト
        ys: y座標のリスト

    Returns: 補間した多項式
    """
    # Lagrange補間で用いるl_i(x)を求める
    lixs = [lix(xs, i, x) for i in range(len(xs))]
    # 補間多項式を求める
    polynomial = sp.expand(np.dot(ys, lixs))

    return polynomial


# 変数xを定義する
x = sp.Symbol("x")
# x座標
xs = np.array((0.0, 0.2, 0.4, 0.6, 0.8, 1.0))
# y座標
ys = np.array((2.0, 2.12, 1.62, 2.57, 1.53, 2.0))

# Lagrange補間を用いて，6点から5次多項式を求める
polynomial = lagrange(x, xs, ys)
print(polynomial)

# 求めた多項式のグラフを描画する
xplots = np.linspace(0.0, 1.0, 100)
yplots = [polynomial.subs(x, xi) for xi in xplots]
plt.title("Lagrange interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(xs, ys, color="blue")
plt.plot(xplots, yplots, color="red")
plt.savefig("./img/lagrange.png")
plt.show()
