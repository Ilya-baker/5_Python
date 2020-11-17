import random

a = ord(input('Введите одну любую строчную букву английского алфавита в нижнем регистре: '))
b = ord(input('Введите ещё одну любую строчную букву английского алфавита в нижнем регистре: '))

if a > b:
    c = chr(random.randint(b,a))
else:
    c = chr(random.randint(a,b))

print(c)