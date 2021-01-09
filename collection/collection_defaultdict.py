from collections import defaultdict

a = defaultdict()
print(a)
# defaultdict(None, {})
s = 'dsdadgadkjdgasvdad v fuahaegajkfsdfnsdf fn sdfsdfns fnwsfnsd kfnwfnsd fnsfnsf sfsdkf'
b =defaultdict(int)
for i in s:
    b[i] +=1
print(b)
# defaultdict(<class 'int'>, {'d': 14, 's': 14, 'a': 7, 'g': 3, 'k': 4, 'j': 2, 'v': 2, ' ': 8, 'f': 16, 'u': 1, 'h': 1, 'e': 1, 'n': 9, 'w': 2})
list_1 = [('kiska',1),('pesil',2),('kiska',3),('zayka',5),('pesil',2)]
b = defaultdict(list)
for k,v in list_1:
    b[k].append(v)
print(b)
# defaultdict(<class 'list'>, {'kiska': [1, 3], 'pesil': [2, 2], 'zayka': [5]})
list_1 = [('kiska',1),('pesil',2),('kiska',3),('zayka',5),('pesil',2)]
b = defaultdict(set)
for k,v in list_1:
    b[k].add(v)
print(b)
# defaultdict(<class 'set'>, {'kiska': {1, 3}, 'pesil': {2}, 'zayka': {5}})
f = defaultdict(lambda :'unkhown')
f.update(rex='pes',kasper='kotek')
print(f)
print(f['kasper'])
print(f['zayka'])
# defaultdict(<function <lambda> at 0x0000022A4674C430>, {'rex': 'pes', 'kasper': 'kotek'})
# kotek
# unkhown
