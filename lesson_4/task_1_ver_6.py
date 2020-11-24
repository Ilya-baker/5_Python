import timeit, cProfile

def turn(num):
    decision = list(num)
    for i in range(len(num) // 2):
        dic_i = decision[i]
        decision[i] = decision[len(num) - i - 1]
        decision[len(num) - i - 1] = dic_i
    return ''.join(decision)

print(timeit.timeit(turn(str(123456789)), number=10)) # 5.5000000000055005e-06
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=10)) # 1.599999999990498e-06
print(timeit.timeit(turn(str(123456789)), number=100)) # 2.3999999999996247e-06
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=100)) # 2.6999999999943736e-06
print(timeit.timeit(turn(str(123456789)), number=1000)) # 1.7500000000003624e-05
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=1000)) # 1.8100000000007e-05
print(timeit.timeit(turn(str(123456789)), number=10000)) # 0.00016619999999999135
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=10000)) # 0.00016410000000000036
print(timeit.timeit(turn(str(123456789)), number=100000)) # 0.0019057999999999992
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=100000)) # 0.0017289000000000054
print(timeit.timeit(turn(str(123456789)), number=1000000)) # 0.016861400000000012
print(timeit.timeit(turn(str(123456789023464689432648775834)), number=1000000)) # 0.016405299999999998

cProfile.run('turn(str(123456789))')

   #       14 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1_ver_6.py:3(turn)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}

cProfile.run('turn(str(123456789023464689432648775834))')

   #       36 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1_ver_6.py:3(turn)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #     31    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}





