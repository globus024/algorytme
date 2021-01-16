# Azamat Khankhodjaev
# 15.01.2021
# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# graph = [
#     [0, 1, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
# ]
from collections import deque

graph = {
    0: (1, 3, 4),
    1: (2, 5),
    2: (1, 6),
    3: (1, 5, 7),
    4: (2, 6),
    5: (6,),
    6: (5,),
    7: (6,)
}
is_visited = [False for _ in range(8)]
start = 0

def tt(graph, start, is_visited, deq):
    start_list  = graph[start]

    deq.append(start)
    for i in start_list:
        if is_visited[i]:
            continue
        is_visited[i] = True
        tt(graph, i, is_visited, deq)

    return deq

deq = deque()
res =tt(graph, 0, is_visited, deq)
print(res)
