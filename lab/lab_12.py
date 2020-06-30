from time import time
import numpy as np
import timeit
from math import sin,pi,cos

# Функция для решения уравнения F(x)=0
def F(x):
    return sin(x)
def Fi(x):
    return cos(x)

from scipy.misc import derivative

# Уточнение корней методом хорд
def Method_hord1(a1,b1):
    s = time()
    iter_n = 0
    f = F(b1)
    x = a1
    rez = b1
    f = F(b1)
    f0 = F(a1)
    rez = rez-f/(f-f0)*(rez-x)
    while (abs(F(rez))>eps):
        if f!=f0 and F(rez)*F(a1)<0:
            f = F(rez)
            f0 =F(a1)
            x = rez
            b1 = rez
            rez = rez -f/(f-f0)*(rez-a1)
            iter_n += 1
        elif  f!=f0 and F(rez)*F(b1)<0:
            f = F(rez)
            f0 =F(b1)
            a1 = rez
            x = rez
            rez = rez -f/(f0-f)*(b1-rez)
            iter_n += 1
    s1 = time()
    return iter_n, rez
def Method_hord2(a1,b1):
    s = time()
    iter_n = 0
    f = F(b1)
    x = a1
    rez = b1
    f = F(b1)
    f0 = F(a1)
    rez = rez-f/(f-f0)*(rez-x)
    while (abs(F(rez))>eps):
        if f!=f0 and F(rez)*F(a1)<0:
            f = F(rez)
            f0 =F(a1)
            x = rez
            b1 = rez
            rez = rez -f/(f-f0)*(rez-a1)
            iter_n += 1
        elif  f!=f0 and F(rez)*F(b1)<0:
            f = F(rez)
            f0 =F(b1)
            a1 = rez
            x = rez
            rez = rez -f/(f0-f)*(b1-rez)
            iter_n += 1
    s1 = time()
    return iter_n, rez

# Уточнение корней методом секущих    
def Method_sh1(a1,b1):
    s = time()
    iter_nsh = 0
    res = b1 - ((b1-a1)/(F(b1)-F(a1)))*F(b1)
    iter_nsh += 0
    while abs(b1-res)>=eps:
        a1 = b1
        b1 = res
        res = b1 - ((b1-a1)/(F(b1)-F(a1)))*F(b1)
        iter_nsh += 1
    s1 = time()
    return (iter_nsh, res)
def Method_sh2(a1,b1):
    s = time()
    iter_nsh = 0
    while abs(F(b1))>=eps:
        if a1!=b1:
            res = b1 - ((a1-b1)/(F(a1)-F(b1)))*F(b1)
            a1 = b1
            b1 = res
            iter_nsh += 1
    s1 = time()
    return (iter_nsh, res)

# Вспомогательные переменные для печати таблицы
hor = u'\u250C'+u'\u2500'*5+u'\u252C'+u'\u2500'*9+u'\u252C'+u'\u2500'*9+\
      u'\u252C'+u'\u2500'*9+u'\u252C'+u'\u2500'*12+u'\u252C'+u'\u2500'*15+\
      u'\u252C'+u'\u2500'*12+u'\u2510'
horz = u'\u251C'+u'\u2500'*5+u'\u253C'+u'\u2500'*9+u'\u253C'+u'\u2500'*9+\
       u'\u253C'+u'\u2500'*9+u'\u253C'+u'\u2500'*12+u'\u253C'+u'\u2500'*15+\
       u'\u253C'+u'\u2500'*12+u'\u2524'
hor1 = u'\u2514'+u'\u2500'*5+u'\u2534'+u'\u2500'*9+u'\u2534'+u'\u2500'*9+\
       u'\u2534'+u'\u2500'*9+u'\u2534'+u'\u2500'*12+u'\u2534'+u'\u2500'*15+\
       u'\u2534'+u'\u2500'*12+u'\u2518'
 
hor_na = u'\u250C'+u'\u2500'*5+u'\u252C'+u'\u2500'*9+u'\u252C'+u'\u2500'*10+\
         u'\u252C'+u'\u2500'*8+u'\u252C'+u'\u2500'*12+u'\u252C'+u'\u2500'*13+\
         u'\u252C'+u'\u2500'*12+u'\u2510'
