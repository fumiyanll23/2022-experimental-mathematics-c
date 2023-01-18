# 2. 手計算またはプログラムを組んで, 次の行列をLU分解せよ.
import numpy as np
import scipy

# (1)[[7,3,7], [2,2,0], [1,1,1]]
A = np.array(
    [
        [7, 3, 7],
        [2, 2, 0],
        [1, 1, 1],
    ]
)
_, L, U = scipy.linalg.lu(A)
print("(1)")
print("L:")
print(L)
print("U:")
print(U)
# (2)[[0,-1,-2], [1,0,-3], [2,3,0]]
A = np.array(
    [
        [0, -1, -2],
        [1, 0, -3],
        [2, 3, 0],
    ]
)
_, L, U = scipy.linalg.lu(A)
print("(2)")
print("L:")
print(L)
print("U:")
print(U)
# (3)[[3,2,1], [2,2,1], [1,1,1]]
A = np.array(
    [
        [3, 2, 1],
        [2, 2, 1],
        [1, 1, 1],
    ]
)
_, L, U = scipy.linalg.lu(A)
print("(3)")
print("L:")
print(L)
print("U:")
print(U)
