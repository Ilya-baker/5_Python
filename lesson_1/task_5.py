a = ord(input('Введите первую строчную букву английского алфавита в нижнем регистре: '))
b = ord(input('Введите вторую строчную букву английского алфавита в нижнем регистре: '))

a = a - 96

b = b - 96

if a > b:
    c = a - b - 1
else:
    c = b - a - 1

print('Первая буква стоит', a,'в английском алфавите\nВторая буква стоит', b, 'в английском алфавите')
print('Между ними находится',c,'букв')