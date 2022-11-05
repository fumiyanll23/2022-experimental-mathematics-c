# written by TAGAWA, Takara and NARITA, Fumiya
# 3x-1=0の解を分数表示するプログラム
import sympy as sp

# 記号xを定義
sp.var("x")
# 3x -1 = 0 をxについて解く
s = sp.solve(3 * x - 1, x)
# 解を表示する
print(s)
