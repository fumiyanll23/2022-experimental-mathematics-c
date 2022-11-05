# sympyをインポート#tagawatakara
import sympy as sp

# 変数x,yを定義
x = sp.Symbol("x")
y = sp.Symbol("y")
# それぞれの方程式の右辺を移項した式を入力
equation1 = x**2 + y**2 - 1
equation2 = -sp.sin(x) + y
# 解を表示
print(sp.solve([equation1, equation2]))
# 代数的には解けないためsympyだとエラーが出る
