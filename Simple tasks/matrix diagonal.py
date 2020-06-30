# Программа выводит элементы матрицы R под главной диагональю, над ней отдельно
R = [['r','a','y','a','a','a','a','a'],
     ['n','r','a','y','a','a','a','a'],
     ['m','n','r','a','y','a','a','a'],
     ['n','m','n','r','a','y','a','a'],
     ['n','n','m','n','r','a','y','a'],
     ['n','n','n','m','n','r','a','y'],
     ['n','n','n','n','m','n','r','a'],
     ['n','n','n','n','n','m','n','r']]

n = int(input("Введите количество строк и столбцов(одно число): "))
#R = []
print('Изначальная матрица R')
for i in range(n):
    for j in range(n):
        print(R[i][j], end = ' ')
    print()    
print()
k = n-1
p = 0

print('Элементы над главной диагональю')
for y in range(n):
    i = k
    j = n-1
    count = 0
    print(' '*y, end = '')
    while count<n-p:
        print(R[i][j], end = ' ')
        i -= 1
        j -= 1
        count += 1
    p += 1
    print()    
    k -= 1
print()
k = 0

print('Элементы под главной диагональю')
for y in range(n):
    i = k
    j = count = 0
    print(' '*y, end = '')
    while count<n-k:
        print(R[i][j], end = ' ')
        i += 1
        j += 1
        count += 1
    print()    
    k += 1    
print()
