# Azamat Khankhodjaev
# 11.10.2020
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

numbers = input('Введите натуральные целые числа: ')+" "
number =''
sum = 0
prev_sum = 0
prev_number = ''
for num in numbers:
    if num.isdigit():
        sum += int(num)
        number =f'{number}{num}'
    else:
        if sum > prev_sum:
            prev_sum = sum
            prev_number = number
        sum,number =0,''


print(prev_number, prev_sum)