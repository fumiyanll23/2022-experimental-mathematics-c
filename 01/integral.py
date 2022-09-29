# 円周率の近似値を積分を用いて求める
# 必要なモジュールをインポートする
import sympy as sp


# 変数xを定義する
x = sp.symbols("x")

# 被積分関数f(x) = √(1-x^2)を定義する
f = sp.sqrt(1 - x*x)

# f(x)を区間[0, 1]で積分する
print(4 * sp.integrate(f, (x, 0, 1)))
