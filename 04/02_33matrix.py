# written by TAGAWA, Takara and NARITA, Fumiya
# 必要なモジュールをインポート
import numpy as np

# 3×3行列を行ごとに入力
arr = np.array([[2, 1, 1] , [1, 2, 1] , [1, 1, 2]])
# 行列を表示
print(arr)
# 固有値、固有ベクトルを計算
w, v = np.linalg.eig(arr)
# 固有値、固有ベクトルを表示
print(w)
print(v)
# 固有ベクトルが固有値4の時t(1,1,1) (tは任意定数) となり、1の時不定形となるためa(1,0,-1) + b(0,1,-1)と表現できる
