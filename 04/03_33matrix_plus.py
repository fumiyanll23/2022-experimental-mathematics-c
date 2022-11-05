# written by TAGAWA, Takara and NARITA, Fumiya
# 行列[[1,1,0], [1,0,1], [1,-1,-1]]の固有値・固有ベクトルを求める
# 必要なモジュールをインポート
import numpy as np

# 3×3行列を行ごとに入力
arr = np.array([[1, 1, 0], [1, 0, 1], [1, -1, -1]])
# 行列を表示
print(arr)
# 固有値、固有ベクトルを計算
w, v = np.linalg.eig(arr)
# 固有値、固有ベクトルを表示
print(w)
print(v)
# pythonでは複素数表現で用いられる虚数iがjとして表現されることに注意
