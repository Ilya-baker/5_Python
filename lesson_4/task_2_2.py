import timeit, cProfile
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# Второй способ:
# Прослеживается линейная зависимость от количества проведённых попыток и не зависит от размера числа вводимого пользователем.
# Однако, по факту, скорость выполнения алгоритма напрямую зависит от размера числа.
# И при введении довольно высокого значения, время работы кода значительно увеличивается.

num = int(input('Введите порядковый номер простого числа: ')) * 100
lis = []

for i in range (2, num + 1):
    for j in lis:
        if i % j == 0:
            break
    else:
        lis.append(i)

print(f'Простое число: {lis[num // 100 - 1]}')

print('4 ============================================')
print(timeit.timeit('num = 4', number=10)) # 5.600000000161032e-06
print(timeit.timeit('num = 4', number=100)) #3.5000000000451337e-06
print(timeit.timeit('num = 4', number=1000)) # 2.7900000000080638e-05
print(timeit.timeit('num = 4', number=10000)) # 0.0002644999999996678
print(timeit.timeit('num = 4', number=100000)) # 0.002692399999999928
print(timeit.timeit('num = 4', number=1000000)) # 0.02688209999999991
print('40 ============================================')
print(timeit.timeit('num = 40', number=10)) # 1.000000000139778e-06
print(timeit.timeit('num = 40', number=100)) # 3.5000000000451337e-06
print(timeit.timeit('num = 40', number=1000)) # 2.86000000002673e-05
print(timeit.timeit('num = 40', number=10000)) # 0.00028380000000005623
print(timeit.timeit('num = 40', number=100000)) # 0.0032332999999997725
print(timeit.timeit('num = 40', number=1000000)) # 0.02811640000000004
print('400 ============================================')
print(timeit.timeit('num = 400', number=10)) # 2.19999999995224e-06
print(timeit.timeit('num = 400', number=100)) # 3.600000000325565e-06
print(timeit.timeit('num = 400', number=1000)) # 2.799999999991698e-05
print(timeit.timeit('num = 400', number=10000)) # 0.00026919999999996946
print(timeit.timeit('num = 400', number=100000)) # 0.002686200000000305
print(timeit.timeit('num = 400', number=1000000)) # 0.027686300000000053
print('4000 ============================================')
print(timeit.timeit('num = 4000', number=10)) # 1.1000000004202093e-06
print(timeit.timeit('num = 4000', number=100)) # 3.5999999998814758e-06
print(timeit.timeit('num = 4000', number=1000)) # 2.8200000000033754e-05
print(timeit.timeit('num = 4000', number=10000)) # 0.000268000000000157
print(timeit.timeit('num = 4000', number=100000)) # 0.003633400000000009
print(timeit.timeit('num = 4000', number=1000000)) # 0.02751429999999999
print('4000000 ============================================')
print(timeit.timeit('num = 4000000', number=10)) # 1.09999999997612e-06
print(timeit.timeit('num = 4000000', number=100)) # 3.5000000000451337e-06
print(timeit.timeit('num = 4000000', number=1000)) # 2.8699999999659553e-05
print(timeit.timeit('num = 4000000', number=10000)) # 0.00026989999999971204
print(timeit.timeit('num = 4000000', number=100000)) # 0.0027077000000002016
print(timeit.timeit('num = 4000000', number=1000000)) # 0.02742530000000043
print('4 ============================================')
cProfile.run('num = 4')
#  3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('40 ============================================')
cProfile.run('num = 40')
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('400 ============================================')
cProfile.run('num = 400')
#          3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('4000 ============================================')
cProfile.run('num = 4000')
#    3 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}