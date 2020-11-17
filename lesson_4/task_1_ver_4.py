import timeit, cProfile

num = str(input('Введите любое целое число: '))
num = ''.join(reversed(num))

print(int(num))