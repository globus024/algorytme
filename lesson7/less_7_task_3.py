# Azamat Khankhodjaev
# 13.01.2021
# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

def midle_element(array):
    for f in array:
        right_pos, left_pos = 0, 0
        for i in array:
            if f > i:
                right_pos += 1
            else:
                right_pos -= 1
        if right_pos == 1:
            return f


m = 28
n = (2 * m) + 1
array = [i for i in range(n)]
random.shuffle(array)

print(midle_element(array))
