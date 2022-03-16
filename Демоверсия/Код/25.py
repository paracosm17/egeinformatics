counter = 0                             # Счётчик для наших 5 чисел
number = 700000                         # Изначальное число

while counter < 5:                      # Цикл. Завершиться, когда найдем 5 нужных чисел
    
    # минимальный делитель
    for i in range(2, number-1):        # Ищем минимальный делитель
        if number % i == 0:
            mind = i
            break
    
    # максимальный делитель
    for i in range(number-1, 2, -1):    # Ищем максимальный делитель
        if number % i == 0:
            maxd = i
            break
    
    summa = mind + maxd                 # Суммируем делители

    if str(summa)[-1] == "8":           # Если сумма оканчивается на 8
        counter += 1                    # то увеличиваем счетчик на 1 и 
        print(number, summa)            # выводим число и сумму
    
    number += 1                         # Увеличиваем число на 1
