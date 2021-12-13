# Дан список. Не изменяя его и не используя дополнительные списки, определите, какое число в этом списке встречается чаще всего.

# Если таких чисел несколько, выведите любое из них.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 1 2 3 2 3 3
# выходные данные
# 3

a = list(map(int, input().split()))

#это задачка на метод count()

res = a[0]
max = 0
s = list(set(a)) # чтобы не перебирать все эдементы списка, ограничимся уникальными

for i in range(len(s)):
    if a.count(s[i]) > max: #считаем, сколько в исходном массиве очередных вариантов чисел
        res = s[i]

print(res)