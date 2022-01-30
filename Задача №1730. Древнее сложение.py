def maya2dec(s):
    res = 0
    razr = s.split()
    for i in range(len(razr)):
        m = 0
        for j in range(len(razr[i])):
            if razr[i][j] == '|':
                m += 5
            elif razr[i][j] == '.':
                m += 1 
            elif razr[i][j] == '*':
                m += 0
            else:
                return ('error')
        res += 20 ** (len(razr) - i - 1) * m 
    return res
    
def dec2maya(n):
    res = []
    k = []
    for i in range(8,-1,-1):
        razr = n // 20 ** i
        if (len(k) != 0 or razr != 0):
            k.append(n // 20 ** i)
        n -= 20 ** i * razr
    
    for i in range(len(k)):
        s = '' 
        razr = k[i]
        s += '|' * (razr // 5)
        s += '.' * (razr % 5)
        res.append(s[::-1])
    
    return(' '.join(res))
    
a = input()
b = input()

print (dec2maya(maya2dec(a) + maya2dec(b)))
