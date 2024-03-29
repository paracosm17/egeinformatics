from itertools import *                 # Импортируем встроенный модуль itertools

counter = 0                             # Объявляем переменную counter для нумерации строк, для удобства

for i in product('ЕЛМРУ', repeat=4):    # Проходимся циклом по результату функции product() из модуля itertools
                                        # C помощью размещений с повторениями можно легко перебрать все строки 
                                        # фиксированной длины, состоящие из заданных символов
                                        # Первым аргументом записываем слово "ЛЕМУР" в алфавитном порядке
                                        # Так как программа будет перебирать символы в том порядке, 
                                        # в котором мы их запишем. А нас в задаче просят в алфавитном порядке
                                        # Вторым аргументом указываем количество повторений
                                        # У нас всего 5 букв, но в задаче нужны четырёхбуквенные слова

    counter += 1                        # Прибавляем к счетчику каждый раз единицу
    print(f"{counter}. {' '.join(i)}")  # Выводим в консоль результат с помощью f-строки
                                        # ' '.join(i) нужно для того, чтобы записывать слова в
                                        # удобно читаемом виде, так как изначально каждое слово выглядит так
                                        # ('Л', 'Е', 'М', 'У')
                                        
                                        # Далее остается просто посмотреть на вывод в консоли и увидеть,
                                        # что первое слово на букву Л идет под номером 126
