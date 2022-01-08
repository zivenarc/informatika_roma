a = []
m = 0
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
    if len(a) >1 and a[len(a)-1] > a[len(a)-2]:
        m += 1
    
print(m)