# written by NARITA, Fumiya
# 連立方程式{x+2y=8, 2x+4y=16}をNumpyで解く
# 必要なモジュールをインポートする
import numpy as np


# 係数行列とベクトルを用意する
Ass = np.array([
    [1, 2],
    [2, 4],
    ])
bs = np.array([8, 16])

# 連立方程式を解く
anss = np.linalg.solve(Ass, bs)
print(f"(x, y) = {anss}")
