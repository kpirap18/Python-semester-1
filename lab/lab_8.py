# Вычисление интегралов методами численного интегрирования.

# Данная программа вычисляет интеграл заданной функции методами численного
# интегрирования, а именно методом левого прямоугольника и методом 3/8.
# Для наименее точного способа также вычисляется интеграл с заданной точностью.

# Входные данные:
# a, b - верняя и нижняя границы интегрирования.
# n1,n2 - значения для разбиения.
# eps - точность для вычисления интеграла с наименьшей точностью.

# Выходые данные:
# int_pr1, int_pr2 - интегралы вычисленные по методу левого прямоугольника.
# с n1 и n2 разбиениями.
# int_381, int_382 - интегралы вычисленные по методу 3/8 с n1 и n2 разбиениями.
# int_toch - точное значение интеграла.
# abs_er, otn_er - абсолютная и относительная ошибки.

# Промежуточные значения:
# h1, h2, h_eps - шаги для вычислений интеграла.
# n_eps - количество операция для вычисления интеграла с заданной точностью.
# k, k_eps - значение для вычисления функции при определенном значение n.
# s2_382, s3_382, s2_381, s3_382 - сумма значений функций для вычисления
# методом 3/8.
# i - переменая для работы цикла

# Пример:
# Ввод:
# a = 0, b = 1
# n1 = 9, n2 = 180
# eps = 0.0001
# Вывод:
# ┌───────────────────────┬───────────────────────┬───────────────────────┐
# │         Метод         │       n1 =  9         │       n2 = 180        │
# ├───────────────────────┼───────────────────────┼───────────────────────┤
# │  Левый прямоугольник  │       0.4172410       │       0.4554865       │
# ├───────────────────────┼───────────────────────┼───────────────────────┤
# │          3/8          │       0.4393204       │       0.4576008       │
# └───────────────────────┴───────────────────────┴───────────────────────┘
#
# Вычисление интеграла с заданной точность epsilon по методу
# "левых прямоугольников"
# Введите точность eps: 0.0001
#
# Интеграл, вычесленный с точностью 0.0001 равен 0.4596463 
# Данное значение интеграла вычесленно за 8192 шагов
# Точное значение интеграла =  0.4596977
#
# Метод " Левых прямоугольников " c заданной точностью: 
# Абсолютная ошибка = 0.0000514 
# Относительная ошибка = 0.0001117 
#
# Метод "Левыx прямоугольников":
# Абсолютная ошибка = 0.0472214 при 9 разбиениях, 0.0023386 при 180 разбиениях
# Относительная ошибка = 0.1027228 при 9 разбиениях, 0.0050873 при 180 разбиениях
#
# Метод "3/8":
# Абсолютная ошибка = 0.0000009 при 9 разбиениях, 0.0000000 при 180 разбиениях
# Относительная ошибка = 0.0000019 при 9 разбиениях, 0.0000000 при 180 разбиениях

from math import sin,cos
a, b = map(float, input("Введите верхнюю и "
                                  "нижнюю границы интегрирования: ").split())
n1, n2 = map(int, input("Введите два значения для разбиения(кратно 3): ").split())
             
def func(x):
    return x**2

from scipy import integrate
int_toch = integrate.quad(func,a,b)[0]

if n1<1 or n2<1 or a>=b :
    print("Введены некорректные исходные данные!")
elif n1 % 3 != 0 or n2 % 3 != 0:
    print('Метод "3/8" работает только для разбиений, кратных 3! ')
    print("Введены некорректные исходные данные!")
else:
#    int_toch = (-1)*(cos(b)-cos(a))

# Вычисление интеграла для n1 
    h1 = (b-a)/n1 
    h2 = (b-a)/n2
    s3_381 = 0; s2_381 = s3_381
    k = a; int_pr1 = 0
    int_381 = int_pr1
    for i in range(1,n1):
        k += h1
        if i%3==0:
            s3_381 += func(k)
        else:
            s2_381 += func(k)
            
        int_pr1 = int_pr1 + func(k)
    int_pr1 = abs((int_pr1+func(a))*h1)
    int_381 = abs(3*h1/8*(func(a)+func(b)+2*s3_381+3*s2_381))
    
