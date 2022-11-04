#Written by TAGAWATakara
#必要なモジュールをインポート
import numpy as np #np.dot(x, y) xyの内積をとる関数。
import matplotlib.pyplot as plt
#座標をx、yそれぞれベクトルとして定義
x = np.array([0.0,0.2,0.4,0.6,0.8,1.0]) # 内積計算のためにnp.arrayで作る。
y = np.array([2.0,2.12,1.62,2.57,1.53,2.0])

#計算内容を関数として定義
def reg1dim(x, y):
    n = len(x)
    a = ((np.dot(x, y)- y.sum() * x.sum()/n)/
        ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum())/n
    return a, b
#計算結果をabとして入れ込む
a, b = reg1dim(x, y)
#y=ax+bのパラメータabを表示
print(a,b)
#グラフを描画
plt.scatter(x, y, color="k")
plt.plot([0, x.max()], [b, a * x.max() + b]) #(0, b)地点から(xの最大値,ax + b)地点までの線
plt.show()
