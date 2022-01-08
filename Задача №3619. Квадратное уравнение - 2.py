a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if a == 0:
    if b == 0:
        if c==0:
            print(3)
        else:
            print(0)
    else:
        x = -c / b
        print (1,x)
else:
    x = []
    if D > 0 :
        x.append((-b + D ** 0.5) / (2 * a))
        x.append((-b - D ** 0.5) / (2 * a))
        x.sort()
    else: 
        if D == 0:
            x.append(-b / (2 * a))
    
    print(len(x),*x)