a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

#print(f'{a}x+ {b}y = {e}')
#print(f'{c}x + {d}y = {f}')

if a == 0:
    y = e / b
    x = (f - d * y) / c 
else: 
    y = f / (d + c * (e - b) / a)
    x = (e - b * y) / a

print(x, y)