# Разное
# Шахматная доска состоит из 8 столбцов и 8 строк. Какое минимальное количество бит потребуется для кодирования 
# координат одной шахматной клетки?
# https://inf-ege.sdamgia.ru/problem?id=4790

from itertools import *

for i in range(100):
    a = len(tuple(product("xy", repeat=i)))
    print(a)
    if a >= 8*8:
        break
