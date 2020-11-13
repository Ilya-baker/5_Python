num = int(input('Введите любое целое число: '))
num_even = 0
num_odd = 0
while num != 0:
    if num%10 %2 == 0:
        num_even += 1
    else:
        num_odd += 1
    num = num // 10
print(f'Количество чётных чисел: {num_even}, количество нечётных чисел: {num_odd}.')



