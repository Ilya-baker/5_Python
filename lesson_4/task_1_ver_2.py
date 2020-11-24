import timeit, cProfile

num = 0
turn = 0

while num > 0:
    turn = turn * 10 + num % 10
    num = num // 10

print(timeit.timeit('num = 1234567890', number=10)) # 4.5000000000045e-06
print(timeit.timeit('num = 123456789023464689432648775834', number=10)) # 1.1999999999928734e-06
print(timeit.timeit('num = 1234567890', number=100)) # 3.5000000000035003e-06
print(timeit.timeit('num = 123456789023464689432648775834', number=100)) # 3.5000000000035003e-06
print(timeit.timeit('num = 1234567890', number=1000)) # 2.7799999999994496e-05
print(timeit.timeit('num = 123456789023464689432648775834', number=1000)) # 2.8799999999995496e-05
print(timeit.timeit('num = 1234567890', number=10000)) # 0.00026449999999998697
print(timeit.timeit('num = 123456789023464689432648775834', number=10000)) # 0.0002817000000000097
print(timeit.timeit('num = 1234567890', number=100000)) # 0.002820299999999998
print(timeit.timeit('num = 123456789023464689432648775834', number=100000)) # 0.0029143999999999975
print(timeit.timeit('num = 1234567890', number=1000000)) # 0.028341500000000006
print(timeit.timeit('num = 123456789023464689432648775834', number=1000000)) # 0.0281458

cProfile.run('num = 1234567890')

   # 3 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('num = 123456789023464689432648775834')

 # 3 function calls in 0.000 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




