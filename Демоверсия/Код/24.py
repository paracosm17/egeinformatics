text = open("C:\projects\Информатика ЕГЭ 2022\Информатика ЕГЭ 2022\Демоверсия\Доп. файлы\Задание 24/24.txt", "r").read()

maxl = 0
counter = 0

for i in range(len(text)):
    
    if text[i] == "P" and text[i+1] == "P":
        counter = 1
    
    else:
        counter += 1
        maxl = max(maxl, counter)

print(maxl)
