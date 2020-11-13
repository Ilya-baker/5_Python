#https://drive.google.com/file/d/1zQZkpktSmWmwYIq9kZuHiFlVWX7nBd6O/view?usp=sharing

sign = 0
while sign != '0':
    num_1 = float(input('Введете первое число: '))
    num_2 = float(input('Введете второе число: '))
    sign = str(input('Введете символ математической операции или 0 для завершения процесса: '))
    if sign == '0':
        print('Завершение процесса')
        break
    elif sign == '/' and num_2 == 0:
        sign=('На ноль делить нельзя, повторите ввод')
    elif sign == '+':
        sign = num_1 + num_2
    elif sign == '-':
        sign = num_1 - num_2
    elif sign == '*':
        sign = num_1 * num_2
    elif sign == '/':
        sign = num_1 / num_2
    else:
        sign =('Не верное значение, повторите ввод')
    print(sign)