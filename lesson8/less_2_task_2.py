# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 9, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start, end):
    begin = start
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float('inf')] * lenght
    parent = [-1] * lenght

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    way = deque([end])
    i = end


    while parent[i] != begin:
        if parent[i] == -1:
            print("Путь не найден")
            return []
        way.appendleft(parent[i])
        i = parent[i]

    way.appendleft(begin)

    return way


print(*dijkstra(g, 1, 2))
