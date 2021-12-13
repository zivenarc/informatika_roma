distance = list(map(int, input().split()))
price = list(map(int, input().split()))
# Cортировка стандартными методами Питона. Если нельзя, можно так же, как в предыдущих задачах на сортировку
distance.sort()
price.sort(reverse=True)
# Умножаем самые короткие расстояния на самые высокие ставки, и наоборот
for i in range(0,len(distance)):
    total += distance[i] * price [i]
    
print (total)
