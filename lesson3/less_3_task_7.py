# Azamat Khankhodjaev
# 05.01.2021
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

random_list = [random.randint(1, 10) for _ in range(10)]
print(random_list)
random_list.sort()
print(random_list[0:2])