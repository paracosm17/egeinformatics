# Подсчет количества разных последовательностей
# Азбука Морзе позволяет кодировать символы для сообщений по радиосвязи, задавая комбинацию точек и тире. 
# Сколько различных символов (цифр, букв, знаков пунктуации и т. д.) можно закодировать, 
# используя код азбуки Морзе длиной не менее четырёх и не более пяти сигналов (точек и тире)?
# https://inf-ege.sdamgia.ru/problem?id=4556

from itertools import product

print(len(tuple(product(".-", repeat=4))) + len(tuple(product(".-", repeat=5))))
