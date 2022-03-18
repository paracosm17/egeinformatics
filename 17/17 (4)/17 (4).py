# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. 
# Назовём парой два идущих подряд элемента последовательности. Определите количество пар, в которых хотя бы 
# один из двух элементов делится на 5 и хотя бы один из двух элементов меньше среднего арифметического всех 
# элементов последовательности, значение которых нечетно. В ответе запишите два числа: сначала количество 
# найденных пар, а затем — максимальную сумму элементов таких пар.
# https://inf-ege.sdamgia.ru/problem?id=40992

nums = list(map(int, open("17 (4).txt", "r").read().splitlines()))
pairs = []
odds = [i for i in nums if i % 2 == 1]
average_odds = sum(odds)/len(odds)

for i in range(0, len(nums)-1):
    if ((nums[i] % 5 == 0) or (nums[i+1] % 5 == 0)) and ((nums[i] < average_odds) or (nums[i+1] < average_odds)):
        pairs.append([nums[i], nums[i+1]])

print(len(pairs), max(list(map(sum, pairs))))
