# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. Определите максимальное количество 
# идущих подряд символов, среди которых каждые два соседних различны.
# https://inf-ege.sdamgia.ru/problem?id=27421

f = open("24 (1).txt", "r").read()

counter = 0
maxx = 0

for i in range(len(f)-1):
    if f[i] == f[i+1]:
        counter = 1
    else:
        counter += 1
        maxx = max(maxx, counter)

print(maxx)
