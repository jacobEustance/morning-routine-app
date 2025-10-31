import random
q = open("quotes.txt", "r")
quotes = q.readlines()
randomquote = random.choice(quotes)
print(randomquote)

index = quotes.index(randomquote)
a = open("authors.txt", "r")
authors = a.readlines()
print(authors[index])