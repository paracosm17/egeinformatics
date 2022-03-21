# На грузовом судне необходимо перевезти контейнеры, имеющие одинаковый габарит и разные массы (некоторые контейнеры 
# могут иметь одинаковую массу). Общая масса всех контейнеров превышает грузоподъёмность судна. 
# Количество грузовых мест на судне не меньше количества контейнеров, назначенных к перевозке. Какое максимальное 
# количество контейнеров можно перевезти за один рейс и какова масса самого тяжёлого контейнера среди всех контейнеров, 
# которые можно перевезти за один рейс?
# Входные данные.
# В первой строке входного файла находятся два числа: S — грузоподъёмность судна (натуральное число, не превышающее 
# 100 000) и N — количество контейнеров (натуральное число, не превышающее 20 000). В следующих N строках находятся 
# значения масс контейнеров, требующих транспортировки (все числа натуральные, не превышающие 100), каждое в отдельной 
# строке.
# Выходные данные.
# Два целых неотрицательных числа: максимальное количество контейнеров, которые можно перевезти за один рейс и 
# масса наиболее тяжёлого из них.
# https://inf-ege.sdamgia.ru/problem?id=36039

# Фактически, абсолютно такая же задача, как и 26 (1), только вместо файлов и места под файлы - грузы и грузоподъемность
# Поэтому нейминг переменных менять не стал
# files - грузы, size - грузоподъемность, memory - складываем подходящие грузы, biggest_file - самый большой груз

# Считываем размеры всех файлов и сортируем в порядке возрастания
files = sorted(list(map(int, open("26 (11).txt", "r").read().splitlines()[1:])))

# Считываем общий объём памяти
size = int(open("26 (11).txt", "r").readline().split(" ")[0])

memory = []                                                 # Сюда будем складывать подходящие файлы

for i in range(len(files)):                                 # Проходимся циклом по всем файлам
    if sum(memory) + files[i] <= size:                      # Если влезаем или ровно влезли
        memory.append(files[i])                             # То добавляем еще один файл

biggest_file = files[len(memory)-1] + size - sum(memory)    # Ищем размер самого большого файла который влезет
while biggest_file not in files:                            # Ищем этот файл во всех файлах, если его нет,
    biggest_file -= 1                                       # То уменьшаем на единицу

print(len(memory), biggest_file)