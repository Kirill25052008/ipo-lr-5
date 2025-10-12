#Темник Кирилл

str = input("Введите строку: ")

a = str.split()

for i in a:
    print(i[-1:0:-1] + i[0])
