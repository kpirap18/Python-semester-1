def sortt(f):
    F = open(f)
    h = open('H.txt','w')
    h1 = open('H1.txt','w')
    while F.readline():
        F.seek(0)
        minf = int(F.readline())
        for line in F:
            if int(line)<minf:
                minf = int(line)
        F.close()        
        F = open(f)
        for line in F:
            if int(line)==minf:
                h.write(line)
            else:
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


def printt(f):
    F = open(f)
    print(f,':')
    for i in F:
        print(i,end='')
    F.close()    

sortt('P.txt')
sortt('P1.txt')
P = open('P.txt')
kp = 0
for i in P:
    kp += 1
P.close()
P1 = open('P1.txt')
kp1=0
for i in P1:
    kp1 += 1
P1.close()


P = open('P.txt')
P1 = open('P1.txt')
i = j = 0
P2 = open('P2.txt','w')
a = P.readline()
b = P1.readline()
while i <=(kp-1) and j<=(kp1-1):
    if a and b and int(a)<int(b):
        P2.write(a)
        i+=1
        if i==kp:
            break
        a = P.readline()
    elif  a and b and int(a)==int(b):
        P2.write(a)
        P2.write(b)
        i+=1
        j+=1
        if i==kp or j==kp1:
            break
        a = P.readline()
        b = P1.readline()        
    else:
        P2.write(b)
        j+=1
        if j ==kp1:
            break
        b = P1.readline()
while i<=(kp-1):
    P2.write(a)
    i+=1
    a=P.readline()
while j<=(kp1-1):
    P2.write(b)
    j+=1
    b = P1.readline()
P.close()
P1.close()
P2.close()
printt('P.txt')
printt('P1.txt')
printt('P2.txt')
    
