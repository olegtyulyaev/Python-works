# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент арифметической прогрессии: "))
b = int(input("Введите введите разность арифметической прогрессии: "))
c = int(input("Введите количество элементов вывода: "))
lst_progression = []


def arithmetic_progression(a, b, c, lst_progression):
    count_progr = 0
    for i in range(c):
        count_progr = a
        a = a+b
        lst_progression.append(count_progr)
    return lst_progression


print(arithmetic_progression(a, b, c, lst_progression))