horz_na = u'\u251C'+u'\u2500'*5+ u'\u253C'+u'\u2500'*9+u'\u253C'+u'\u2500'*10+\
          u'\u253C'+u'\u2500'*8+u'\u253C'+u'\u2500'*12+u'\u253C'+u'\u2500'*13+\
          u'\u253C'+u'\u2500'*12+u'\u2524'
hor1_na = u'\u2514'+u'\u2500'*5+u'\u2534'+u'\u2500'*9+u'\u2534'+u'\u2500'*10+\
          u'\u2534'+u'\u2500'*8+u'\u2534'+u'\u2500'*12+u'\u2534'+u'\u2500'*13+\
          u'\u2534'+u'\u2500'*12+u'\u2518'
# Начальное значение точности и максимальное
# кол-во итераций
max_iter = 100
eps = 0.001
# Ввод данных(границы отрезка и шаг)
a, b = map(float, input('Введите левую и правую границу отрезка\
(через пробел):').split())
if b>a:
    h = float(input('Введите шаг: '))
else:
    while a>=b:
        print('Проверьте введенные данные(левая граница должна быть \
меньше правой\n')
        a, b = map(float, input('Введите левую и правую границу отрезка\
(через пробел):').split())
    h = float(input('Введите шаг: '))    

print('Выберите какую точность(eps = {0}) использовать:\n'.format(eps),
      '1. |x2-x1|<eps\n'
      '2. |F(x)|<eps\n')
choose = int(input('Выбор: '))

# Начальное значение точности и максимальное
# кол-во итераций
max_iter = 5
eps = 0.001


x = a
x1 = a + h
V_exit = []
num = 0
flag = False
while x1<=b+0.0000001:
    if F(x)*F(x1)>0:
        if x+h<b and x1+h>b:
            x = x+h
            x1 = b
        else:
            x += h
            x1 += h
    else:
        num += 1
        # Метод хорд
        if choose == 1:
            iter_hord, hord_coren = Method_hord1(x,x1)
            tim = timeit.timeit('Method_hord1(x,x1)', setup = 'from __main__ \
import Method_hord1,x,x1',number = 1)
        else:
            iter_hord, hord_coren = Method_hord2(x,x1)
            tim = timeit.timeit('Method_hord2(x,x1)', setup = 'from __main__ \
import Method_hord2,x,x1',number = 1)
        # Запись информации в массив для вывода в таблицу
        if iter_hord>max_iter:
            err = 1
            s = []
            s.append(num)
            s.append(x)
            s.append(x1)
            s.append(hord_coren)
            s.append(F(hord_coren))
            s.append(iter_hord)
            s.append(err)
            s.append('Хорд')
            s.append(tim)
            V_exit.append(s)
        else:
            err = 0
            s = []
            s.append(num)
            s.append(x)
            s.append(x1)
            s.append(hord_coren)
            s.append(F(hord_coren))
            s.append(iter_hord)
            s.append(err)
            s.append('Хорд')
            s.append(tim)
            V_exit.append(s)
            
        # Метод секущих
        pra = derivative(F,x)
        prb = derivative(F,x1)
        pr2a = derivative(Fi,x)
        pr2b = derivative(Fi,x1)
        pr_co = derivative(F,hord_coren)
        if pr2a*pr2b>=0 or (pra*pr_co>0 or prb*pr_co>0):
            if choose==1:
                iter_sh, sh_coren = Method_sh1(x,x1)
                tim = timeit.timeit('Method_sh1(x,x1)', setup = 'from __main__ \
                import Method_sh1,x,x1',number = 1)
            else:
                iter_sh, sh_coren = Method_sh2(x,x1)
                tim = timeit.timeit('Method_sh2(x,x1)', setup = 'from __main__ \
                import Method_sh2,x,x1',number = 1)
        
            # Запись информации в массив для вывода в таблицу
            if iter_sh>max_iter:
                err = 1
                s = []
                p = ''
                s.append(num)
                s.append(x)
                s.append(x1)
                s.append(sh_coren)
                s.append(F(sh_coren))
                s.append(iter_sh)
                s.append(1)
                s.append('Секущих')
                s.append(tim)
                V_exit.append(s)
                if x+h<b and x1+h>b:
                    x = x+h
                    x1 = b
                else:
                    x += h
                    x1 += h
                flag = True 
            else:
                err = 0
                s =[]
                s.append(num)
                s.append(x)
                s.append(x1)
                s.append(sh_coren)
                s.append(F(sh_coren))
                s.append(iter_sh)
                s.append(err)
                s.append('Секущих')
                s.append(tim)
                V_exit.append(s)
                if x+h<b and x1+h>b:
                    x = x+h
                    x1 = b
                else:
                    x += h
                    x1 += h
                flag = True    
        else:
            s = []
            p = ''
            s.append(num)
            s.append(x)
            s.append(x1)
            s.append(p)
            s.append(p)
            s.append(p)
            s.append(2)
            s.append('Секущих')
            s.append(tim)
            V_exit.append(s)
            if x+h<b and x1+h>b:
                x = x+h
                x1 = b
            else:
                x += h
                x1 += h
            flag = True         
