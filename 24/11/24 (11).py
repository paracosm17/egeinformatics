# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z). 
# Определите максимальное количество идущих подряд символов, среди которых нет ни одной буквы A и 
# при этом не менее трёх букв E.
# https://inf-ege.sdamgia.ru/problem?id=40740

f = open("24 (11).txt", "r").read().split("A")
mylist = [i for i in f if i.count("E") >= 3]
print(max(map(len, mylist)))
