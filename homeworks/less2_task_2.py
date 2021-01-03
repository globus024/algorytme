# Azamat Khankhodjaev
# 11.10.2020
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число'))
i, chet, ne_chet = 0, '', ''
while num > 0:
    a = num % 10
    if a % 2:
        chet =f'{a},{chet}'
    else:
        ne_chet = f'{a},{ne_chet}'
    num = num//10

print(f'Чётные {chet}')
print(f'Не чётные {ne_chet}')