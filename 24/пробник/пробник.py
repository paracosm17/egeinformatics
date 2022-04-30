# Задание с моего пробника по информатике
# На решуЕГЭ подобного задания не нашёл, напишу примерно как оно звучало

# Дана последовательность из букв B, D, A. Найти длину самой длинной подпоследовательности,
# состоящей из BA или DA или BA и DA
# Например, в последовательности BDAADBADBADBADABADADABADBADB 
# ответ будет BADABADADABA, её длинна соответственно 12

f = open("пробник.txt", "r").read()

# Алгоритмическое решение
counter, maxx = 0, 0
for i in range(len(f)-1):
    if f[i] in "BD" and f[i+1] == "A":
        counter += 1
        maxx = max(maxx, counter)
        continue
    if f[i] == "A" and f[i-1] in "BD":
        continue
    else:
        counter = 0
print(maxx*2)


# Решение с помощью regexp
import re
from itertools import count
for i in count(1):
    match = re.search(r"(DA|BA){%s}" % str(i), f)
    if match:
        continue
    print((i - 1) * 2)
    break


# Решение с помощью замены
f = f.replace("DA", "X").replace("BA", "X")
print(len(max(" ".join(" ".join(" ".join(f.split("D")).split("B")).split("A")).split()))*2)
