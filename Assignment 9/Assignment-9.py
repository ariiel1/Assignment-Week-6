import re

text = ''.join(open('miyagi.txt').readlines())
sentences = re.split(r"(?<=[^A-Z].[.?]) +(?=[A-Z])", text)

for i in sentences:
    print(i)

