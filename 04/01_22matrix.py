# written by TAGAWA, Takara and NARITA, Fumiya
# 必要なモジュールをインポート
import numpy as np

# 2×2正方行列を定義
a = np.array([[2, -2], [-1, 3]])

# aの固有値と固有ベクトル
# インデクス0に固有値、インデクス1に固有ベクトルが格納される
a_eig = np.linalg.eig(a)

# 固有値を表示
print("固有値 {}".format(a_eig[0]))

# 固有ベクトルを表示
print("固有ベクトル {}".format(a_eig[1]))
# (-0.89442719,-0.4472136)が固有値1に、(0.70710678,-0.70710678)が固有値4に対応する
