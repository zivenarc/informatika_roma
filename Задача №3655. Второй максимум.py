a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
 
a.sort()
a.pop()

print(a.pop())