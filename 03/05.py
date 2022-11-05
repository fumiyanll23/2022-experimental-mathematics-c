# 必要なモジュールをインポート#tagawatakara
import numpy as np

# 連立方程式の左辺の係数を式ごとに入力
left = [[9, 2, 1, 1], [2, 8, -2, 1], [-1, -2, 7, -2], [1, -1, -2, 6]]

# 連立方程式の右辺を入力
right = [20, 16, 8, 17]
# 解を表示（左からx,y,z,w）
print(np.linalg.solve(left, right))
