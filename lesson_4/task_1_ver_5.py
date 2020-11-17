import timeit, cProfile

time_ = """
num = str(1234567890)
# num = str(123456789023464689432648775834)
num = list(reversed(num))
turn = 0

for i in num:
    turn = turn * 10 + int(i)"""

print(timeit.timeit(time_, number=10))
# num = 1234567890 -- 0.00011690000000000311
# num = 123456789023464689432648775834 -- 0.0004568999999999962
print(timeit.timeit(time_, number=100))
# num = 1234567890 -- 0.0009398000000000045
# num = 1234567890234646894326487758345234576484568567956 -- 0.0049283999999999994
print(timeit.timeit(time_, number=1000))
# num = 1234567890 -- 0.009555599999999997
# num = 1234567890234646894326487758345234576484568567956 -- 0.04439280000000001
print(timeit.timeit(time_, number=10000))
# num = 1234567890 -- 0.0970687
# num = 1234567890234646894326487758345234576484568567956 -- 0.43472160000000004
print(timeit.timeit(time_, number=100000))
# num = 1234567890 -- 0.9547130000000001
# num = 1234567890234646894326487758345234576484568567956 -- 4.491632399999999
print(timeit.timeit(time_, number=1000000))
# num = 1234567890 -- 9.8509878
# num = 1234567890234646894326487758345234576484568567956 -- 45.6520757