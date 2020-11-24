import timeit, cProfile

num = str(0)
num = list(reversed(num))
turn = 0

for i in num:
    turn = turn * 10 + int(i)

print(timeit.timeit('num = str(1234567890)', number=10)) # 1.1899999999995248e-05
print(timeit.timeit('num = str(123456789023464689432648775834)', number=10)) # 1.2200000000003874e-05
print(timeit.timeit('num = str(1234567890)', number=100)) # 6.659999999999999e-05
print(timeit.timeit('num = str(123456789023464689432648775834)', number=100)) # 0.00010330000000000061
print(timeit.timeit('num = str(1234567890)', number=1000)) # 0.0007086000000000037
print(timeit.timeit('num = str(123456789023464689432648775834)', number=1000)) # 0.0010037999999999991
print(timeit.timeit('num = str(1234567890)', number=10000)) # 0.006400599999999992
print(timeit.timeit('num = str(123456789023464689432648775834)', number=10000)) # 0.010657199999999992
print(timeit.timeit('num = str(1234567890)', number=100000)) # 0.06561979999999999
print(timeit.timeit('num = str(123456789023464689432648775834)', number=100000)) # 0.10282270000000002
print(timeit.timeit('num = str(1234567890)', number=1000000)) # 0.6737194
print(timeit.timeit('num = str(123456789023464689432648775834)', number=1000000)) # 1.0243884

cProfile.run('num = 1234567890')

  # 3 function calls in 0.000 seconds
  #
  #  Ordered by: standard name
  #
  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
  #       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('num = 123456789023464689432648775834')

   #       3 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

