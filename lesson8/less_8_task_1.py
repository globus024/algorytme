# Azamat Khankhodjaev
# 15.01.2021
# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from collections import Counter

# Количество рукопожатий это напрафленный граф с нулевой вершина связана направлена на все вершины.
# Первая вершина направлена направлена n-1 вершины итд.
#    N =4
#    |0 1 1 1|
#    |0 0 1 1|
#    |0 0 0 1|
#    |0 0 0 0|

def handshake_graf(people_in: int):
    d = Counter();
    peoples = [1 for _ in range(people_in)]

    for i in range(people_in):
        peoples[i] = 0
        b = peoples[:]
        d.update(b)

    return d.get(1)

print(handshake_graf(5))
