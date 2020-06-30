''' Данная задача была на экзамене по программированию на питоне в 19-20 гг

    Файл состоит из строк, которве состоят из букв и цифр.
    Файл сортируюется по цифрам(числам), при этом, если в строке
    есть буквы заглавные, то такие строчки остаются на месте и не подчиняются
    сортировки.
'''


''' Функция определяет есть ли заглавные буквы в строке '''
def buk(u):
    w = ''
    kol = 0
    KOL = 0
    for r in u:
        if 'A'<=r<='Z' or 'a'<=r<='z':
            kol+=1
            if 'A'<=r<='Z':
                KOL+=1
    if kol==KOL:
        return True
    else:
        return False

''' Функция извлекает числа из строки '''    
def chicla(u):
    w =''
    for r in u:
        if '0'<=r<='9':
            w += r       
    return w

''' Функция сортирует строки по значению в ней чисел'''
def sortt(f):
    F = open(f)
    h = open('H.txt','w')
    h1 = open('H1.txt','w')
    while F.readline():
        F.seek(0)
        a = F.readline()
        ooo = buk(a)
        Fq = chicla(a)
        minf = int(Fq)
        for line in F:
            lin = chicla(line)
            if int(lin)<minf and buk(line)!=True:
                minf = int(lin)
        F.close()        
        F = open(f)
        for line in F:
            lin = chicla(line)
            if int(lin)==minf and buk(line)==False:
                h.write(line)
            elif buk(line)!=True:
                h1.write(line)
        h1.close()
        h1 = open('H1.txt')
        F.close()
        F = open(f,'w')
        for line in h1:
            F.write(line)
        F.close()
        h1.close()
        F = open(f)
        h1=open('H1.txt','w')
    F.close()
    h.close()
    h1.close()
    h = open('H.txt')
    F = open(f,'w')
    for line in h:
        F.write(line)
    F.close()
    h.close()

''' Функция печатает данный файл '''
def printt(f):
    F = open(f)
    print(f,':')
    for i in F:
        print(i,end='')
    F.close()    



bb = open('bb.txt','w')
f = open('P.txt')
for i in f:
    bb.write(i)
bb.close()
printt('bb.txt')

sortt('P.txt')
k = l = 0
bb = open('bb.txt')
p = open('P.txt','w')
h = open('H.txt')
for line in bb:
    if buk(line):
        p.write(line)
    else:
        p.write(h.readline())
        
p.close()


printt('H.txt')
printt('P.txt')
