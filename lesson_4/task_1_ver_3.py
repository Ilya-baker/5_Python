import timeit, cProfile

num = 0
num = int(str(num)[::-1])

print(timeit.timeit('num = 1234567890', number=10)) # 4.100000000006876e-06
print(timeit.timeit('num = 123456789023464689432648775834', number=10)) # 1.000000000001e-06
print(timeit.timeit('num = 1234567890', number=100)) # 5.400000000002625e-06
print(timeit.timeit('num = 123456789023464689432648775834', number=100)) # 3.600000000006376e-06
print(timeit.timeit('num = 1234567890', number=1000)) # 2.7100000000002122e-05
print(timeit.timeit('num = 123456789023464689432648775834', number=1000)) # 2.789999999999737e-05
print(timeit.timeit('num = 1234567890', number=10000)) # 0.0002758000000000066
print(timeit.timeit('num = 123456789023464689432648775834', number=10000)) # 0.0003520999999999941
print(timeit.timeit('num = 1234567890', number=100000)) # 0.003236799999999998
print(timeit.timeit('num = 123456789023464689432648775834', number=100000)) # 0.002850399999999989
print(timeit.timeit('num = 1234567890', number=1000000)) # 0.0277313
print(timeit.timeit('num = 123456789023464689432648775834', number=1000000)) # 0.027635699999999985

cProfile.run('num = 1234567890')

 # 3 function calls in 0.000 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('num = 123456789023464689432648775834')

   #     3 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




