#Темник Кирилл

str1 = input("Введите строку 1: ")
str2 = input("Введите строку 2: ")

if sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower()):
    print("Слова являются анаграммами")
else:
    print("Слова не являются анаграммами")

