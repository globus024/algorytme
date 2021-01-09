# Collection Deque
from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 5, 4, 9, 0])
print(a, b, c, sep='\n')
# deque([])
# deque(['a', 'b', 'c', 'd', 'e', 'f'])
# deque([1, 2, 3, 5, 4, 9, 0])
print('*' * 70)
b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=6)
print(b, c, sep='\n')
c.clear()
d = deque([i for i in range(5)])
d.append(1)
d.appendleft(5)
print(d)
d.extend([1, 2, 3, 4])
d.extendleft([11, 12, 13])
print(d)
# deque(['d', 'e', 'f'], maxlen=3)
# deque([4, 5, 6, 7, 8, 9], maxlen=6)
# deque([5, 0, 1, 2, 3, 4, 1])
# deque([13, 12, 11, 5, 0, 1, 2, 3, 4, 1, 1, 2, 3, 4])
print("-" * 70)
f = deque([i for i in range(10)], maxlen=7)
print(f)
x = f.pop()
y = f.popleft()
print(x, y, f, sep='\n')
# deque([3, 4, 5, 6, 7, 8, 9], maxlen=7)
# 9
# 3
# deque([4, 5, 6, 7, 8], maxlen=7)
print('*' * 70)
g = deque([i for i in range(5)], maxlen=9)
print(g)
g.append(2)
print(g.count(2))
print(g.index(2))
g.insert(2, 6)
print(g)
g.reverse()
print(g)
g.rotate(2)
print(g)
# deque([0, 1, 2, 3, 4], maxlen=9)
# 2
# 2
# deque([0, 1, 6, 2, 3, 4, 2], maxlen=9)
# deque([2, 4, 3, 2, 6, 1, 0], maxlen=9)
# deque([1, 0, 2, 4, 3, 2, 6], maxlen=9)
# Собрать в массив отрицательные и положительные элементы
print("-+" * 70)
import random

a = [random.randint(-100, 100) for _ in range(20)]
print(a)
d = deque()
for i in a:
    if i > 0:
        d.append(i)
    else:
        d.appendleft(i)
print(d)
# [90, -69, -15, -96, 45, -38, -12, -16, -74, -92, 13, 55, 26, 92, -22, 64, 57, -81, -17, 63]
# deque([-17, -81, -22, -92, -74, -16, -12, -38, -96, -15, -69, 90, 45, 13, 55, 26, 92, 64, 57, 63])
# 10 последних жобавленых строк в дщп файл

with open('log_ip.txt', 'r', encoding='utf-8') as f:
    last_ten = deque(f, 10)

print(last_ten)
# deque(['192.168.0.9\n', '192.168.0.5\n', '192.168.0.4\n', '192.168.0.2\n', '192.168.0.3\n', '192.168.0.1\n', '192.168.0.7\n', '192.168.0.2\n', '192.168.0.6\n', '192.168.0.5'], maxlen=10)