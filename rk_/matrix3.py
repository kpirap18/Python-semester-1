# Матрица из центра спираль
n = int(input())
mat = [[0]*n for i in range(n)]
st, m = n*n, 0
# Заранее присваиваю значение центральному элементу
# матрицы
mat[n//2][n//2]=1
for v in range(n//2):
    #Заполнение верхней горизонтальной матрицы
    for i in range(n-m):
        mat[v][i+v] = st
        st-=1
        #i+=1
    #Заполнение правой вертикальной матрицы    
    for i in range(v+1, n-v):
        mat[i][-v-1] = st
        st-=1
        #i+=1
    #Заполнение нижней горизонтальной матрицы
    for i in range(v+1, n-v):
        mat[-v-1][-i-1] =st
        st-=1
        #i+=1
    #Заполнение левой вертикальной матрицы
    for i in range(v+1, n-(v+1)):
        mat[-i-1][v]=st
        st-=1
        #i+=1
    #v+=1
    m+=2
#Вывод результата на экран
for i in mat:
    print(*i)