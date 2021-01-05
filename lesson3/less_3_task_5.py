# Azamat Khankhodjaev
# 05.01.2021
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

random_list = [random.randint(-20, 20) for _ in range(51)]
print(random_list)
max_neg = float('-inf')
pos =-1
for k,v in enumerate(random_list):
    if v >= 0:
        continue
    print(v)
    if v > max_neg:
        max_neg = v
        pos = k
print(f'*'*30)
print(max_neg, pos)