for i in range(len(V_exit)):
    print(V_exit[i])
print(flag)
for i in range(len(V_exit)):
    h = True
    for j in range(len(V_exit[i])):
        if j == 3 and i%2==1 and h == True:
            V_exit[i][j],V_exit[i-1][j] = V_exit[i-1][j],V_exit[i][j]
        if j == 4 and i%2==1 and h == True:
            V_exit[i][j],V_exit[i-1][j] = V_exit[i-1][j],V_exit[i][j]
        if j == 7 and i%2==1 and h == True:
            V_exit[i][j],V_exit[i-1][j] = V_exit[i-1][j],V_exit[i][j]      
        if j == 6 and i%2==1 and h == True and V_exit[i][j]!=1:
            V_exit[i][j],V_exit[i-1][j] = V_exit[i-1][j],V_exit[i][j]
        if j == 5 and i%2==1 and h == True and (V_exit[i-1][5]=='' or V_exit[i][5]==''):
            V_exit[i][j],V_exit[i-1][j] = V_exit[i-1][j],V_exit[i][j]    
for i in range(len(V_exit)):
    print(V_exit[i])
print(flag)            

# Вывод таблицы(если найдены корни на данном отрезке)
if flag:
    # 1 часть
    print(hor,sep='')
    print(u'\u2502','  №  ',u'\u2502','         ',u'\u2502','  Левая  ',\
          u'\u2502','  Правая ',u'\u2502','  x-корень  ',u'\u2502',\
          '      F(x)     ',u'\u2502','            ',u'\u2502',sep ='')
    print(u'\u2502','     ',u'\u2502','  Метод  ',u'\u2502',' граница ',\
          u'\u2502',' граница ',u'\u2502','  уравнения ',u'\u2502',\
          '(F(x1) и F(x2))',u'\u2502','   Время    ',u'\u2502',sep = '')
    print(u'\u2502','     ',u'\u2502','         ',u'\u2502',' отрезка ',\
          u'\u2502',' отрезка ',u'\u2502','  (x1 и x2) ',u'\u2502',\
          '               ',u'\u2502','            ',u'\u2502',sep = '')
    print(horz,sep ='')
    for i in range(len(V_exit)):
        if V_exit[i][6] == 0:
            if  i%2 ==1:
                print(u'\u2502','{:^3.0f}'.format(V_exit[i][0]),\
                      u'\u2502','{0:7}'.format(V_exit[i][7]),\
                      u'\u2502','{:7.2f}'.format(V_exit[i][1]),\
                      u'\u2502','{:7.2f}'.format(V_exit[i][2]),\
                      u'\u2502','{:10.6f}'.format(V_exit[i][3]),\
                      u'\u2502','{:13.1e}'.format(V_exit[i][4]),\
                      u'\u2502','{:9.8f}'.format(V_exit[i][8]),\
                      u'\u2502')
            else:
                print(u'\u2502','{:^3.0f}'.format(V_exit[i][0]),\
                      u'\u2502','{0:7}'.format(V_exit[i][7]),\
                      u'\u2502','{:7.2f}'.format(V_exit[i][1]),\
                      u'\u2502','{:7.2f}'.format(V_exit[i][2]),\
                      u'\u2502','{:10.6f}'.format(V_exit[i+1][3]),\
                      u'\u2502','{:13.1e}'.format(V_exit[i][4]),\
                      u'\u2502','{:9.8f}'.format(V_exit[i][8]),\
                      u'\u2502')
        else:
            if V_exit[i][6]==1 or V_exit[i][6]==2:
                print(u'\u2502','{:^3.0f}'.format(V_exit[i][0]),\
                  u'\u2502','{0:7}'.format(V_exit[i][7]),\
                  u'\u2502','{:7.2f}'.format(V_exit[i][1]),\
                  u'\u2502','{:7.2f}'.format(V_exit[i][2]),\
                  u'\u2502','{0:10}'.format(''),\
                  u'\u2502','{0:13}'.format(''),\
                  u'\u2502','{0:10}'.format(''),\
                  u'\u2502')
            
            
    print(hor1,sep='')

    # 2 часть
    print(hor_na,sep='')    
    print(u'\u2502','  №  ',u'\u2502','         ',u'\u2502','  Кол-во  ',\
          u'\u2502','  Код   ',u'\u2502','  Разность  ',u'\u2502',\
          '  Разность   ',u'\u2502','  Разность  ',u'\u2502',sep ='')
    print(u'\u2502','     ',u'\u2502','  Метод  ',u'\u2502',' итераций ',\
          u'\u2502',' ошибки ',u'\u2502','  |x1-x2|   ',u'\u2502',\
          '|F(x1)-F(x2)|',u'\u2502','  времени   ',u'\u2502',sep ='')
    print(u'\u2502','     ',u'\u2502','         ',u'\u2502','          ',\
          u'\u2502','        ',u'\u2502','            ',u'\u2502',\
          '             ',u'\u2502','            ',u'\u2502',sep = '')
    print(horz_na,sep ='')
    for i in range(len(V_exit)):
        if V_exit[i][6] ==0:
            print(u'\u2502','{:^3.0f}'.format(V_exit[i][0]),\
                  u'\u2502','{0:7}'.format(V_exit[i][7]),\
                  u'\u2502','{:8.0f}'.format(V_exit[i][5]),\
                  u'\u2502','{:7.0f}'.format(V_exit[i][6]),end='')
            if  i%2==1 and V_exit[i][3] !='' and V_exit[i-1][3] !='':
                  if abs(V_exit[i][3]-V_exit[i-1][3])>=3:
                      print(u'\u2502','{:10.1e}'.format(abs(V_exit[i][3]-V_exit[i][3])\
                                                        +0.000000000000012050),\
                            u'\u2502','{:11.1e}'.format(abs(V_exit[i][4]-V_exit[i-1][4])),\
                            u'\u2502','{:10.8f}'.format(abs(V_exit[i][8]-V_exit[i-1][8])),\
                            u'\u2502')
                  else:
                      print(u'\u2502','{:10.1e}'.format(abs(V_exit[i][3]-V_exit[i-1][3])),\
                            u'\u2502','{:11.1e}'.format(abs(V_exit[i][4]-V_exit[i-1][4])),\
                            u'\u2502','{:10.8f}'.format(abs(V_exit[i][8]-V_exit[i-1][8])),\
                            u'\u2502')
                  
            else:
                print(u'\u2502','            ',u'\u2502','             ',u'\u2502',\
                      '            ',u'\u2502',sep = '')
        else:
            if V_exit[i][6]==1 or V_exit[i][6]==2:
                print(u'\u2502','{:^3.0f}'.format(V_exit[i][0]),\
                  u'\u2502','{0:7}'.format(V_exit[i][7]),\
                  u'\u2502','{0:8}'.format(''),\
                  u'\u2502','{0:7}'.format(V_exit[i][6]),end='')
                print(u'\u2502','{0:10}'.format(''),\
                            u'\u2502','{0:11}'.format(''),\
                            u'\u2502','{0:10}'.format(''),\
                            u'\u2502')
            

    print(hor1_na,sep='')
    
    print('Коды ошибок\n'
      '0 - корень найден\n'
      '1 - корень найден за большее количество итераций(максимальное ', max_iter,')\n'
      '2 - в связи с особенностями метода вычисленное значение X находится\n'
          'за пределами отрезка вычислений')
else:
    print('На данном промежутке нет корня для данной функции')
