# written by NARITA, Fumiya
# 連立方程式{3x_1+x_2+2x_3=13, 5x_1+x_2+3x_3=20, 4x_1+2x_2+x_3=13}をSympyで解く
# 必要なモジュールをインポートする
import sympy as sp

# 変数を定義する
x = sp.Symbol("x_1")
y = sp.Symbol("x_2")
z = sp.Symbol("x_3")

# 方程式を多項式として定義する
eq_01 = 3 * x + y + 2 * z - 13
eq_02 = 5 * x + y + 3 * z - 20
eq_03 = 4 * x + 2 * y + z - 13

# 連立方程式を解く
anss = sp.solve([eq_01, eq_02, eq_03], [x, y, z])
for k, v in anss.items():
    print(f"{k} = {v}")
