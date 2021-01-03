# Azamat Khankhodjaev
# 03.01.2021
# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
char_1_2 = input('Введите 2 буквы: ')
chars = 'abcdefghijklmnopqrstuvwxyz'
chr_1, chr_2 = char_1_2.split()
if chr_1 in chars and chr_2 in chars:
    pos_1, pos_2 = chars.find(chr_1)+1, chars.find(chr_2)+1
    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1
    print(pos_1, pos_2, (pos_2-pos_1-1))
else:
    print('Символ не найден')
