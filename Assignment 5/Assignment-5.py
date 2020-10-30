def hapax(text):
    f = open("book.txt",encoding="utf-8")
    hapaxes = []
    all_words = []
    for i in f.read().split():
        all_words.append(i)
    word_count = {}

    for i in all_words:
        if i not in word_count:
            word_count[i.lower()] = 1
        else:
            word_count[i.lower()] += 1
    
    for(key,value) in word_count.items():
        if value == 1:
            hapaxes.append(key)
    return hapaxes
        

print(hapax("book.txt"))

