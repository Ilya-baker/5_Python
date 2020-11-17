import timeit, cProfile

num = int(input('Введите любое целое число: '))
num = int(str(num)[::-1])

print(num)