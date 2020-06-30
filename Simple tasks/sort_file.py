''' Cортировка файла простыми вставками
     (даннуб программу можно улучшить и использовать всего 2 доп файла)
'''

''' Функция находит минимальный эдемент в файле, записывает
    его в результирующий файл, а так же записывает все значения,
    которые равны данному минимальному значению. Алгоритм повторяется
    тех пор, пока в исходном файле есть хотя бы одно число
'''

def Sorter(k1, U):  
    if k1==0:
        R = open('G')
    else:
        R = open('h')

    h2 = open('h2','w')
    for i in R:
        h2.write(i)
    h2.close()

    R.close()
    R = open('h2')
    minr = int(R.readline())
    count = 1
    for y in R:
        if int(y)<int(minr):
            minr = int(y)
            count = 1
        elif int(y)==int(minr):
            count += 1        
    for i in range(count):
        U.write(str(minr))
        U.write('\n')
    R.close()
    h = open('h','w')
    if k1==0:
        R = open('G')
    else:
        R = open('h2')
    lenh = 0
    for i in R:
        if int(i)!=int(minr):
            lenh += 1
            h.write(str(i))
    R.close()
    h.close()
    if lenh!=0:
        Sorter(1, U)

''' Функция принимающая значения для записи в файл '''
def inputV(R,n):
    print('Введите значения файла')
    for i in range(n):
        R.write(input())
        R.write('\n')

''' Функция выводит содержимое файла '''
def OutputP(R,o):
    if o==0:
        print('Исходный файл:')
    else:
        print('Преобразованный файл')
    for i in R:
        print(i,end='')
    


m = int(input('Введите m(кол-во элементов файла): '))
G = open('G','w')
inputV(G,m)
G.close()

G = open('G','r')
OutputP(G,0)
G.close()

U = open('U','w')
Sorter(0, U)
U.close()

U = open('U','r')
OutputP(U,1)
U.close()   
