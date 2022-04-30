# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. Определите длину самой длинной 
# последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
# https://inf-ege.sdamgia.ru/problem?id=27686

from itertools import count

f = open("27686.txt", "r").read()

for i in count(1):      # Бесконечный итератор, возвращает числа 1 2 3 4 5 6 ... до бесконечности
    if "X" * i in f:
        maxx = i
    else:
        break

print(maxx)

# Однострочное решение
# print(len(max(" ".join(" ".join(f.split("Y")).split("Z")).split())))
