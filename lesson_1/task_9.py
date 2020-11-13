a = float(input('Введите три разных числа, первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if b > a > c or c > a > b:
    print(a)
elif a > b > c or c > b > a:
    print(b)
else:
    print(c)