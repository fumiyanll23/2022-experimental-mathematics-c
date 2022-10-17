#必要なモジュールをインポート#tagawatakara
from numpy.linalg import solve
#連立方程式の左辺の係数を式ごとに入力
left = [[2, 3],
        [4, 5]]
#連立方程式の右辺を入力
right = [8, 14]
#解を表示（左がx,右がy）
print(solve(left, right))
