import timeit, cProfile

num = input('Введите любое целое число: ')
num = list(reversed(num))
turn = 0

for i in num:
    turn = turn * 10 + int(i)

print(turn)