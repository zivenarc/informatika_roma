n = int(input())
x = float(input())
a = []
for i in range(n + 1):
    a.append(float(input()))

P = a[n]
for i in range (n-1 ,-1,-1):
        P *= x
        P += a[i]
    
print(P)
