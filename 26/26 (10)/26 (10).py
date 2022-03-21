# В текстовом файле записан набор натуральных чисел, не превышающих 10^9. Гарантируется, что все числа различны. 
# Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в 
# файле, и чему равно наибольшее из средних арифметических таких пар.
# Входные данные.
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк 
# содержит одно число.
# В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
# https://inf-ege.sdamgia.ru/problem?id=35484

nums = list(map(int, open("26 (10).txt", "r").read().splitlines()[1:]))
result = []
for i in range(len(nums) - 1):                                                           
    for j in range(i + 1, len(nums)):
        if nums[i] % 2 == 0 and nums[j] % 2 == 0: 
            if (nums[i] + nums[j]) // 2 in nums:
                    result.append((nums[i] + nums[j]) // 2)
print(len(result), max(result))