import timeit, cProfile

def turn(num):
    decision = list(num)
    for i in range(len(num) // 2):
        dic_i = decision[i]
        decision[i] = decision[len(num) - i - 1]
        decision[len(num) - i - 1] = dic_i
    return ''.join(decision)

result = turn(input('Введите любое целое число: '))

print(int(result))