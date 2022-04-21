# Подсчет количества слов
# Некоторый алфавит содержит 4 различных символа. 
# Сколько трехбуквенных слов можно составить из символов этого алфавита, если символы в слове могут повторяться?
# https://inf-ege.sdamgia.ru/problem?id=4798

from itertools import product

print(len(tuple(product("ABCD", repeat=3))))
