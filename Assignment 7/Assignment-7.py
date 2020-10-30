book = open("book.txt","r",encoding="utf-8")
words = []
for i in book.read().split():
    words.append(len(i))
avg = sum(words)/len(words)
print(avg)

