# Задача №111159. Создание архива
# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.

# Известно, какой объем занимают файлы каждого пользователя.

# Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске определит максимальное число пользователей, чьи данные можно поместить в архив, при этом используя свободное место как можно более полно.

# Входные данные
# Программа получает на вход в одной строке число S – размер свободного места на диске (натуральное, не превышает 10000), и число N – количество пользователей (натуральное, не превышает 100), после этого идет N чисел - объем данных каждого пользователя (натуральное, не превышает 1000), записанных каждое в отдельной строке.

# Выходные данные
# Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.

# Примеры
# входные данные
# 100 2
# 200
# 50
# выходные данные
# 1
# входные данные
# 100 3
# 50
# 30
# 50
# выходные данные
# 2

a, b = map(int, input().split())
arc = []
for i in range (b):
    arc.append(int(input()))
    
s = 0 
arc.sort()
for i in range(len(arc)):
    if s > a:
        break
    s += arc[i]

print(i)  