# written by TAGAWA, Takara
#3x-1=0の解を分数表示するプログラム
import sympy
# 記号xを定義
sympy.var('x')
# 3x -1 = 0 をxについて解く
s = sympy.solve( 3*x- 1, x)
#解を表示する
print(s)
