# Azamat Khankhodjaev
# 09.01.2021
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import Counter, deque


def sixteen(val: int):
    sixteen = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if val < 16:
        if val > 9 and val < 16:
            return sixteen[val]
        else:
            return val


def dec(val):
    dec = Counter(
        {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
         'E': 14, 'F': 15})

    return dec[val]


def dec_to_sixteen(val):
    b = val
    d = []
    while b > 0:
        a = b
        b = b // 16
        d.append(a % 16)

    d.reverse()
    f = ''
    for i in d:
        f = f'{f}{sixteen(i)}'
    return f


def sixteen_to_dec(val):
    d = []
    l = len(val)
    summ = 0
    for i in val:
        l -= 1
        num = dec(i)
        summ += num * (16 ** l)

    return summ


if __name__ == '__main__':
    print('Калкулятор для шестнадцатеричной системы')
    s = input('Введите 2 шестнадцатеричного числа через пробел: ').upper()
    sixteen1, sixteen2 = s.split()
    sixteen_deque1, sixteen_deque2 = deque(sixteen1), deque(sixteen2)

    op = int(input('Суммировать - 1, Умножить - 2 : '))
    res_sixteen =''
    if op == 1:
        summ = sixteen_to_dec(sixteen1) + sixteen_to_dec(sixteen2)
        res_sixteen = dec_to_sixteen(summ)
    elif op == 2:
        dot = sixteen_to_dec(sixteen1) * sixteen_to_dec(sixteen2)
        res_sixteen = dec_to_sixteen(dot)
    else:
        print('Неправильная операция')
    sixteen_deque_res = deque(res_sixteen)
    print(list(sixteen_deque1), list(sixteen_deque2),list(sixteen_deque_res))