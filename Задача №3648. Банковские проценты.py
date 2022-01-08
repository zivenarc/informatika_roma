x = int(input())
p = int(input())
y = int(input())
a = 1 + (p / 100)
b = 0
while x < y:
    x *= a
    x = int(x)
    b += 1
print(b)