# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [84052; 84130], 
# число, имеющее максимальное количество различных натуральных делителей, если таких чисел несколько — 
# найдите минимальное из них. Выведите на экран количество делителей такого числа и само число.

# Например, в диапазоне [2; 48] максимальное количество различных натуральных делителей имеет число 48, 
# поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# https://inf-ege.sdamgia.ru/problem?id=27857

maxx = 0
pairs = []

for num in range(84052, 84131):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
            pairs.append([count, num])  # Создаем список списков вида [[кол-во делителей, число], ..., ...] 
    maxx = max(maxx, count)             # Выбираем самое большое количество делителей


# Ищем первое число с самым большим количеством делителей. Первое найденное и будет самым маленьким
for pair in pairs:
    if pair[0] == maxx:
        print(pair)
        break