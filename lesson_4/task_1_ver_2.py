import timeit, cProfile

num = int(input('Введите любое целое число: '))
turn = 0

while num > 0:
    turn = turn * 10 + num % 10
    num = num // 10

print(turn)
