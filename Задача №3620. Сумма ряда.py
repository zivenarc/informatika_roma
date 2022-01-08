n = int(input())

s = 0
for x in range(n):
    s += 1 / ((x + 1) ** 2)
    
print(s)
