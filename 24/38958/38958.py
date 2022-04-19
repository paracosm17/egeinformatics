# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
# https://inf-ege.sdamgia.ru/problem?id=38958

f = open("38958.txt", "r").read()
mylist = []
maxx = 0

for i, j in enumerate(f):
    if j == "A":
        mylist.append(i)
    
for i in range(2, len(mylist)-1):
    maxx = max(maxx, mylist[i] - mylist[i-2] - 1)

print(maxx)
