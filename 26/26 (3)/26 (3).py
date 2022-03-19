# В первой строке входного файла находятся два числа: S — размер свободного места на диске 
# (натуральное число, не превышающее 10 000) и N — количество пользователей (натуральное число, не превышающее 5000). 
# В следующих N строках находятся значения объёмов файлов каждого пользователя (все числа натуральные, не превышающие 100), 
# каждое в отдельной строке.
# Запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив, 
# затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены файлы 
# максимально возможного числа пользователей.
# https://inf-ege.sdamgia.ru/problem?id=28141

# Всё то же самое, что и в 26 (1)
files = sorted(list(map(int, open("26 (3).txt", "r").read().splitlines()[1:])))
size = int(open("26 (3).txt", "r").readline().split(" ")[0])

memory = []

for i in range(len(files)):
    if sum(memory) + files[i] <= size:
        memory.append(files[i])

biggest_file = files[len(memory)-1] + size - sum(memory)
while biggest_file not in files:
    biggest_file -= 1

print(len(memory), biggest_file)