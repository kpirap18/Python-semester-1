'''       Oперации над записями, хранящимися в файле
Выполнение действий над файлов, выбранным пользователем
                                     Козлова Ирина ИУ7-12б'''
# Выбор действий над файлами и записями
# choose_menu - выбор пользователя
def menu():
    while True:
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
            'Опрерации c набором записей:\n'
            '1. Выбрать файла.\n'
            '2. Cоздать в файле нового набора записей.\n'
            '3. Добавить записи.\n'
            '4. Вывести всех записей.\n'
            '5. Поиск по одному полю.\n'
            '6. Поиск по двум полям.\n'
            '7. Отсортировать набор записи по одному полю.\n'
            '8. Отсортировать набор записи по двум полям.\n'  
            '0. Выход\n'
            '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
            )
        try:
            choose_menu = int(input('Выбор: '))
            print()
            if choose_menu>8 or choose_menu<0:
                print('Не существует операции под таким номером\n')
            else:
                return(choose_menu)
        except ValueError:
            print('Введены некорректные данные\n'
                        'Проверьте введеные данные\n\n')

# Выбор файла(1)
# filename - переменная, привязаннная к файлу
def choose_file():
    while True:
        try:
            filename = input('Введите имя файла: ')
            print()
            return(filename)
            #fileused = open(file_name)
            #fileused.close()
            print()

            return file_name
        except IOError:
            prin('Файла с таким именем не найдено'
                 'Проверьте введенные данные')

# Создание новых записей(2)
# Функция полностью перезаписывает файл
# f,file - переменые для файла
# coll_record - количество новых записей
# add - новая запись
def create_record(f):
    if f is not None:
        file = open(f,'w')
        print('Добавление новых записей в файл'.format(f))
        coll_record = int(input('Введите количество новых записей: '))
        for i in range(coll_record):
            print('Введите запись {0} для записи в файл'.format(i+1))
            add = input()
            add += '\n'
            file.writelines(add)
        file.close()
        print()
    else:
        print('Файл не найден. Выбирете файл.\n')

# Добавления записи(3)
# Функция добавляет новые записи в конец файла
# f,file - переменые для файла
# coll_record - количество новых записей
# add - новая запись
def add_record(f):
    if f is not None:
        file = open(f,'a+')
        print('Добавление новых записей в файл'.format(f))
        coll_record = int(input('Введите количество новых записей: '))
        for i in range(coll_record):
            print('Введите запись {0} для записи в файл'.format(i+1))
            add = input()
            add += '\n'
            file.writelines(add)
        file.close()
        print()    
    else:
        print('Файл не найден. Выбирете файл.\n')

# Вывод всего файла(4)        
def output_all_records(f):
    try:
        if f is not None:
            file = open(f)
            print('Вывод всех записей файла {}:'.format(f))
            for i in file:
                print(i,end='')
            print()
            file.close()    
        else:
            print('Файл не найден. Выбирете файл.\n')
    except FileNotFoundError:
        print('Файл пустой, заполните файл!\n')
        
# Поиск по одному полю(5)
# Пользователь вводит поле , по которому необхдимо произвести поиск
# На экран вывоятся только те записи, которые удовлетворяют запросу
def one_field_search(f):
    try:
        k = 0
        
        if f is not None:
            file = open(f,'r')
            all_line = []
            for i in file:
                list_line = i.split()
                all_line.append(list_line)
            print('Работа с файлом {}:'.format(f))
            file.close()
            sortF = open('sortF','w')
            num_pol = int(input('Введите номер поля, по \
которому надо произвести поиск: ')) # номер поля
            if num_pol==3:          # если совпадает с полем Год рождение
                print('Введите диапазон поиска ')
                search1 = int(input('начало: '))
                search2 = int(input('Конец: '))
                ent = None
                for i in range(len(all_line)):
                    if search1<=int(all_line[i][2])<=search2:
                        k +=1
                        if k==1:
                            print('Записи, удовблетворяющие условию поиска')
                        ent = ' '.join(all_line[i])
                        print(ent)
                        sortF.writel(ent)
                        sortF.write('\n')
                print()
                sortF.close()
            else:        
                search = input('Введите поле, по которому надо произвести \
поиск: ')
                print()
                ent = None
                for line in all_line:
                    if search in line:
                        k +=1
                        if k==1:
                            print('Записи, в которых содежратся {0}'\
                                  .format(search))
                        ent = ' '.join(line)
                        print(ent)
                        sortF.write(ent)
                        sortF.write('\n')
            print()
            sortF.close()
            if ent is None:
                print('Записей с таким полем не существует\n')
        
        else:
            print('Файл не найден. Выбирете файл.\n')
    except FileNotFoundError:
        print('Файл пустой, заполните файл!\n')

