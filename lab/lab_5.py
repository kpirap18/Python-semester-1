# Наибольшое число в массиве, которое не является суммой разных
# элементов этого массива

def summ(v_res, B, ind,cS):
    if ind<len(B):
        #print(v_res,' ', B, ' ', ind,' ', cS)
        cS += B[ind]
        
        
        for i in range(ind+1,len(B)):
            res = summ(v_res,B,i,cS)
            #print('res',res)
            v_res.append(res)
            #print('v_res',v_res)
    #print('\n exit')        
    return(cS)

# Основная программа
print('Задача: Наибольшое число в массиве, которое не является суммой разных\n'
      'других элементов этого массива')
print()
#n = int(input('Введите размер массива В: '))
B = []
print('Введите числа массива B: ',end = '')
B = list(map(int,input('').split()))
#print(B)
n = len(B)
#print(n)
v_res = []
for i in range(0,len(B)):
    res = summ(v_res,B,i,0)
    v_res.append(res)
#print(v_res)

for i in range(n):
    v_res.remove(B[i])
#print(v_res)    

maxB = -100000000
F = False
for i in range(n):
    if B[i]>=maxB:
        k = B[i] in v_res
        if k==False:
            maxB = B[i]
            F = True
if F:
    print('Наибольшее число удовлетворяющее условию: ',maxB)            
else:
    print('Такого числв нет')
