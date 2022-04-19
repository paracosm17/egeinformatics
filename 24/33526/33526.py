# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
# https://inf-ege.sdamgia.ru/problem?id=33526

from statistics import mode

f = open("33526.txt", "r").read()
mylist = []

for i in range(len(f)-2):
    if f[i] == f[i+2]:
        mylist.append(f[i+1])

print(mode(mylist))
