# Разное
# Шахматная доска состоит из 8 столбцов и 8 строк. Какое минимальное количество бит потребуется для кодирования 
# координат одной шахматной клетки?
# https://inf-ege.sdamgia.ru/problem?id=4790

from itertools import product, count

for i in count(1):
    a = len(tuple(product("xy", repeat=i)))
    if a >= 8*8:
        print(a)
        break
