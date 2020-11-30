# Задача 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке[0; 50).Выведите на экран исходный и отсортированный массивы.

import random

size = 10
long = 50
array = [round(random.uniform(0, long), 1) for i in range(size)]
print(array)

def merges(array):

    if len(array) > 1:
        i, j, f = 0, 0, 0
        left_num = (array[:len(array) // 2])
        right_num = (array[len(array) // 2:])
        merges(left_num)
        merges(right_num)

        while i < len (left_num) and j < len(right_num):
            if left_num[i] < right_num[j]:
                array[f] = left_num[i]
                i +=1
            else:
                array[f] = right_num[j]
                j += 1
            f += 1

        while i < len(left_num):
            array[f] = left_num[i]
            i += 1
            f += 1

        while j < len(right_num):
            array[f] = right_num[j]
            j += 1
            f += 1

merges(array)
print(array)