# Azamat Khankhodjaev
# 03.01.2021
# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_str = input('Введите 3 числа с пробелом: ')
x, y, z = num_str.split()
x, y, z = int(x), int(y), int(z)
a = x
if not ((a > y and a < z) or (a > z and a < y)):
    if (y > a and y < z) or (y > z and y < a):
        a = y
    else:
        a = z


print(a)
