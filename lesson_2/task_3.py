def recursion(num, turn):
    if num != 0:
        return recursion(num // 10, turn * 10 + num%10)
    return turn

print(recursion(int(input('Введите любое целое число: ')), 0))

