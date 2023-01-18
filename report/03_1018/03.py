# 3. 次の行列を対角化することにより, 正定値であることを証明せよ.
import numpy as np

# (1)[[2,1,1], [1,2,1], [1,1,2]]
A = np.array(
    [
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
    ]
)
eigen_values = np.linalg.eig(A)[0]
print("(1)")
if eigen_values.all() > 0:
    print("This matrix is positive definite.")
    print(f"固有値: {eigen_values}")
else:
    print("The matrix isn't positive definite.")


# (2)[[3,2,1], [2,2,1], [1,1,1]]
A = np.array(
    [
        [3, 2, 1],
        [2, 2, 1],
        [1, 1, 1],
    ]
)
eigen_values = np.linalg.eig(A)[0]
print("(2)")
if eigen_values.all() > 0:
    print("This matrix is positive definite.")
    print(f"固有値: {eigen_values}")
else:
    print("The matrix isn't positive definite.")
