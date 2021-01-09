# Counter collection
from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'red': 1, 'blue': 2})
d = Counter(cats=4, dogs=2)
print(a, b, c, d, sep='\n')
print(b['z'])
print(b)
b['z'] = 0
print(b)
print('*' * 50)
print(list(b.elements()))
# Counter()
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'blue': 2, 'red': 1})
# Counter({'cats': 4, 'dogs': 2})
# 0
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'z': 0})
# **************************************************
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# Часто встречающиеся объекты (most existed element 2)
print(b.most_common(2))
# [('a', 5), ('b', 2)]
g = Counter(a=2, b=3, c=-4, f=3)
f = Counter(a=1, b=2, c=4, d=-1)
g.subtract(f)
print(g)
f.subtract(g)
print(f)
f.clear()
print(f)
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
# [('a', 5), ('b', 2)]
# Counter({'f': 3, 'a': 1, 'b': 1, 'd': 1, 'c': -8})
# Counter({'c': 12, 'b': 1, 'a': 0, 'd': -2, 'f': -3})
# Counter()
print("--" * 50)
x = Counter(a=1, b=5, c=1)
y = Counter(b=2, c=5, a=3, d=4)
print(x + y, ' x+y')
print(x - y,' x-y')
print(x & y,' x&y')
print(x | y, ' x|y')
# Counter({'b': 7, 'c': 6, 'a': 4, 'd': 4})  x+y
# Counter({'b': 3})  x-y
# Counter({'b': 2, 'a': 1, 'c': 1})  x&y
# Counter({'b': 5, 'c': 5, 'd': 4, 'a': 3})  x|y

# Унарные операции в коллекции
z = Counter(a=1, b=-2, c=-3, d=3)
print("--" * 50)
print(+z)
# Берёт только положительные значения
# Counter({'d': 3, 'a': 1})
print(-z)
# Берёт только отрицательные значения но меняет знак
# Counter({'c': 3, 'b': 2})

