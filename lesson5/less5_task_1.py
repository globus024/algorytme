# Azamat Khankhodjaev
# 09.01.2021
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter
from functools import reduce

company_cnt = int(input('Введите данные о количестве предприятий: '))
sal_counter = Counter()
for i in range(1, company_cnt + 1):
    print(f'Предприятия № {i}')
    name = input('Наименование: ')
    income_list = input('Прибыль за каждый квартал (через пробел 4 значения): ').split()
    sum = reduce(lambda x, y: float(x) + float(y), income_list) / len(income_list)
    sal_counter[name] = sum

all_sum = 0
cnt = 0
v = list(sal_counter.values())
all_sum = reduce(lambda x, y: float(x) + float(y), v)
all_avg = all_sum / len(v)
comp_than_all_avg = [(k, v) for k, v in sal_counter.items() if all_avg < v]
comp_less_all_avg = [(k, v) for k, v in sal_counter.items() if all_avg > v]

print('*' * 70)
print(f'Средняя прибыль за год для всех предприятий: {all_avg}')
print('Предприятия, чья прибыль выше среднего:')
for k, v in comp_than_all_avg:
    print(f'Наименование предприятия: {k}, Средняя прибыль за год: {v}')
print('Предприятия, чья прибыль ниже среднего:')
for k, v in comp_less_all_avg:
    print(f'Наименование предприятия: {k}, Средняя прибыль за год: {v}')
