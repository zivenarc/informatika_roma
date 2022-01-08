P = int(input())
X = int(input())
Y = int(input())
K = int(input())

for i in range(K):
    a = X * 100 + Y
    a = (100 + P) * a / 100
    X = int(a // 100)
    Y = int(a % 100)

print(X,Y)