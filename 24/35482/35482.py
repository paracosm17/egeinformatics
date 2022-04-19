# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. 
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв G 
# (если таких строк несколько, надо взять ту, которая находится в файле раньше), и определить, 
# какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, 
# которая позже стоит в алфавите.
# https://inf-ege.sdamgia.ru/problem?id=35482

from statistics import multimode

file = open("35482.txt").read().splitlines()
strings = []

# Генерируем список вида [[количество G1, индекс строки1], [количество G2, индекс строки2], ...]
# Где каждый подсписок - это строка. Первый элемент подсписка - количество букв g, второй элемент - номер строки
for index, line in enumerate(file):
    strings.append([line.count("G"), index])

string = file[sorted(strings)[0][1]]    # Получаем искомую строку. Сортируем strings, таким образом первый элемент
                                        # будет строкой, с наименьшим количеством g и получаем индекс этой строки

print(max(multimode(string)))           # С помощью multimode выбираем самые часто встречаемые символы в строке
                                        # И с помощью max() определяем тот символ, который стоит позже в алфавите
                                        # Так как при сравнении букв будут сравниваться их значения в UNICODE, а чеё значение
                                        # больше, тот и стоит позже в алфавите

# Решение в одну строку
# print(max(multimode(open("24 (6).txt").read().splitlines()[sorted([[l.count("G"), i] for i, l in enumerate(open("24 (6).txt").read().splitlines())])[0][1]])))
