# written by TAGAWA, Takara
# 3x-1=0の解を小数表示するプログラム
# numpyをインストール
import numpy as np

# 与えられた方程式の係数から解を求める
print(np.roots([3, -1])[0])
# n次方程式にならばその分リストの数が増えることになる
