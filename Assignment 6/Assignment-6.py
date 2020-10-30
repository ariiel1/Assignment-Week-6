old = open("old.txt","r",encoding="utf-8")
new = open("new.txt","w",encoding="utf-8")
lines = 1
for linecount in old:
    if linecount != "\n":
        new.write(str(lines) + " " + linecount)
        lines += 1

