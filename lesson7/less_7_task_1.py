# Azamat Khankhodjaev
# 13.01.2021
# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


# import cProfile
# from memory_profiler import profile

# Оптимизированный пузырковый метод.
# За один проход второго цикла смешается максимальный элемент в право, также сразу определяется минимальный элемент и заменяется
# на позицию с кjторой идёт отчёт. После этого передвигаю цикл как с начала так и с конца. Таким образом цикл уменьшает количество проходов
# 2 рого цикла в два раза
# @profile()
def buble_sort(a):
    n = 1
    l = len(a)
    pos = 0
    min = float('inf')
    min_pos = 0
    while n < l:
        for i in range(pos, l - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            if a[i] < min:
                min = a[i]
                min_pos = i
        a[pos], a[min_pos] = a[min_pos], a[pos]
        min = a[l - 1]
        pos += 1
        n += 1
    return a


a = [i for i in range(-100, 101)]
random.shuffle(a)

print(a)
print(buble_sort(a))


# [-58, -10, 90, 60, 71, -21, 73, -76, 43, -67, 13, 1, -33, 35, 68, 48, 96, -26, -24, -63, -90, -51, 42, 47, -65, -16, -35, 82, -84, 40, 97, -64, 32, -20, 4, 53, -81, -45, -92, -43, -56, -98, 77, -31, -50, -18, 18, 61, 22, 31, 52, 20, 57, 83, 75, 19, -39, -29, -13, -66, 28, 99, 49, -77, 29, -96, 74, 7, 81, -74, 8, -60, -15, 44, -12, 23, -75, 86, -4, -69, -78, 34, 58, 41, 14, -44, 45, -57, 5, 16, 51, 21, 87, 54, 27, 39, -89, 50, 85, -3, -28, 94, -37, -47, -32, 91, 56, -36, 25, 24, -70, -55, -72, -86, -83, 69, -68, 89, 59, -79, 65, -62, 33, -61, -94, -11, -41, -6, 98, 78, -85, -30, 70, 46, 36, -9, 10, -100, 30, 80, 38, 95, 72, -22, -23, -38, -53, -2, 88, 67, -73, 2, -17, -14, 15, 11, -99, 17, -93, 92, 3, -42, -52, -46, -27, 9, -95, 37, -97, 55, -87, -7, 12, -91, -40, 100, -49, -5, 63, -88, 6, 76, -71, 0, -82, -34, -1, -8, -25, -54, 84, 93, -59, -19, 66, 26, -48, 64, 62, 79, -80]
# [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, 99, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100]


# (base) D:\geekbrains\algorytme\lesson7>python -m timeit -n1000 -s "import less_7_task_1" "less_7_task_1.buble_sort()

# range(-100,100)
# 1000 loops, best of 5: 2.22 msec per loop

# range(-1000,1000)
# 100 loops, best of 5: 240 msec per loop

# Обычный пузырковый метод
def buble_sort2(a):
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

        n += 1
    return a

# timeit
# (base) D:\geekbrains\algorytme\lesson7>python -m timeit -n1000 -s "import less_7_task_1" "less_7_task_1.buble_sort2()

# range(-100,100)
# 1000 loops, best of 5: 2.88 msec per loop

# range(-1000,1000)
# 100 loops, best of 5: 321 msec per loop
