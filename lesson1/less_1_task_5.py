# Azamat Khankhodjaev
# 03.01.2021
# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num_char = input('Введите номер буквы: ')
const = 96
num_char = int(num_char)
if num_char > 0 and num_char < 27:
    print(chr(num_char+const))
else:
    print('Значение вне диапозона (1-26)')

