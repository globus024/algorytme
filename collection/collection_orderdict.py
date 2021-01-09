from collections import OrderedDict

a = {'pesil': 2, 'kiska': 3, 'zayka': 1}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)
# OrderedDict([('kiska', 3), ('pesil', 2), ('zayka', 1)])
b = {'kiska': 3, 'zayka': 1, 'pesil': 2}
new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
print(new_b)
print(a == b)
print(new_a == new_b)
# OrderedDict([('zayka', 1), ('pesil', 2), ('kiska', 3)])
# True
# False
print('*' * 70)
new_b.move_to_end('zayka')
print(new_b)
new_b.move_to_end('zayka', last=False)
print(new_b)
# OrderedDict([('pesil', 2), ('kiska', 3), ('zayka', 1)])
# OrderedDict([('zayka', 1), ('pesil', 2), ('kiska', 3)])
new_b.popitem()
print(new_b)
# OrderedDict([('zayka', 1), ('pesil', 2)])
new_b.popitem(last=False)
print(new_b)
# OrderedDict([('pesil', 2)])
new_b.update(pesil=3, kiska=3, zayka=1)
print(new_b)
# OrderedDict([('pesil', 3), ('kiska', 3), ('zayka', 1)])
new_b['buryana'] = 1
new_b['pesil'] = 4
print(new_b)
# OrderedDict([('pesil', 4), ('kiska', 3), ('zayka', 1), ('buryana', 1)])
print('*' * 70)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)
for key in reversed(new_c):
    print(key, new_c[key])

# OrderedDict([('pesil', 2), ('kiska', 3), ('zayka', 1)])
# zayka 1
# kiska 3
# pesil 2
print('*' * 50)
from collections import deque, defaultdict

n = 1000
with open('log_ip.txt', 'r', encoding='utf-8') as f:
    d_list = deque(f, n)
print(d_list)
def_list = defaultdict(int)
order_list = OrderedDict()
for item in d_list:
    ip = item[:-1]
    if not ip.startswith('192.168'):
        def_list[ip] += 1
        order_list[ip] = 1
print(def_list, order_list, sep='\n')
order_list.update(def_list)

order_list = OrderedDict(sorted(order_list.items(), key=lambda x: x[1], reverse=True))
with open('log_sorted.txt', 'w', encoding='utf-8') as f:
    for k, v in order_list.items():
        f.write(f'{k} - {v}\n')
