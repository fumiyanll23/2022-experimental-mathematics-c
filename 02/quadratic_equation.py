# written by NARITA, Fumiya
# 2次方程式2x^2-6x+3 = 0をSympyで解く
# 必要なモジュールをインポートする
import sympy as sp


# 変数xを定義する
x = sp.symbols("x")

# 2次方程式を解く
anss = sp.solve(2*x**2 - 6*x + 3, x)

for i in range(len(anss)):
    # メソッドevalf()を用いて解を小数で表す
    print(f"{anss[i]} = {anss[i].evalf()}")
