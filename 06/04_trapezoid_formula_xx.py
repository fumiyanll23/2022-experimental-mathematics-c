#x^2の定積分を台形公式を用いて求めるプログラム#Written by Takaratagawa
#被積分関数を定義
def f(x):
    return x**2

#区間を何等分するかを設定
N = 10**6

a = 0 #積分範囲の下端
b = 1 #積分範囲の上端
h = (b-a)/N #積分区間をN等分した微小区間の定義

#台形公式の計算
S = (h/2) * (f(a) + 2*sum(f(h*i) for i in range(1,N-1)) + f(b))

#近似値の表示
print(S)
