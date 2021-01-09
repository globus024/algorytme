from collections import ChainMap

d_1 = {'a': 12, 'b': 13, 'c': 6}
d_2 = {'a': 10, 'b': 1, 'c': 51, 'd':122}
d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['c'] = 12
print(d_2, d_map, sep='\n')
print(d_map['a'], d_map['d'])
print('*-'*30)
# ChainMap({'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 51, 'd': 122})
# {'a': 10, 'b': 1, 'c': 12, 'd': 122}
# ChainMap({'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 12, 'd': 122})
# 12 122
x = d_map.new_child({'a':122,'b':133, 'c':92, 'd':32})
print(x)
print(x.maps[0])
print(x.maps[-1])
print(x.parents)
print('*'*70)
# ChainMap({'a': 122, 'b': 133, 'c': 92, 'd': 32}, {'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 12, 'd': 122})
# {'a': 122, 'b': 133, 'c': 92, 'd': 32}
# {'a': 10, 'b': 1, 'c': 12, 'd': 122}
# ChainMap({'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 12, 'd': 122})
# **********************************************************************
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] =1
print(y)
# ChainMap({}, {'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 12, 'd': 122})
# 12
# ChainMap({'a': 1}, {'a': 12, 'b': 13, 'c': 6}, {'a': 10, 'b': 1, 'c': 12, 'd': 122})
