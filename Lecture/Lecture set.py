print('3.3+5.7')
print('     Объединение множеств')
a = {7,2,'азбуз',3,4}
b = {9,'яблоко',2,3}
print('объединение множеств')
c = a|b
print(c)
print()

d = a.union(b)
print(d)
d1 = b.union(a)
print(d1)
print()

print('Расширение множеств')
a.union(b)
print(a)
b = b|{'груша'}
print(b)
print()

print('      Пересечение множеств')
a = {7,2,'спартак',3,4}
b = {9,'ЦСКА',2,3}
print('персечение пможеств')
c = a&b
print(c)
print()

d = a.intersection(b)
print(d)
d1 = b.intersection(a)
print(d1)
print()

print('расширение исхожных множеств')
a.intersection_update(b)
print(a)
b = b|{'Динамо'}
print(b)
print()

print('Разность множеств')
a = {7,2,'курск',3,4}
b = {9,'Орел',2,3}
print('Разность множеств')
c = a-b
print(c)
print()

d = a.difference(b)
print(d)
d1 = b.difference(a)
print(a)
print()

print('расширение исх множества')
a.difference_update(b)
print(a)
b = b|{'сочи'}
print(b)
print()

print('симметри азность мноеж')
a = {7,2,'окунь',3,4}
b = {9,'карп',2,3}
print('сим разн мн')
c = a^b
print(a)
print()

d = a.symmetric_difference(b)
print(d)
d1 = b.symmetric_difference(a)
print(d1)
print()

a.symmetric_difference_update(b)
print(a)
b = b|{'судак'}
print(b)
