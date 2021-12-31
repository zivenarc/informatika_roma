n = float(input())
c = (n % 1)
if c >= 0.5:
    print(int(n // 1)+1)
else:
    print(int(n // 1))