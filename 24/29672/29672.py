# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. 
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z). 
# Определите количество строк, в которых буква E встречается чаще, чем буква A.
# https://inf-ege.sdamgia.ru/problem?id=29672

f = open("29672.txt", "r").read().splitlines()
counter = 0

for line in f:
    if line.count("E") > line.count("A"):
        counter += 1

print(counter)
