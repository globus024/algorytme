# Azamat Khankhodjaev
# 05.01.2021
# 4. Определить, какое число в массиве встречается чаще всего.
# Решил сделать в одном цикле поэтому реализация мудрёная
import random

random_list = [random.randint(1, 20) for _ in range(51)]
random_list.sort()

print(random_list)
prev = 0
cnt = 0
prev_max = 0
max_el = 0
random_list.append(0)
for i,current in enumerate(random_list):
    if i == 0:
        cnt = 1
        prev = current
        continue
    if current != prev:
        if cnt >= prev_max:
            prev_max = cnt
            max_el = prev
        prev = current
        cnt = 1
    else:
        cnt += 1

print(max_el, prev_max)
