import numpy as np
print('Вид поля')
dt = np.dtype([('name','U10'),('height', float),('age',int)])
print(dt,'\n')

print('Исходный список')
gruppa = [('Саша',1.8,16),('Ваня',1.85,16),('Никита',1.76,18)]
print(gruppa)
print()

print('Сфомировать список')
a = np.array(gruppa,dtype = dt)
print(a)
print()

print('Отсортированный список по росту')
print(np.array(a,order = 'height'))
print()

print('ДЗугой вариант задания данных и сортировка по name')
a = np.array([('Саша',1.8,16),('Ваня',1.85,16),('Никита',1.76,18)],\
             dtype[('name','U10'),('height', float),('age',int)])
print(a)
print(np.sort(a,order = 'name'))

print('\n\n\n')
print('Сортировка по полю age и при их равенстве по полю height')
print(np.sort(a,order = ['age','height']))
