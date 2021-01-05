# Azamat Khankhodjaev
# 05.01.2021
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

random_list = [random.randint(1, 10) for _ in range(10)]
random_list.sort()
print(random_list)

prev_min = 0
prev_max = 0
sum_mid = 0
max_len = len(random_list)-1

for k, v in enumerate(random_list):
    if k == 0:
        prev_min = v
        prev_max = random_list[max_len]
        max_len -= 1
        continue
    if random_list[max_len] == prev_max:
        max_len -= 1

    if v != prev_min and k < max_len+1:
        sum_mid += v

print(sum_mid)
