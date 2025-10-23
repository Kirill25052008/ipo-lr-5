# Кирилл
# Вариант 3

f = open(r"text.txt", "r", encoding = 'UTF-8')# Открываем файл "text.txt" для чтения
text = f.read()# В переменную text записываем текст из файла "text.txt"
count_of_words = text.lower().split()# В переменную count_of_words (количество слов) записываем все слова из файла "text.txt" в нижнем регистре
count_of_new_words = sorted(set(count_of_words))# В переменную count_of_new_words (количество новых слов) записываем все уникальные слова из переменной count_of_words (количество слов)

print(count_of_new_words)# Выводим значение переменной count_of_words (количество слов)

q = open(r"output.txt", "w", encoding = 'UTF-8')# Открываем новый файл "output.txt" для записи

for i in count_of_new_words:# Создаём цикл (пока переменная i находится в переменной count_of_words (количество слов))
    q.write(i + ", ")# Записываем все уникальные слова из переменной count_of_words (количество слов) в новый файл "output.txt"


