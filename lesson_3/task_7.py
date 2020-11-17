# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
num_1 = 0
num_2 = 0
print(array)


if array[0] < array[1]:
    num_2 = 1
else:
    num_1 = 1
for i in range(2, len(array)):
    if array[i] < array[num_1]:
        num_1 = i
    elif array[i] < array[num_2]:
        num_2 = i

print(f'Первый наименьший элемент: {array[num_1]}, позиция в массиве {num_1}')
print(f'Второй наименьший элемент: {array[num_2]}, позиция в массиве {num_2}')