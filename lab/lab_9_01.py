''' Программа записывает файл V в файл Т в обратном порядке'''
try:
    V = open('V','r')
except FileNotFoundError:
        print('Создайте файл')
        exit
else:
    T = open ('T','w')
    k = 0
    for line in V:
        k += 1   
    V = open('V','r')
    r = k
    for i in range(r):
        p = 0
        V = open('V','r')
        for line in V:
            p += 1
            y = line
            if p == k:
                T.write(y)
                k -= 1
    V.close()
    T.close()
