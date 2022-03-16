# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
# https://inf-ege.sdamgia.ru/problem?id=37131

f = open("24 (9).txt", "r").read()
counter = 0
maxx = 0

for i in range(len(f)-1):
    if (f[i] == "K" and f[i+1] == "L") or (f[i] == "L" and f[i+1] == "K"):
        counter = 1
    else:
        counter += 1
        maxx = max(maxx, counter)

print(maxx)
