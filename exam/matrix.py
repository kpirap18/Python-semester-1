''' Данная функция сортирует матрицу по среднему арифметическому
    стоблцов. И определяет, где больше числе кратных 5
    в нижней треугольной матрице или же в верхней треугольной матрице
'''    

def sortt(a1,n1,m1):
    for p in range(m1):
        mins = 0
        f = False
        for h in range(n1):
            if a1[h][p]>0:
                mins+=a1[h][p]
        mins = mins/n1
        '''print('mins',mins)'''
        for i in range(p,m1):
            s = 0
            for j in range(n1):
                if a1[j][i]>0:
                    s += a1[j][i]
            s = s/n1    
            if s<mins:
                mini = i
                f = True
        '''print(mini)'''
        if f:
            for l in range(n1):
                a1[l][p],a1[l][mini] = a1[l][mini],a1[l][p]
            

def printt(prr):
    if prr ==0:
        print('вниз')
    elif prr==1:
        print('поравно')
    elif prr==2:
        print('нет')
    elif prr==3:
        print('вверх')


n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))
print('Введите матрицу по cтроке(символы через пробел): ')
a=[[0]*m]*n
for i in range(n):
    a[i] = list(map(float,input().split()))

sortt(a,n,m)    
  
for t in a:
    print(t)
    
for i in range(m):
    sr = 0
    for j in range(n):
        if a[j][i]>0:
            sr += a[j][i]
    sr = sr/n
    print('{:3.1f}'.format(sr),end = ' ')

k1 = 0
k2 = 0
for i in range(n):
    for j in range(m):
        if a[i][j]%5 == 0:
            if i<=j:
                k1+=1
            else:
                k2+=1
print()
if k1<k2:
    pr = 0
elif k1==k2 and k1==k2==0:
    pr = 1
elif k1==k2 and k1!=0:
    pr = 2
else:
    pr = 3
    
printt(pr)            
        
            
        
