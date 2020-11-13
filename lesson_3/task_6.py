# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_len = 0
max_len = 0
_sum = 0
print(array)

for i in range(len(array)):
    if array[min_len] > array[i]:
        min_len = i
    elif array[max_len] < array[i]:
        max_len = i

if max_len > min_len:
    for i in range(min_len + 1, max_len):
            _sum += array[i]
else:
    for i in range(max_len + 1, min_len):
            _sum += array[i]

print(f'Минимальное число: {array[min_len]}\nМаксимальное число: {array[max_len]}')
print(f'Сумма чисел между ними: {_sum}')
