# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# Первый способ (за основу взят код из урока 2):

num = int(input('Введите порядковый номер простого числа: '))
size = num * 100
lis = [i for i in range(size)]

lis[1] = 0
for i in range(2, size):
    if lis[i] != 0:
        j = i + i
        while j < size:
            lis[j] = 0
            j += i

print(lis)
list_2 = []
for i in lis:
    if i != 0:
        list_2.append(i)
print(list_2)
print(f'Простое число: {list_2[num - 1]}')




