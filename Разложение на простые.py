
# Задача №4182. Разложение на простые
# Дано натуральное число N>1. Выведите все его простые натуральные делители с учетом кратности. Алгоритм должен иметь сложность O(n−−√).

# Входные данные
# Вводится натуральное число N≤2∗109.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 12
# выходные данные
# 2 2 3 

def IsPrime(n): #Определим функцию проверки простого числа чтобы дважды код не переписывать
    d = 2
    if n != int(n):
        return False
        
    while n % d != 0:
        d += 1
    return d == n

a = list(map(int, input().split()))[0]
res = []

if (IsPrime(a)):
    res.append(a)
else:
    b = 2
    if a % b == 0:
        res.append(b)
    
    while not(IsPrime(a / b)):
        while not((IsPrime(b)) and (a % b == 0)):
            b += 1
        res.append(b)
        a = int(a / b)
        b = 2
        if (a == 1):
            break
    
    
    if (a != 1):    
        res.append(int(a / b))
print(*res)


