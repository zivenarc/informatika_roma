a = list(map(int,input().split()))
n = a[0]
m = a[1]

A = [ list(map(int, input().split())) for i in range(n)]

x = 0
y = 0
mx = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > mx:
            x = i
            y = j 
            mx = A[i][j]

print(x,y)
