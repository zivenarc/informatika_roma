n = int(input())
x = float(input())

s = 1
xn = 1
f = 1
for i in range (1, n + 1):
    d = -2 * (i % 2 - 0.5)
    xn *= x * x
    f *= 2 * i * (2 * i - 1)
    s += d * xn / f

print(s)
