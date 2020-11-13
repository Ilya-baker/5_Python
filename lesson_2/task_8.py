num = int(input('Введите общее количество чисел: '))
scan = int(input('Введите цифру которую необходимо посчитать: '))
quantity = 0
for i in range(num, 0, -1):
    num_count = int(input(f'{i} -- '))
    while num_count != 0:
        if num_count % 10 == scan:
            quantity += 1
        num_count = num_count // 10
print(f'Цифра {scan} была введена {quantity} раз(а)')