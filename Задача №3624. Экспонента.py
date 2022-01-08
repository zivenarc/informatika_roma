n = int(input())
x = float(input())

s = 1
xn = 1
f = 1
for i in range (1, n+1):
    xn *= x
    f *= i
    s += xn / f

print(s)
