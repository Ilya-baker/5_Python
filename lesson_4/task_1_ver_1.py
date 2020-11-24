import timeit, cProfile

def recursion(num, turn):
    if num != 0:
        return recursion(num // 10, turn * 10 + num % 10)
    return str(turn)

print(timeit.timeit(recursion(1234567890, 0), number=10)) # 4.400000000001625e-06
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=10)) #9.000000000120023e-07
print(timeit.timeit(recursion(1234567890, 0), number=100)) # 2.4999999999886224e-06
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=100)) # 2.5000000000025002e-06
print(timeit.timeit(recursion(1234567890, 0), number=1000)) # 1.7200000000008875e-05
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=1000)) # 1.6900000000000248e-05
print(timeit.timeit(recursion(1234567890, 0), number=10000)) # 0.0001648999999999956
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=10000)) # 0.00017259999999999498
print(timeit.timeit(recursion(1234567890, 0), number=100000)) # 0.0016424999999999912
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=100000)) # 0.0016892999999999908
print(timeit.timeit(recursion(1234567890, 0), number=1000000)) # 0.01690989999999999
print(timeit.timeit(recursion(123456789023464689432648775834, 0), number=1000000)) # 0.016485500000000014

cProfile.run('recursion(1234567890, 0)')

   #       14 function calls (4 primitive calls) in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #   11/1    0.000    0.000    0.000    0.000 task_1_ver_1.py:3(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('recursion(123456789023464689432648775834, 0)')

   #       34 function calls (4 primitive calls) in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #   31/1    0.000    0.000    0.000    0.000 task_1_ver_1.py:3(recursion)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




