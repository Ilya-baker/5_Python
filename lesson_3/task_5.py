# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = -1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
ind_num = -1

for i in range(len(array)):
    if array[i] < 0 and ind_num == -1 or 0 > array[i] > array[ind_num]:
        ind_num = i
    i += 1

print(f'Максимальный отрицательный элемент массива: {array[ind_num]}\nОн занимает {ind_num} позицию в массиве.')