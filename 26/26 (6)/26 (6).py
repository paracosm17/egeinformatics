# Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена, поэтому перевезти 
# сразу все грузы не удастся. Грузы массой от 200 до 210 кг грузят в первую очередь, гарантируется, что все такие грузы 
# поместятся. На оставшееся после этого место стараются взять как можно больше грузов. Если это можно сделать несколькими 
# способами, выбирают тот способ, при котором самый большой из выбранных грузов имеет наибольшую массу. Если и при этом 
# условии возможно несколько вариантов, выбирается тот, при котором наибольшую массу имеет второй по величине груз, и т. д.
# Известны количество грузов, масса каждого из них и грузоподъёмность грузовика. Необходимо определить количество и общую 
# массу грузов, которые будут вывезены при погрузке по вышеописанным правилам.
# Входные данные.
# Первая строка входного файла содержит два целых числа: N — общее количество грузов и M — грузоподъёмность грузовика в кг. 
# Каждая из следующих N строк содержит одно целое число — массу груза в кг.
# В ответе запишите два целых числа: сначала максимально возможное количество грузов, затем их общую массу.
# https://inf-ege.sdamgia.ru/problem?id=33198

# Считываем размеры всех файлов и сортируем в порядке возрастания
cargos = sorted(list(map(int, open("26 (6).txt", "r").read().splitlines()[1:])))

# Считываем общий объём памяти
capacity = int(open("26 (6).txt", "r").readline().split(" ")[1])

c = len([x for x in cargos if 200 <= x <= 210])         # Количество грузов 200-210 кг
remains = [x for x in cargos if not (200 <= x <= 210)]  # Список оставшихся грузов
memory = [x for x in cargos if 200 <= x <= 210]         # Сюда будем добавлять грузы. Изначально тут уже все грузы 200-210

for i in range(len(remains)):                           # С помощью этого цикла узнаем
    if sum(memory) + remains[i] <= capacity:            # Максимальное количество грузов
        memory.append(remains[i])
        c +=  1                                         # Счетчик количества грузов

memory.pop()                                            # Вырезаем из грузов 2 элемента, чтобы
memory.pop()                                            # Можно было уместить один максимально большой

biggest = capacity - sum(memory)                        # Вычисляем максимально большой груз
while biggest not in remains:
    biggest -= 1 
memory.append(biggest)                                  # Добавляем в список наших грузов
print(c, sum(memory))                                   # Выводим количество и сумму с учетом максимально большого груза
