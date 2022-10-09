# written by NARITA, Fumiya
# 2次方程式2x^2-6x+3 = 0をSympyで解く
# 必要なモジュールをインポートする
import sympy as sp


# 変数xを定義する
x = sp.symbols("x")

# 2次方程式ax^2+bx+c = 0の各係数を設定する
a, b, c = 2, -6, 3

# 2次方程式を解く
anss = sp.solve(a*x**2 + b*x + c, x)

# 1. 2つの解を数値計算で求める
for i in range(len(anss)):
    # メソッドevalf()を用いて解を小数で表す
    print(f"{anss[i]} = {anss[i].evalf()}")

# 2. 大きい方の解を数値計算で求め，小さい方の解を解と係数の関係から求める
large = anss[1]
small = -(b/a) - large
print(f"{small} = {small.evalf()}")
print(f"{large} = {large.evalf()}")

# 小さい方の解の求め方による差異を確認する
print(f"(数値計算で求めた解) - (解と係数の関係から求めた解) = {anss[0].evalf() - small.evalf()}")
