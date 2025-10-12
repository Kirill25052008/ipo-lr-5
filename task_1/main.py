#Темник Кирилл

str = input("Введите строку ")
print("Длина строки = ", len(str))

count_of_vowels = 0
count_of_consonants = 0

vowels = "аоэеиыуёюяАОЭЕИЫУЁЮЯ"
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

for i in str:
    if i in vowels:
        count_of_vowels = count_of_vowels + 1
    if i in consonants:
        count_of_consonants = count_of_consonants + 1

print("Количество гласных = ", count_of_vowels)
print("Количество согласных = ", count_of_consonants)
