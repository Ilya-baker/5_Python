import random

a = int(input('Введите любое целое число 1: '))
b = int(input('Введите любое целое число 2: '))

if a > b:
    c = random.randint(b,a)
else:
    c = random.randint(a,b)

print(c)
