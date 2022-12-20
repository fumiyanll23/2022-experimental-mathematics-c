# 4. 次の3点を通るラグランジュ補間多項式関数P2(x)を求めよ. さらに(5, 4)を通るラグランジュ補間多項式関数P3(x)を求めよ.
import numpy as np
from scipy import interpolate

xys = np.array(
    [
        [0, 5],
        [1, 8],
        [3, 11],
    ]
)
xs = np.array([x for x, _ in xys])
ys = np.array([y for _, y in xys])
P2 = interpolate.lagrange(xs, ys)
print("P2(x):")
print(P2)
additional_point = np.array([[5, 4]])
new_xys = np.append(xys, additional_point, axis=0)
new_xs = np.array([x for x, _ in new_xys])
new_ys = np.array([y for _, y in new_xys])
P3 = interpolate.lagrange(new_xs, new_ys)
print("P3(x):")
print(P3)
