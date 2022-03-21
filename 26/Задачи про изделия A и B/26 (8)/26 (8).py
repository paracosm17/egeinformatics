# Предприятие производит оптовую закупку некоторых изделий A и B, на которую выделена определённая сумма денег. 
# У поставщика есть в наличии партии этих изделий различных модификаций по различной цене. На выделенные деньги 
# необходимо приобрести как можно больше изделий A независимо от модификации. Если у поставщика закончатся изделия A, 
# то на оставшиеся деньги необходимо приобрести как можно больше изделий B. Известны выделенная для закупки сумма, 
# а также количество и цена различных модификаций данных изделий у поставщика. Необходимо определить, сколько будет 
# закуплено изделий B и какая сумма останется неиспользованной.
# Входные данные.
# Первая строка входного файла содержит два целых числа: N — общее количество партий изделий у поставщика и M — сумма 
# выделенных на закупку денег (в рублях). Каждая из следующих N строк описывает одну партию и содержит два целых числа 
# (цена одного изделия в рублях и количество изделий в партии) и один символ (латинская буква A или B), определяющий тип 
# изделия. Все данные в строках входного файла отделены одним пробелом.
# В ответе запишите два целых числа: сначала количество закупленных изделий типа B, затем оставшуюся неиспользованной 
# сумму денег.
# https://inf-ege.sdamgia.ru/problem?id=33528

# Генерируем список всех партий вида [["10", "15", "A"], ["19", "17", "B"], ..., ...]
f = lambda x: x.split()                                             
lots = list(map(f, open("26 (8).txt", "r").read().splitlines()[1:]))

# Изначально выделенная сумма и остаток после покупки всех партий A
summa = int(open("26 (8).txt", "r").readline().split()[1])
remain = summa - sum([int(x[0])*int(x[1]) for x in lots if x[2] == "A"])

# Все партии B, отсортированные по цене за штуку, вида [[19, 17], [27, 13], ..., ...] и счётчик для товаров B
Bs = sorted([[int(x[0]), int(x[1])] for x in lots if x[2] == "B"])
b = 0

if remain > 0:
    for price, quantity in Bs:                  # Проходимся по партиям B
        if remain - (price * quantity) > 0:     # Если купить всю партию и остануться деньги, то продолжаем покупать
            remain -= price * quantity
            b += quantity                       # Считаем товары 
            continue
        else:                                   # Если денег на целую партию уже не хватает
            for _ in range(1, quantity):        # То проходимся циклом по этой партии
                if remain - price > 0:          # Если нам хватает денег купить один товар
                    remain -= price             # То покупаем
                    b += 1                      # Считаем товары
                else:
                    break
            break

print(b, remain)                                # Вывод результата

# Чтобы не запутаться
# b - один товар внутри партии B
