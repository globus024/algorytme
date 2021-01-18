# Azamat Khankhodjaev
# 18.01.2021
# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество
# различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
from collections import defaultdict


def hash_func(string: str) -> str:
    # Константа для верхнего регистра
    # 10 начинается для определения позиции закодираваной строке
    c = 37
    alfa = defaultdict(list, {
        ' ': 10,
        'a': 11,
        'b': 12,
        'c': 13,
        'd': 14,
        'e': 15,
        'f': 16,
        'g': 17,
        'h': 18,
        'i': 19,
        'j': 20,
        'k': 21,
        'l': 22,
        'm': 23,
        'n': 24,
        'o': 25,
        'p': 26,
        'q': 27,
        'r': 28,
        's': 29,
        't': 30,
        'u': 31,
        'v': 32,
        'w': 33,
        'x': 34,
        'y': 35,
        'z': 36,

    })
    codes = ''

    for s in string:
        if s.upper() == s:
            s_lower = s.lower()
            if (alfa[s_lower]):
                codes = f'{codes}{str(alfa[s_lower] + c)}'
        else:
            if alfa[s]:
                codes = f'{codes}{str(alfa[s])}'

    return codes


def find_in_str(string: str, sub_string: str) -> int:
    assert len(string) > 0 and len(sub_string) > 0, 'Cтроки не могут быть пустыми'
    assert len(string) > len(sub_string), 'Длина подстроки больше строки'
    hash1 = hash_func(string)
    hash2 = hash_func(sub_string)

    if hash2 in hash1:
        return hash1.index(hash2) // 2
    else:
        return -1


# Метод для сравнения результата
def find_in_str2(string: str, sub_string: str) -> int:
    assert len(string) > 0 and len(sub_string) > 0, 'Cтроки не могут быть пустыми'
    assert len(string) > len(sub_string), 'Длина подстроки больше строки'
    p = -1
    if sub_string in string:
        p = string.index(sub_string)

    return p


# Проверка
if __name__ == '__main__':
    string = input('Ввелите строку: ')
    sub_string = input('Ввелите подстроку: ')
    pos = find_in_str(string, sub_string)
    if pos >= 0:
        print(f'Строка найдена в позиции {pos}')
    else:
        print(f'Строка не найдена')

    pos2 = find_in_str2(string, sub_string)
    if pos == pos2:
        print('Оба метода дают один результат')
    else:
        print('Методы не равны')
