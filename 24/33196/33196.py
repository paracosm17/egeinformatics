# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
# https://inf-ege.sdamgia.ru/problem?id=33196

from statistics import multimode

f = open("33196.txt", "r").read()
mylist = []

for i in range(len(f)-1):
    if f[i] == "A":
        mylist.append(f[i+1])
    
print(multimode(mylist))
