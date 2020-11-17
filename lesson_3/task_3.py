#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_len = 0
max_len = 0


for i in range(len(array)):
    if array[min_len] > array[i]:
        min_len = i
    elif array[max_len] < array[i]:
        max_len = i
        
print(f'{array}\nmin: {array[min_len]}  max: {array[max_len]}')
array[min_len], array[max_len] = array[max_len], array[min_len]
print(array)