a, b = map(int, input().split())
s = sorted([int(input()) for i in range(b)])
n = 0
for i in range(len(s)):
    a -= s[i]
    if a >= 0:
        n += 1
print(n)