#Кирилл

str = input("Введите строку: ")

count_of_vowels = 0
vowels = "аоэеиыуёюяАОЭЕИЫУЁЮЯaeiouAEIOU"

for i in str:
    if i in vowels:
        count_of_vowels = count_of_vowels + 1
        
print("Количество гласных = ", count_of_vowels)

