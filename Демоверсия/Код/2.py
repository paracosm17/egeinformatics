print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not y or (x == w)) or z and not x:
                    continue
                print(w, x, y, z)

# Вывод:

# w x y z
# 0 1 1 0
# 0 1 1 1
# 1 0 1 0

# Далее просто соотносим таблицы, анализируем и формируем ответ
# Ответ: wxyz
