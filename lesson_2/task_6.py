import random

num = random.randint(0, 100)
print(num)
i = 10
while i != 0:
    luck = int(input(f'Введи целое число от 0 до 100. Попыток {i}: '))
    i -= 1
    if num > luck:
        print('Правильный ответ больше')
    elif num < luck:
        print('Правильный ответ меньше')
    elif num == luck:
        break
print(f'Верный ответ: {num}')
