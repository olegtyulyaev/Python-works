# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
n_set = set(int(input()) for i in range(n))
print("Первое множество", n_set)

m = int(input("Введите количество элементов второго множества: "))
m_set = set(int(input()) for i in range(m))
print("Второе множество", m_set)

sum_set = sorted(n_set.intersection(m_set))
print(f"Объединенное множество:", sum_set)