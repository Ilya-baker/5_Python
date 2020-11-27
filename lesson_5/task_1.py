# Задача 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

num_company = int(input('Введите количество компаний: '))
company = [i for i in range(num_company)]
profit = [i for i in range(num_company)]
c = Counter()
j = 0

while j < num_company:
    company[j] = str(input(f'Введите название {j + 1} компании: '))
    profit[j] = float(input('Заработок за 1й квартал: ')) + \
                float(input('Заработок за 2й квартал: ')) + \
                float(input('Заработок за 3й квартал: ')) + \
                float(input('Заработок за 4й квартал: '))
    c.update({company[j]:profit[j]})
    j +=1

sum_profit = sum(profit)/num_company

print('======================================')
print(f'Средняя сумма дохода компаний: {sum_profit}')
print('======================================')
print('Компании с доходом выше среднего:')

for i in range(num_company):
    if c.most_common()[i][1] > sum_profit:
        print(c.most_common()[i][0], c.most_common()[i][1])

print('======================================')
print('Компании с доходом ниже среднего:')

for i in range(num_company):
    if c.most_common()[i][1] < sum_profit:
        print(c.most_common()[i][0], c.most_common()[i][1])