# Поиск по двум полям(6)
def two_field_search(f):
    try:
        k = 0
        if f is not None:
            file = open(f,'r')
            all_line = []
            ent = None
            for i in file:
                list_line = i.split()
                all_line.append(list_line)    
            print('Работа с файлом {}:'.format(f))
            file.close()
            sortF = open('sortF.txt','w')
            num_pol = int(input('Введите номер поля, по которому надо \
произвести поиск: '))
            if num_pol==3:
                print('Введите диапазон поиска')
                search1_1 = int(input('Начало: '))
                search2_1 = int(input('Конец: '))
                search2 = input('Введите второе поле, по которому надо \
произвести поиск: ')
                print()
                ent = None
                for i in range(len(all_line)):
                    if (search1_1<=int(all_line[i][2])<=search2_1) and \
                       (search2 in all_line[i]):
                        k +=1
                        if k==1:
                            print('Записи, удовлетворяющие условиям поиска')
                        ent = ' '.join(all_line[i])
                        print(ent)
                        sortF.write(ent)
                        sortF.write('\n')
                sortF.close()       
            else:    
                search1 = input('Введите первое поле, по которому \
надо произвести поиск: ')
                search2 = input('Введите второе поле, по которому \
надо произвести поиск: ')
                for line in all_line:
                    if search1 in line and search2 in line:
                        k += 1
                        ent = ' '.join(line)
                        if k==1:
                            print('Записи, в которыых содержатся {0} и {1}'\
                                  .format(search1,search2))
                        print(ent)
                        sortF.write(ent)
                        sortF.write('\n')
                print()
                sortF.close()
            if ent is None:
                print('Записей с такими полями не существует\n')
        else:
            print('Файл не найден. Выбирете файл.\n')        
    except FileNotFoundError:
        print('Файл пустой, заполните файл!\n')

# Сортировка набора записей(7)
# По одному полю
def sortFile_1(f):
    try:
        if f is not None:
            file = open(f,'r')
            p = int(input('Укажите номер поля, по которому необходимо произвести сортировку: '))
            all_line = []
            for i in file:
                #print(i)
                list_line = i.split()
                #print(list_line)
                all_line.append(list_line)
            #print(all_line)    
            for i in range(len(all_line)):
                for j in range(len(all_line)-1-i):
                    if all_line[j][p-1] > all_line[i+1][p-1]:
                        all_line[j],all_line[j+1] = all_line[j+1],\
                                                           all_line[j]
            for i in all_line:
                ent = ' '.join(i)
                print(ent)           
        else:
            print('Файл не найден. Выбирете файл.\n')                    
    except FileNotFoundError:
        print('Файл пустой, заполните файл!\n')
        
# Сортировка набора записей(8)
# По двум полям(если встречаются одинаковые, то сортируется по 2 полю)
def sortFile_2(f):
    try:
        if f is not None:
            file = open(f,'r')
            p1,p2 = map(int,input('Укажите номерa полей, по которым\n'
                                  'необходимо произвести сортировку(через \
пробел): ').split())
            all_line = []
            for i in file:
                #print(i)
                list_line = i.split()
                #print(list_line)
                all_line.append(list_line)
            #print(all_line)    
            for i in range(len(all_line)):
                for j in range(len(all_line)-1-i):
                    if all_line[j][p1-1] > all_line[j+1][p1-1]:
                        all_line[j],all_line[j+1] = all_line[j+1],\
                                                           all_line[j]
                    elif all_line[j][p1-1]==all_line[j+1][p1-1]:
                        if all_line[j][p2-1] > all_line[j+1][p2-1]:
                            all_line[j],all_line[j+1] = all_line[j+1],\
                                                           all_line[j]
                        
            for i in all_line:
                ent = ' '.join(i)
                print(ent)           
        else:
            print('Файл не найден. Выбирете файл.\n')                    
    except FileNotFoundError:
        print('Файл пустой, заполните файл!\n')

        
# Пограмма
input_file = None
while True:
    
    result = menu()
    if result == 1:
        input_file = choose_file()
    elif result == 2:
        create_record(input_file)
    elif result == 3:
        add_record(input_file)
    elif result == 4:
        output_all_records(input_file)
    elif result == 5:
        one_field_search(input_file)
    elif result == 6:
        two_field_search(input_file)
    elif result == 7:
        sortFile_1(input_file)
    elif result == 8:
        sortFile_2(input_file)        
    elif result == 0:
        break
