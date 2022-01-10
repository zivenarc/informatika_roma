n = int(input())
a = []
b = []
for i in range(n):
    m = input()
    m = m.split()
    a.append(m[0]) 
    b.append(int(m[1]))    
k = 1 
while k > 0:
    k = 0
    for i in range(1, len(a)):
        if b[i - 1] < b[i]:
            k += 1
            a[i - 1], a[i] = a[i], a[i - 1]
            b[i - 1], b[i] = b[i], b[i - 1]     
for i in range(0, len(a)):
    print(a[i])