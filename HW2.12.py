# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summa = int(input('Введите сумму чисел: '))
proizved = int(input('Введите произведение чисел: '))

chislo_1 = (summa - (summa ** 2 - 4 * proizved) ** 0.5) / 2
chislo_2 = (summa + (summa ** 2 - 4 * proizved) ** 0.5) / 2
if chislo_1 > 1000 or chislo_2 > 1000:
 print('Числа должны быть меньше 1000')
else:
 print(f'{summa} {proizved} -> {int(chislo_1), int(chislo_2)}')
