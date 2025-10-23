#Кирилл

f = open(r"text.txt","r",encoding = 'UTF-8')# Открываем файл "text.txt" для чтения
text = f.read()# Читаем файл
count_of_words = text.split()# В переменную count_of_words записываем количество слов из файла "text.txt"

print(count_of_words)# Выводим значение переменной count_of_words


