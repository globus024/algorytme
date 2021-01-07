# Azamat Khankhodjaev
# 07.01.2021
# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)

# 1 method
def eratosfen_sieve(n,pos):

    n_list = [i for i in range(n)]
    n_list[1] = 0

    for i in range(2, n):
        if n_list[i] != 0:
            j = i * 2
            while j < n:
                n_list[j] = 0
                j += i
    res = [i for i in n_list if i != 0]

    return res[pos]


# 2 method
import math
def simple_number(n,pos):

    n_list = [i for i in range(n) if i > 1]
    simple =[];
    for i in n_list:
        d = int(math.sqrt(i))
        f=0
        for j in range(2,d+1):
            if i %j ==0:
                f=1
                continue
        if f == 0:
            simple.append(i)
    return simple[pos]


# метод тестирование
def test_most_number(func):
    test_list = [2, 3, 5, 7]

    for k, t in enumerate(test_list):
        assert t == func(100,k)
        print(t, f'OK {func.__name__}')
    print('-' * 10)

#
test_most_number(eratosfen_sieve)
test_most_number(simple_number)

# 2 OK eratosfen_sieve
# 3 OK eratosfen_sieve
# 5 OK eratosfen_sieve
# 7 OK eratosfen_sieve
# ----------
# 2 OK simple_number
# 3 OK simple_number
# 5 OK simple_number
# 7 OK simple_number
# --------------------------------------------------

# timeit
# 1 method eratosfen_sieve(10000)

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.eratosfen_sieve(1000,5)"
# 1000 loops, best of 5: 264 usec per loop

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.eratosfen_sieve(10000,5)"
# 1000 loops, best of 5: 2.92 msec per loop

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.eratosfen_sieve(20000,5)"
#1000 loops, best of 5: 6.3 msec per loop

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.eratosfen_sieve(100000,5)"
# 1000 loops, best of 5: 33 msec per loop
# --------------------------------------------

# 2 method simple_number(1000)

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.simple_number(1000,5)"
# 1000 loops, best of 5: 1.44 msec per loop

# python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.simple_number(2000,5)"
# 1000 loops, best of 5: 3.66 msec per loop

# >python -m timeit -n1000 -s "import less_4_task_2" "less_4_task_2.simple_number(4000,5)"
# 1000 loops, best of 5: 9.59 msec per loop

# -----------------------------------------------

# cProfile

# method 1
import cProfile
cProfile.run('eratosfen_sieve(100000,5)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.001    0.001    0.035    0.035 <string>:1(<module>)
# 1    0.028    0.028    0.034    0.034 less_4_task_2.py:18(eratosfen_sieve)
# 1    0.003    0.003    0.003    0.003 less_4_task_2.py:20(<listcomp>)
# 1    0.003    0.003    0.003    0.003 less_4_task_2.py:29(<listcomp>)
# 1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# method 2

cProfile.run('simple_number(100000,5)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.001    0.001    1.052    1.052 <string>:1(<module>)
# 1    1.031    1.031    1.050    1.050 less_4_task_2.py:36(simple_number)
# 1    0.006    0.006    0.006    0.006 less_4_task_2.py:38(<listcomp>)
# 1    0.000    0.000    1.052    1.052 {built-in method builtins.exec}
# 99998    0.013    0.000    0.013    0.000 {built-in method math.sqrt}
# 9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}