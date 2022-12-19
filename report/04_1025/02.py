# 2. 次の行列の固有値・固有ベクトルを求めよ.
# 参考文献:
# - note.nkmk.me/Python, NumPyで行列の演算（逆行列、行列式、固有値など） (https://note.nkmk.me/python-numpy-matrix/)
# - NumPy/numpy.linalg.eig (https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
import numpy as np


def get_eigen_pairs(mat) -> list[tuple[float, list[float]]]:
    """固有値および対応する固有ベクトルを求める

    Args:
        mat : 行列

    Returns:
        list[tuple[float, list[float]]]: 固有値および対応する固有ベクトル
    """
    vals, vecs = np.linalg.eig(mat)
    eigen_pairs = []
    for i, val in enumerate(vals):
        normarized_vec = vecs[:, i] / np.min(np.abs(vecs[:, i][vecs[:, i] != 0]))
        eigen_pairs.append((val, normarized_vec))

    return eigen_pairs


# (1) [[2,-2], [-1,3]]
A = np.array([
    [2,-2],
    [-1,3],
])
eigen_paris = get_eigen_pairs(A)
print("(1)")
for val, vec in eigen_paris:
    print(f"固有値: {val}, 固有ベクトル: {vec}")

# (2) [[1,1,2], [0,1,1], [1,1,3]]
A = np.array([
    [1,1,2],
    [0,1,1],
    [1,1,3],
])
eigen_paris = get_eigen_pairs(A)
print("(2)")
for val, vec in eigen_paris:
    print(f"固有値: {val}, 固有ベクトル: {vec}")

# (3) [[1,1,1], [1,1,0], [1,0,0]]
A = np.array([
    [1,1,1],
    [1,1,0],
    [1,0,0],
])
eigen_paris = get_eigen_pairs(A)
print("(3)")
for val, vec in eigen_paris:
    print(f"固有値: {val}, 固有ベクトル: {vec}")