# Вычисление интеграла для n2
    s3_382 = 0; s2_382 = s3_382
    k = a; int_pr2 = 0
    int_382 = int_pr2
    for i in range(1,n2):
        k += h2
        if i%3==0:
            s3_382 += func(k)
        else:
            s2_382 += func(k)
        int_pr2 = int_pr2 + func(k)
    int_pr2 = abs((int_pr2+func(a))*h2)
    int_382 = abs(3*h2/8*(func(a)+func(b)+ 2 * s3_382 + 3 *s2_382))

    print('\n',u'\u250C',u'\u2500'*25,u'\u252C',u'\u2500'*23,u'\u252C',\
          u'\u2500'*23,u'\u2510',sep='')
    print(u'\u2502','        Метод          ',u'\u2502','      n1 =',\
          '{:^4.0f}'.format(n1),'     ',u'\u2502','      n2 =',\
          '{:^4.0f}'.format(n2),'     ',u'\u2502')
    print(u'\u251C',u'\u2500'*25,u'\u253C',u'\u2500'*23,u'\u253C',\
          u'\u2500'*23,u'\u2524',sep='')
    print(u'\u2502',' Левыx прямоугольников ',u'\u2502','{:^21.7f}'\
          .format(int_pr1),u'\u2502','{:^21.7f}'.format(int_pr2),u'\u2502')
    print(u'\u251C',u'\u2500'*25,u'\u253C',u'\u2500'*23,u'\u253C',\
          u'\u2500'*23,u'\u2524',sep='')
    print(u'\u2502','         3/8           ',u'\u2502','{:^21.7f}'\
          .format(int_381),u'\u2502','{:^21.7f}'.format(int_382),u'\u2502')
    print(u'\u2514',u'\u2500'*25,u'\u2534',u'\u2500'*23,u'\u2534',\
          u'\u2500'*23,u'\u2518',sep='')

    abs_erpr = abs(int_toch - int_pr2)
    abs_er38 = abs(int_toch - int_382)
    if abs_erpr>abs_er38:
        s = 'Левыx прямоугольникoв'
        print('\nВычисление интеграла с заданной точность epsilon по методу \n\
"левыx прямоугольников"')
        eps = float(input('Введите точность eps: '))
        n_eps = 1
        h_eps = (b-a)/n_eps
        int_eps1 = abs(h_eps*(func(b)+func(a)))
        while True:
            int_eps2 = 0
            n_eps *= 2
            h_eps = (b-a)/n_eps
            k_eps = a
            for i in range(1,n_eps):
                k_eps += h_eps
                int_eps2 += func(k_eps)
            int_eps2 = abs((int_eps2+func(a)) * h_eps)
            if abs(int_eps2-int_eps1) < eps:
                break
            else:
                int_eps1 = int_eps2
    else:
        s = '3/8'
        print('\nВычисление интеграла с заданной точность epsilon по методу \
"3/8"')
        eps = float(input('Введите точность eps: '))
        n_eps = 1
        h_eps = (b-a)/n_eps
        int_eps1 = abs(3/8*h_eps*(func(b)+func(a)))
        while True:
            s3_38 = s2_38 = 0
            int_eps2 = 0
            n_eps *= 2
            h_eps = (b-a)/n_eps
            k_eps = a
            for i in range(1,n_eps):
                k_eps += h_eps
                if i%3==0:
                    s3_38 += func(k_eps)
                else:
                    s2_38 += func(k_eps)    
            int_eps2 = abs(3/8*h_eps*(func(a)+func(b)+2*s3_38+3*s2_38))
            if abs(int_eps2-int_eps1)<eps:
                break
            else:
                int_eps1 = int_eps2
    print('\nИнтеграл, вычесленный с точностью {0} равен {1:^10.7f}\nДанное \
значение интеграла вычесленно за {2} шагов'.format(eps,int_eps2,n_eps))
    print('Точное значение интеграла =','{:10.7f}'.format(int_toch))

    abse = abs(int_toch - int_eps2)
    otn = abs((int_toch - int_eps2)/int_toch)
    print('\nМетод "',s,'" c заданной точностью: \n\
Абсолютная ошибка = {0:.7f} \n\
Относительная ошибка = {1:.7f} \n'.format(abse, otn))

    
        
    abs_er2 = abs(int_toch - int_pr1)
    otn_er1 = abs((int_toch - int_pr1)/int_toch)
    otn_er2 = abs((int_toch - int_pr2)/int_toch)
    print('Метод "Левых прямоугольников":\n'
          'Абсолютная ошибка = {0:^9.7f} при {1} разбиениях, '
          '{2:^9.7f} при {3} разбиениях\n'
          'Относительная ошибка = {4:^9.7f} при {1} разбиениях, '
          '{5:^9.7f} при {3} разбиениях\n'
          .format(abs_er2,n1,abs_erpr,n2,otn_er1,otn_er2))
    
    abs_er38 = abs(int_toch - int_381)
    abs_er2 = abs(int_toch - int_382)
    otn_er1 = abs((int_toch - int_381)/int_toch)
    otn_er2 = abs((int_toch - int_382)/int_toch)
    print('Метод "3/8":\n'
          'Абсолютная ошибка = {0:^9.7f} при {1} разбиениях, '
          '{2:^9.7f} при {3} разбиениях\n'
          'Относительная ошибка = {4:^9.7f} при {1} разбиениях, '
          '{5:^9.7f} при {3} разбиениях\n'
          .format(abs_er38,n1,abs_er2,n2,otn_er1,otn_er2))