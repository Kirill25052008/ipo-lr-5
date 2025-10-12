#Темник Кирилл

f = open(r"text.txt","r",encoding = 'UTF-8')
text = f.read()
count_of_words = text.split()

print(count_of_words)
