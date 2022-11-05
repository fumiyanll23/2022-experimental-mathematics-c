# sympyをインポート#tagawatakara
import sympy as sp

# 変数x,yを定義
x = sp.Symbol("x")
y = sp.Symbol("y")
# それぞれの方程式の右辺を移項した式を入力
equation1 = 2 * x + 1 * y - 7
equation2 = 6 * x + 3 * y - 15
# 解を表示
print(sp.solve([equation1, equation2]))
# 解なしであれば空白のリストが表示される
