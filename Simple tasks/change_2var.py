''' Программа меняет 2 переменные местами, не используя 3
    и возможностей питона.
'''    
x, y = map(int,input('Введите две переменные через пробел: ').split())
x = x+y
y = x-y
x = x-y
print(x,' ' ,y)