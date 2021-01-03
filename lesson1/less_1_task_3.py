# Azamat Khankhodjaev
# 03.01.2021
# 2. 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

print(
    f'программа, которая генерирует в указанных границах\n'
    f'1- случайное целое число, вводит 2 числа через  пробел (1 8)\n'
    f'2 -случайное вещественное число, вводит 2 числа через пробел (-1.4, 2.5) \n'
    f'3 - случайный символ, вводит через пробел последовательность символом (a,b,z,w,y)')
mode = int(input('Введите режимы 1-3: '))
range_xy = input('Введите диапазон через пробел: ')
if mode == 1 or mode == 2:
    range_x, range_y = range_xy.split()
    if mode == 1:
        range_x, range_y = int(range_x), int(range_y)
    else:
        range_x, range_y = float(range_x), float(range_y)

    if range_x > range_y:
        range_x, range_y = range_y, range_x
    if mode == 1:
        print(random.randrange(range_x, range_y + 1, 1))
    else:
        print(random.uniform(range_x, range_y))
else:
    if mode == 3:
        chars = range_xy.split()
        rnd_char = random.choice(chars)
        print(rnd_char)
    else:
        print('Режим выбран не верно')