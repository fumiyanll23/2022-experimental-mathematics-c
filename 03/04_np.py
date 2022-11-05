# written by NARITA, Fumiya
# 連立方程式{3x_1+x_2+2x_3=13, 5x_1+x_2+3x_3=20, 4x_1+2x_2+x_3=13}をNumpyで解く
# 必要なモジュールをインポートする
import numpy as np

# 係数行列とベクトルを用意する
Ass = np.array(
    [
        [3, 1, 2],
        [5, 1, 3],
        [4, 2, 1],
    ]
)
bs = np.array([13, 20, 13])

# 連立方程式を解く
anss = np.linalg.solve(Ass, bs)
print(f"(x, y, z) = {anss}")
