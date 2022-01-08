a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
 
s = sum(a)/len(a)
v = 0
for i in range(len(a)):
    v += (a[i] - s) ** 2
    
v /= (len(a) - 1)
v = v ** 0.5

print(v)