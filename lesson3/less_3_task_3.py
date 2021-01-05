# Azamat Khankhodjaev
# 05.01.2021
#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
random_list = [random.randint(1,100) for _ in range(51)]
print(random_list)
max = float('inf')
min =  float('-inf')

for k,v in enumerate(random_list):
    if v > min:
        min =v
        min_pos = k
    if v < max:
        max =v
        max_pos =k

max_value = random_list[max_pos]
min_value = random_list[min_pos]
random_list[max_pos],random_list[min_pos] = min_value,max_value
print(random_list)
