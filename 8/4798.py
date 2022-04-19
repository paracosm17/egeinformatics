# Подсчет количества слов
# Некоторый алфавит содержит 4 различных символа. 
# Сколько трехбуквенных слов можно составить из символов этого алфавита, если символы в слове могут повторяться?
# https://inf-ege.sdamgia.ru/problem?id=4798

from itertools import *

counter = 0
for i in product("1234", repeat=3):
    counter += 1
    print(f'{counter}.\t{" ".join(i)}')
