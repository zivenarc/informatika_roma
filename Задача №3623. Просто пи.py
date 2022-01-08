n = int(input())

s = 1
for i in range (1, n+1):
    d = -2 * (i % 2 - 0.5)
    s += d / (2 * i + 1)

print(4*s)
