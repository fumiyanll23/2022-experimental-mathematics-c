# written by NARITA, Fumiya
# 連立方程式{x^2+y^2=1, 4x+3y=5}をSympyで解く
# 必要なモジュールをインポートする
import sympy as sp


# 変数を定義する
x = sp.Symbol("x")
y = sp.Symbol("y")

# 方程式を多項式として定義する
eq_01 = x**2 + y**2 - 1
eq_02 = 4*x + 3*y - 5

# 連立方程式を解く
anss = sp.solve([eq_01, eq_02], [x, y])
print(f"x = {anss[0][0]}")
print(f"y = {anss[0][1]}")
