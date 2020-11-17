# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

num_first = 2
num_last = 99 + 1
mul_first = 2
mul_last = 9 + 1

for i in range(mul_first, mul_last):
    counter = 0
    for mul_ in range(num_first, num_last):
        if mul_ % i == 0:
            counter += 1
    print(f'{counter} чисел кратно числу {i}')