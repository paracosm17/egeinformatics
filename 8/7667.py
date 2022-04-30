# Подсчет количества слов с ограничениями
# Сколько слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э? 
# Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.
# https://inf-ege.sdamgia.ru/problem?id=7667

from itertools import product

counter = 0

for i in product("ЕГЭ", repeat=5):
    if i[0] == "Г":
        continue
    counter += 1

print(counter)
