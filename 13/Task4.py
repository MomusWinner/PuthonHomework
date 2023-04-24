

file = input("Type file name: ")
words = {}
maxValue = 0
bestWord = ""

with open(file,"r") as fr:
    for i in fr:
        [ for j in i.lower().split() ]


for key in words:
    if int(words[key]) >= maxValue:
        maxValue = words[key]
        bestWord = key

print(f"Word: {bestWord} Quantity: {maxValue}")