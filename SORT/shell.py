def shell1(data):
    inc = len(data)//2
    while inc:
        for i,el in enumerate(data):
            while i>=inc and data[i-inc]>el:
                data[i] = data[i-inc]
                i-=inc
            data[i]=el
        inc =1 if inc==2 else int(inc*5/11)
    return data    


def shell(mass):
    len_mass = len(mass)

    t = len_mass // 2
    while t > 0:
        for i in range(len_mass - t):
            j = i
            while j > -1 and mass[j] > mass[j + t]:
                mass[j], mass[j + t] = mass[j + t], mass[j]
                j -= 1
        t //= 2
    return mass


a = [9,8,9,8,7,6,5,4,3,2,1]
print(a)
d = shell(a)
print(d)
a = [8,7,7,5,4,3,6,2,1]
print(a)
d1 = shell1(a)
print(d1)
