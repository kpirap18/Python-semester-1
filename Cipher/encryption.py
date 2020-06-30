# Козлова Ирина ИУ7-12
# Шифровальная таблица

from random import randint

# заполняет таблицу рандомными симвоами
def tabl_sim():
    A = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            k = randint(65,123)
            A[i][j] = chr(k)
    return(A)        

# Шифровальная таблица    
def tabl():
    A1 = [[0]*n for i in range(n)]
    B = [[0]*n for i in range(n)]
    k = 1
    # 1 четверть
    for i in range(n//2):
        for j in range(n//2):
            A1[i][j] = k
            B[i][j] = k
            k += 1
    # 2 четверть
    p = n//2-1
    for i in range(n//2):
        for j in range(n//2,n):
            A1[i][j] = B[p][i]
            p -= 1
        p = n//2-1
    # 3 четверть
    p = n//2-1
    a = 0
    for i in range(n//2,n):
        for j in range(n//2):
            A1[i][j] = B[a][p]
            a += 1
        p -= 1    
        a = 0
    # 4 четверть
    p = a = n//2-1
    for i in range(n//2,n):
        for j in range(n//2,n):
            A1[i][j] = B[p][a]
            a -= 1
        p -= 1
        a = n//2-1

    '''for i in A1:
        print(i)'''    
    return(A1)

# Матрица из 0 и 18
def rand_tabl():    
    B = [[0]*n for i in range(n)]
    ib = jb = -1
    pA = [i for i in range(1,17)]
    f = False
    k = 0
    i = 0

    while k!=n*n//4:
        p = randint(1,16)
        #print(p)
        if p in pA:
            if p in A_num_tabl[i]:
                ib = i
                jb = A_num_tabl[i].index(p)
                k += 1
                B[ib][jb]=1
                pA[pA.index(p)]=0
        if i==n-1:        
            i = 0
        else:
            i += 1
    ''''for i in B:
        print(i)'''
    return(B)            

# Перевод из 2 в 10
def transl_2v10():
    Vv = []
    for i in range(n):
        v = 0
        for j in range(n):
            v = v+2**(n-j-1)*B_0_and_1[i][j]
        Vv.append(v)
    return (Vv)

# Сам шифр(запись сообщения в таблицу)
def shifr(A):
    k = 0
    for i in range(n):
        for j in range(n):
            if B_0_and_1[i][j] == 1:
                if k < len(sen_shifr):
                    A[i][j] = sen_shifr[k]
                    k += 1
                
    # 2 четверть
    p = n-1
    for i in range(n):
        for j in range(n):
            if B_0_and_1[p][i] == 1:
                if k < len(sen_shifr):
                    A[i][j] = sen_shifr[k]
                    k += 1
            p -= 1
        p = n-1
    # 3 четверть
    p = n-1
    a = 0
    for i in range(n):
        for j in range(n):
            if B_0_and_1[a][p] == 1:
                if k < len(sen_shifr):
                    A[i][j] = sen_shifr[k]
                    k += 1
            a += 1
        p -= 1    
        a = 0
    # 4 четверть
    p = a = n-1
    for i in range(n):
        for j in range(n):
            if B_0_and_1[p][a] == 1:
                if k < len(sen_shifr):
                    A[i][j] = sen_shifr[k]
                    k += 1
            a -= 1
        p -= 1
        a = n-1
    return(A) 
# Основная программа
n = int(input('Введите размерность матрицы(n): '))
A_sim_tabl = tabl_sim()
#for i in A_sim_tabl:
#    print(i)
A_num_tabl = tabl()
B_0_and_1 = rand_tabl()
sen_shifr = input('Напечатайте сообщение без пробелов: ')
A_shifr = shifr(A_sim_tabl)
v10 = transl_2v10()
Shifr = open('shifr.txt','w')
print('Вектор: ')
for i in v10:
    print(i,end=' ')
    Shifr.write(str(i))
    Shifr.write(' ')
Shifr.write('\n')    
print()
print('Матрица c cообщением: ')
for i in range(n):
    for j in range(n):
        print(A_shifr[i][j],' ', end = '')
        Shifr.write(str(A_shifr[i][j]))
        Shifr.write(' ')
    Shifr.write('\n') 
    print()
Shifr.close()    
print('Матрица дырок: ')    
for i in range(n):
    for j in range(n):
        print(B_0_and_1[i][j],' ', end = '')
    print()
