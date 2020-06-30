# Козлова Ирина ИУ7-12
# расшифровка шифра из файла

# Перевод из 10  2
def from_10_to_2(V):
    B = []
    for i in range(n):
        k = bin(int(V[i]))
        k = k[2:]
        g = len(k)
        k = '0'*(8-g)+k
        #print(k)
        B.append(k)
    return(B)

# Расшифровка шифра из таблицы
def shifr(R):
    l =''
    k = 0
    for i in range(n):
        for j in range(n):
            if B_0_and_1[i][j] == '1':
                R.write(A[i][j])
                l += A[i][j]
                k += 1            
    # 2 четверть
    p = n-1
    for i in range(n):
        for j in range(n):
            if B_0_and_1[p][i] == '1':
                R.write(A[i][j])
                l += A[i][j]
                k += 1 
            p -= 1
        p = n-1
    # 3 четверть
    p = n-1
    a = 0
    for i in range(n):
        for j in range(n):
            if B_0_and_1[a][p] == '1':
                R.write(A[i][j])
                l += A[i][j]
                k += 1 
            a += 1
        p -= 1    
        a = 0
    # 4 четверть
    p = a = n-1
    for i in range(n):
        for j in range(n):
            if B_0_and_1[p][a] == '1':
                R.write(A[i][j])
                l += A[i][j]
                k += 1 
            a -= 1
        p -= 1
        a = n-1
    print('Зашифрованное сообщение:\n',l)

# Считывание данных из файла    
Shifr = open('shifr.txt','r')
v = Shifr.readline()
v = v.split()
n = len(v)
A = []
for i in range(n):
    s = Shifr.readline()
    s = s.split()
    A.append(s)
Shifr.close()

B_0_and_1 = from_10_to_2(v)
Rshifr = open('Rshifr.txt','w')
shifr(Rshifr)
Rshifr.close()
