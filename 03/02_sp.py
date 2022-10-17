# written by NARITA, Fumiya
# 連立方程式{x+2y=8, 2x+4y=16}をSympyで解く
# 必要なモジュールをインポートする
import sympy as sp


# 変数を定義する
x = sp.Symbol("x")
y = sp.Symbol("y")

# 方程式を多項式として定義する
eq_01 = x + 2*y - 8
eq_02 = 2*x + 4*y - 16

# 連立方程式を解く。ただし、特異行列 (非正則行列) なので不定である
anss = sp.solve([eq_01, eq_02], [x, y])
for k, v in anss.items():
    print(f"{k} = {v}")
