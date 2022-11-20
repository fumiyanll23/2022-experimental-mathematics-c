# Written by Takaratagawa and NARITA, Fumiya
# sin_pi*xの定積分を求めるプログラム
# 必要なモジュールをインポート
import sympy as sp

# 変数xを定義
x = sp.Symbol('x')

# 積分の対象となる式
expr = sp.sin(sp.pi*x)

# 不定積分を求める
ans1 = sp.integrate(expr,x)

# 定積分を求める（積分範囲まで指定する）
ans2 = sp.integrate(expr, (x, 0, 1))

# 計算結果
print("不定積分の結果：", ans1)
print("定積分の結果：", ans2)
