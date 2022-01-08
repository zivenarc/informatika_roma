n = int(input())
a = int(input())

s = n * a
for i in range (n-1, 0, -1):
    s = s ** 0.5
    s += i * a

    
print(s**0.5)
