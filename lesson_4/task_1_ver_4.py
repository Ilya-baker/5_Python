import timeit, cProfile

num = str(0)
num = ''.join(reversed(num))

print(timeit.timeit('num = str(1234567890)', number=10)) # 1.2100000000000999e-05
print(timeit.timeit('num = str(123456789023464689432648775834)', number=10)) # 1.2600000000001499e-05
print(timeit.timeit('num = str(1234567890)', number=100)) # 7.279999999999787e-05
print(timeit.timeit('num = str(123456789023464689432648775834)', number=100)) # 0.00010159999999999336
print(timeit.timeit('num = str(1234567890)', number=1000)) # 0.000650799999999993
print(timeit.timeit('num = str(123456789023464689432648775834)', number=1000)) # 0.0010035000000000044
print(timeit.timeit('num = str(1234567890)', number=10000)) # 0.00674799999999999
print(timeit.timeit('num = str(123456789023464689432648775834)', number=10000)) # 0.010159299999999996
print(timeit.timeit('num = str(1234567890)', number=100000)) # 0.0673953
print(timeit.timeit('num = str(123456789023464689432648775834)', number=100000)) # 0.10195050000000003
print(timeit.timeit('num = str(1234567890)', number=1000000)) # 0.6697242999999999
print(timeit.timeit('num = str(123456789023464689432648775834)', number=1000000)) # 1.020854

cProfile.run('num = str(1234567890)')

   #       3 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('num = 123456789023464689432648775834')

   #   3 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



