a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

x = []
if D > 0 :
    x.append((-b + D ** 0.5) / (2 * a))
    x.append((-b - D ** 0.5) / (2 * a))
    x.sort()
else: 
    if D == 0:
        x.append(-b / (2 * a))

print(*x)