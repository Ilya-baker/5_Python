import random

a = float(input('Введите любое вещественное число 1: '))
b = float(input('Введите любое вещественное число 2: '))

if a > b:
    c = random.uniform(b,a)
else:
    c = random.uniform(a,b)

print(c)
