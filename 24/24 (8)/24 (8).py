# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z. 
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# https://inf-ege.sdamgia.ru/problem?id=36037

f = open("24 (8).txt", "r").read()
counter = 0
maxx = 0

for i in range(len(f)-3):
    if f[i] == "X" and f[i+1] == "Z" and f[i+2] == "Z" and f[i+3] == "Y":
        counter = 3
    else:
        counter += 1
        maxx = max(maxx, counter)

print(maxx)
