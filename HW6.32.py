# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

a = list(map(int, input('Введите массив: ').split()))

minimum = int(input('Min: '))
maximum = int(input('Max: '))
print(*[i for i in range(len(a)) if minimum <= a[i] <= maximum]) 