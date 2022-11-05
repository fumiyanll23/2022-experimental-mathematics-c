# written by TAGAWA, Takara
# x-cosxがsympyでは解が出せないことを示すプログラム
import sympy as sp

# 記号xを定義
sp.var("x")
K = sp.solve(x - sp.cos(x), x)
# 解を表示する(しかし表示に"解けない"と出る)
print(K)
