n = int(input())

s = 0
for x in range (1, n+1):
    d = 2 * (x % 2 - 0.5)
    s += d / x
    
print(s)
