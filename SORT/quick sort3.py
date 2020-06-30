def quicksort(mass, l, r):
    print(mass)
    if l >= r:
        return
    i, j = l, r
    x = mass[(l + r) // 2]
    while i <= j:
        while mass[i] < x:
            i += 1
        while mass[j] > x:
            j -= 1
        if i <= j:
            mass[i], mass[j] = mass[j], mass[i]
            i += 1
            j -= 1

    quicksort(mass, l, j)
    quicksort(mass, i, r)
    return mass

a = [9,8,7,6,5,3,3,4,5,6,4,2,0,1]
print(a)
quicksort(a,0,len(a)-1)
print(a)
