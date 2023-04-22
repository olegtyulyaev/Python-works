# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

#*Пример:*
# 5
#  1 2 3 4 5
#   6
#   -> 5

from random import randint
N = int(input("Введите колчиство элементов N для массива: "))
X = int(input("Введите число Х, которое надо найти: "))
list_random = [randint(0,10) for i in range(0, N)]
number_counter = 0
min_spread = 10
for i in range(len(list_random)):
    diff = abs(X - list_random[i])
    if diff < min_spread:
        min_spread = diff
        number_counter = list_random[i]
print(*list_random)
print(f"Самый близкий по величине элемент к заданному числу Х равен {number_counter}")