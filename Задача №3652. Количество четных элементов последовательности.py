a = []
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        a.append(n)
    
print(len(a))