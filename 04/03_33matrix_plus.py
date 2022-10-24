#必要なモジュールをインポート
import numpy
import numpy.linalg as LA
#3✖️3行列を行ごとに入力
arr = numpy.array([[1, 1, 0] , [1, 0, 1] , [1, -1, -1]])
#行列を表示
print(arr)
#固有値、固有ベクトルを計算
w, v = LA.eig(arr)
#固有値、固有ベクトルを表示
print(w)
print(v)
#pythonでは複素数表現で用いられる虚数iがjとして表現されることに注意
