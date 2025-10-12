#Темник Кирилл

f = open(r"text.txt", "r", encoding = 'UTF-8')
text = f.read()
count_of_words = text.lower().split()
count_of_new_words = sorted(set(count_of_words))

print(count_of_new_words)

q = open(r"output.txt", "w", encoding = 'UTF-8')

for i in count_of_new_words:
    q.write(i + ", ")
