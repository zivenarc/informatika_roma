a = int(input())
b = int(input())
c = int(input())
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print(0)
else:
    p = (a + b + c) / 2.0
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)