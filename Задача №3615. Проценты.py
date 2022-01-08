P = int(input())
X = int(input())
Y = int(input())

a = (100 + P) * (X * 100 + Y) / 100
r = int(a // 100)
k = int(a % 100)

print(r,k)