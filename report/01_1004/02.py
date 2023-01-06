# 2. 次の計算をせよ.
import numpy as np

# (1)
A = np.array([
    [2, 1, 4],
    [1, 1, 2],
    [0, 7, 3],
])
B = np.array([
    [2, 4, 1],
    [2, 3, 0],
    [3, 1, 2],
])
C = np.array([
    [5, 3, 0],
    [8, 6, 2],
    [2, 0, 1],
])
print("(1)")
print(A @ (3*B) @ ((-2)*C))

# (2)
A = np.array([
    [1, 3, 2],
    [0, 1, 5],
])
B = np.array([
    [1, 0],
    [4, 1],
    [-3, 2],
])
print("(2)")
print(A @ B)
4
# (3)
A = np.array([
    [1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3)],
    [1/np.sqrt(2), 1/np.sqrt(2), 0],
    [1/np.sqrt(6), 1/np.sqrt(6), -2/np.sqrt(6)]
])
B = np.array([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2],
])
C = np.array([
    [1/np.sqrt(3), 1/np.sqrt(2), 1/np.sqrt(6)],
    [1/np.sqrt(3), -1/np.sqrt(2), 1/np.sqrt(6)],
    [1/np.sqrt(3), 0, -2/np.sqrt(6)],
])
print("(3)")
print(A @ B @ C)

# (4)
A = np.array([
    [-3/4, 1/2, 1/4],
    [1/2, -1/3, 1/6],
    [1/4, 1/6, -1/12],
])
B = np.array([1, 2, 1])
print("(4)")
print(A @ B)

# (5)
A = np.array([3, 2, 1])
B = np.array([4, -3, 5])
print("(5)")
print(A @ B)
