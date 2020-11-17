# Урок 2 задача 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import timeit, cProfile

def recursion(num, turn):
    if num != 0:
        return recursion(num // 10, turn * 10 + num%10)
    return str(turn)

print(recursion(int(input('Введите любое целое число: ')), 0))

