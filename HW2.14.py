# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number_N = int(input("Введите число: "))
base = 2
while base < number_N:
    print(f'числа 2к для N : {base}')
    base = base * 2