a = []
m = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > m:
        m = n
    
print(m)