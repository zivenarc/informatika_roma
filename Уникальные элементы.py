# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 1 2 2 3 3 3
# выходные данные
# 1

a = list(map(int, input().split()))
res = []

for i in range(0,len(a)):
    uniqueTest = True #сначала предположим, что этот элемент уникальный
    for j in range (0,len(a)): 
        if (a[i] == a[j]) and (i != j): #если элемент такой же, но не он
            uniqueTest = False #тест на уникальность провален
            break #если у числа есть пара, прервать цикл, дальнейший перебор не имеет смысла
    if (uniqueTest):
        res.append(a[i]) #если тест на уникальность пройден, добавляем элемент в результат

print(*res)
        