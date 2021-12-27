# Задача №111307. Нижний регистр
# Дана строка, возможно, содержащая пробелы. Считайте эту строку и переведите все символы этой строки в нижний регистр. Решение оформите в виде функции ToLower (S), получающей в качестве параметра строку и возвращающую новую строку.

# Для перевода одного символа в нижний регистр напишите отдельную функцию.

# Примеры
# входные данные
# Hello, world!
# выходные данные
# hello, world!

def symbolToLower(a):
    offset=ord("a")-ord("A")
    if ord("A") <= ord(a) <= ord("Z"):
        return(chr(ord(a)+offset))
    return(a)
    
def ToLower(S):
    res = ""
    for i in range(len(S)):
        res += symbolToLower(S[i])
    return(res)
    
s = input()
print(ToLower(s))