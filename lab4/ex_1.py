#!/usr/bin/env python3
# Генератор
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Шкаф', 'price': 20500, 'color': 'red'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
print(*('\'' + x + '\'' for x in field(goods, 'title')))    #
print(*(x for x in field(goods, 'title', 'price')))  # Выводим все значения title и price
print(*(x for x in gen_random(1, 3, 5)))  # Выводим массив чисел от 1 до 3 5 раз
