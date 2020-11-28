# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Урок 1 Задача 6: Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# Windows 10 pro 1909 (64-разрядная) CPython Python 3.8 (32-bit)

import sys

ABC = int(input('Введите целое положительное число от 1 до 26: ')) - 1

# Вариант 1
var_1 = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'Вариант 1: {var_1[ABC]}')

# Вариант 2
var_2 = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'Вариант 2: {var_2[ABC]}')

# Вариант 3
var_3 = ['A', 'B', 'C', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(f'Вариант 3: {var_3[ABC]}')

# Вариант 4
var_4 = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F',
       6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L',
       12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R',
       18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
print(f'Вариант 4: {var_4[ABC]}')

print(f'Вариант 1: Объекты класса: {type(var_1)}, в количестве {len(var_1)}, заняли {sys.getsizeof(var_1)} Байт.')
# Объекты класса: <class 'str'>, в количестве 26, заняли 51 Байт.
print(f'Вариант 2: Объекты класса: {type(var_2)}, в количестве {len(var_2)}, заняли {sys.getsizeof(var_2)} Байт.')
# Объекты класса: <class 'tuple'>, в количестве 26, заняли 124 Байт.
print(f'Вариант 3: Объекты класса: {type(var_3)}, в количестве {len(var_3)}, заняли {sys.getsizeof(var_3)} Байт.')
# Объекты класса: <class 'list'>, в количестве 26, заняли 132 Байт.
print(f'Вариант 4: Объекты класса: {type(var_4)}, в количестве {len(var_4)}, заняли {sys.getsizeof(var_4)} Байт.')
# Объекты класса: <class 'dict'>, в количестве 26, заняли 628 Байт.

# Выводы:
#
# Пустая строка заняла 25 байт и каждый последующий символ будет добавлять по 1 байту.
# В данном примере строковый класс занял 51 байт.
# Значит одна строка будет "выгоднее" в плане занимаемой памяти, нежели множество коротких строк
# (+25 байт добавочной стоимости за строку).
#
# У списка и словаря getsizeof() не возвращала настоящую память. Эта функция считает каждый объект списка указателем
# в независимости от его фактического размера.
# И возвращает память указателей + память самого списка. Однако пустой словарь весит 20 байт, а пустой список 28.
# Получается что словари "выгоднее"
# списков на 8 байт, с учётом одинакового наполнения.
#
# Пустой словарь занимает 40 байт, при добавлении от 1 до 5 элементов включительно возрастает на 68 байт,
# от 6 до 9 на 68 байт, от 10 до 20 на 148, от 21 на 284 байта. И того в данном примере 628 байт.
# Получается словарь самый массивный класс, однако самый быстро действенный по обращению к его элементам.




