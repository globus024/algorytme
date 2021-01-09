from collections import namedtuple

n = ('Kuzya', 'bos', 1200, 12)
print(n[3])
# 12
Named_Personal = namedtuple('Named_Personal', 'name position sallary agility')
named_n = Named_Personal('Kuzya', 'bos', 1200, 12)
print(named_n)
# Named_Personal(name='Kuzya', position='bos', sallary=1200, agility=12)
print(named_n.name)
# Kuzya

a = ['name', 'position', 'sallary', 'agility']
Named_Personal1 = namedtuple('Named_Personal1', a, rename=True)
named_n = Named_Personal1('Buri', 'staff', agility=1.2, sallary=300)
print(named_n.sallary)
# 300
print('*' * 70)
Point = namedtuple('Point', 'x,y,z')
print(Point)
t = [1, 22, 15]
p1 = Point._make(t)
print(p1)
d2 = p1._asdict()
print(d2)
p2 = p1._replace(x=120)
print(p2)
print(p2._fields)
print('*'*50)
New_point = namedtuple('New_point', 'x y z', defaults=[0,0,0])
print(New_point)
dct = {'x':10,'y':12,'z':16}
p3 = New_point(**dct)
print(p3)


