# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

#*Пример:*

#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам  


song = input('Введите текст песни: ').split()

def check_rhytm (song):
  letters = 'а е ё и о у ы э ю я'
  count_letters= lambda x: sum(1 for i in x if i in letters)
  count_letters_in_words= list(map(count_letters, song))
  print (count_letters_in_words)
  return ('Парам пам-пам') if all([i == count_letters_in_words[0] for i in count_letters_in_words]) else ('Пам парам')

print(check_rhytm(song))
