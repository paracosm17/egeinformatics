from itertools import combinations                                  # Импортируем функцию, если пара это разные элементы, а не только рядомстоящие

# Начало одинаково для всех задач
nums = list(map(int, open("17.txt", "r").read().splitlines()))      # Тут генерируем список чисел из файла
pairs = []                                                          # Сюда будем добавлять нужные пары


# ЦИКЛ
# Либо пара - это только рядом стоящие числа, тогда будет один цикл
for i in range(len(nums)-1):                                        # Проходимся циклом по всем числам
    if nums[i] or nums[i+1]:                                        # Если выполняется условие (Условие в каждой задаче своё!)
        pairs.append([nums[i], nums[i+1]])                          # Добавляем пару в список всех пар

# Либо пара - это любые числа, тогда используем функцию combinations. Она как раз составит все комбинации без повторений
# Обязательно указывайте r=2, чтобы генерировались пары
for i, j in combinations(nums, r=2):
    if i or j:                                                      # Если выполняется условие (Условие в каждой задаче своё!)                        
        pairs.append([i, j])                                        # Добавляем пару в список всех пар


# ВЫВОД РЕЗУЛЬТАТА
# Либо нужно вывести количество пар и максимальную сумму элементов пар
print(len(pairs), max(list(map(sum, pairs))))

# Либо нужно вывести количество пар и максимальную из разностей элементов пар
print(len(pairs), max(list(map(lambda l: abs(l[0] - l[1]), pairs))))

# Определяем lambda функцию, которая из списка вида [число1, число2] достанет числа
# и отнимет их друг от друга и вернет модуль разности
# Выводим количество пар и самую большую разность