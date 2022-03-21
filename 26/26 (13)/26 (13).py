from unittest.util import sorted_list_difference


f = lambda x: x.split()
products = list(map(f, open("26 (13).txt", "r").read().splitlines()[1:]))
f = lambda x: [int(x[0]), x[1]]
products = sorted(list(map(f, products)))

summa = int(open("26 (13).txt", "r").readline().split()[1])
summ = 0
i = 0

while summ < summa:
    summ += products[i][0]
    if summ > summa:
        summ -= products[i][0]
        break
    i += 1
