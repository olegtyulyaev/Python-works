# На столе лежат n монеток. Некоторые из них лежат вверх решкой,а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите оличество монеток: "))
orel, reshka = 0, 0
for i in range(n):
    temp = int(input(f"Введите 0 или 1 (0 - решка, 1 - орёл): "))
    if temp:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Минимальное количество монеток, которое нужно перевернуть - {orel} монеток')
else:
    print(f'Минимальное количество монеток, которое нужно перевернуть - {reshka} монеток')