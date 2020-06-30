# Лабораторная работа №10         Козлова Ирина ИУ7-12Б
# Выполнение операций над текстом, находящимся в массиве
# Данная программа выполняет обработку текста, по заданным условиям,
# выбираемым пользователем. Операции поьзователь выбирает из меню, которые 
# вызывается каждый раз после выполнения операций.
# Текст содержится в массиве input_text

# Содержание меню
def menu():
    while True:
        print(
            'Опрерации c текстом:\n'
            '1. Выравнивание по ширине.\n'
            '2. Выравнивание по левому краю.\n'
            '3. Выравнивание по правому краю.\n'
            '4. Замена во всем тексте одного слова другим.\n'
            '5. Удаление заданного слова из текста.\n'
            '6. Замена арифметических операций на их числовое значение.\n'
            '7. Найти самое короткое слово в самом длинном по количеству \
слов предложении.\n'
            '8. Самое которкое предложение напечатать в столбик по словам.\n\n'
            '0. Выход\n'
            )
        try:
            choose_menu = int(input('Выбор: '))
            print()
            if choose_menu>8 or choose_menu<0:
                print('Не существует операции под таким номером')
            else:
                return(choose_menu)
        except ValueError:
            print('Введены некорректные данные\n'
                        'Проверьте введеные данные\n\n')

mark = ['.',',',':',';','!','?']
input_text = ['Воланд сидел на складном табурете, одетый в черную свою',
              '      сутану. Его длинная широкая шпага была воткнута между \
двумя ',
              'рассекшимися плитами террасы   вертикально, так что',
              '   получились   солнечные часы. Тень шпаги медленно и \
неуклонно ',
              'удлинялась, подползая к черным туфлям   на ногах сатаны. \
Положив ',
              'острый 9+8 подбородок на кулак, скорчившись на табурете и',
              'поджав      одну ногу под себя,  Воланд        не отрываясь \
смотрел ',
              'на   5+2   необъятное сборище дворцов, гигантских домов и \
маленьких,',
              '    обреченных на слом         лачуг. Азазелло, расставшись',
              'со своим современным нарядом, то есть пиджаком, котелком \
лакированными ',
              'туфлями, одетый, как и Воланд, в черное,        неподвижно \
стоял ',
              'не вдалеке от своего        повелителя, так же как      и     \
он ',
              '          не спуская       глаз с города.']

print('Исходный текст:')
for i in input_text:
    print(i)
print()    

# Предворительная обработка исходного текста
# Функция удаляет лишние пробелы между словами
def first_treatment(text):
    new_text = [0]*len(text)
    for i in range(len(text)):
        j = text[i].split()
        new_text[i] = ' '.join(j)
    #for i in new_text:
    #    print(i)
    return(new_text)

# Выравниевание по ширине(1)
# Текст выравнивается по ширине путем добавления пробелов между словами
def on_weight(text):
    print('Преобразованный текст')
    # Поиск максимальной длины строки
    max_len = 0
    for i in text:
        if len(i)>=max_len:
            max_len = len(i)
    # Создание массива - количество пробелов между словами
    # Количество пробелов в строке
    for i in range(len(text)):
        if max_len > len(text[i]):
            strt =''
            c_probel = 0
            for j in range(len(text[i])):
                if text[i][j]==' ':
                    c_probel += 1
            # Добавление пробелом между словами, в зависимости от длины строки           
            probel = [0]*c_probel
            delta = max_len - len(text[i])
            k1 = delta//c_probel
            for j in range(c_probel):
                probel[j] = k1+1   
            k1 = delta%c_probel
            k = 0
            while k1>0:
                probel[k] += 1
                k1 -= 1
                k += 1
            # Форматированный вывод текста    
            k = 0    
            for j in range(len(text[i])):
                if text[i][j]!=' ':
                    strt += text[i][j]
                else:
                    strt += ' '*probel[k]
                    k += 1
            print(strt)
        else:
            print(text[i])
    print()

# Выпавнивание по левому краю(2)
# Текст выравнивается по левому краю путем удаления пробелов в начале строки
def on_left(text):
    print('Преобразованный текст')
    for i in range(len(text)):
        strt = ''
        sim_fou = False
        for j in range(len(text[i])):
            if text[i][j]!=' ':
                sim_fou = True
            if sim_fou:
                strt += text[i][j]
        print(strt)
    print()        

# Выравнивание по правому краю(3)
# Текст выравнивается по правому краю путем добавления проблев в начало строки
def on_right(text):
    max_len = 0
    print('Преобразованный текст')
    # Поиск максимальной длины строки
    for i in text:
        if len(i)>=max_len:
            max_len = len(i)
    # Добавление пробелов перед строкой        
    for i in range(len(text)):
        k = ' '*(max_len - len(text[i]))
        print(k,text[i])
    print()

# Замена слова в тексте(4)
# Замена выбранного слова другим, введенным с клавиатуры
def replace_word(text):
    word = input('Введите слово, которое нужно заменить: ')
    word_replaced = input('Введите слово, на которое нужно \
заменить исходное слово: ')
    print()
    print('Преобразованный текст')
    word_replaced2 = ''
    str_text = []
    for i in range(len(text)):
        s = text[i].split()
        str_text.append(s)
    #for i in str_text:
    #   print(i)
    
    # Поиск удаляемого слова с учетом регистра
    # и замена его, с учетом регистра и возможных дополнительных символов
    # после данного слова(',' или '.')
    for i in range(len(str_text)):
        for j in range(len(str_text[i])):
            del_sim = ''
            c = str_text[i][j]
            if c[len(c)-1] in mark:
                del_sim = c[len(c)-1]
                c = c[:len(c)-1]
            if c.lower() == word.lower():
                word_replaced2 = ''
                len_c = len(c)
                print(len_c)
                if c[0].isupper():
                    word_replaced2 += chr(ord(word_replaced[0].lower())-32)
                    word_replaced2 += word_replaced[1:]
                else:
                    word_replaced2 += chr(ord(word_replaced[0].lower()))
                    word_replaced2 += word_replaced[1:]
                str_text[i][j] = word_replaced2

    # Форматированный вывод
    for i in range(len(text)):
        k = 0
        str_word = ''
        j = 0
        while j<len(text[i])-1:
            if text[i][j] == ' ':
                str_word += ' '
                j += 1
            if text[i][j] != ' ':
                if text[i][j] in mark:
                    str_word += text[i][j]
                    j += 1
                elif str_text[i][k] == word_replaced2:
                    str_word += str_text[i][k]
                    j += len_c
                    k += 1
                else:    
                    str_word += str_text[i][k]
                    j += len(str_text[i][k])
                    k += 1
        print(str_word)
    print()    

# Удаление слова(5)
# Поиск введенного слова в тексте с учетом регистра и возможно стоящих за ним
# символов ',' или '.' и удаление такого слова
def delet_word(text):
    del_word = input('Введите удаляемое слово: ')
    print()
    print('Преобразованный текст')
    str_text = []
    for i in range(len(text)):
        s = text[i].split()
        str_text.append(s)
    #for i in str_text:
    #    print(i)    
    for i in range(len(str_text)):
        for j in range(len(str_text[i])):
            c = str_text[i][j]
            if c[len(c)-1] in mark:
                c = c[:len(c)-1]
            if c.lower() == del_word.lower():
                str_text[i][j] = ''
                len_del_word = len(del_word)
    #for i in str_text:
    #    print(i)                        
    for i in range(len(text)):
        k = 0
        str_word = ''
        j = 0
        while j<=len(text[i])-1:
            if text[i][j] == ' ':
                str_word += ' '
                j += 1
            elif text[i][j] != ' ':
                if text[i][j] in mark:
                    str_word += text[i][j]
                    j += 1
                elif str_text[i][k] == '':
                    str_word += str_text[i][k]
                    j += len_del_word
                    k += 1
                else:    
                    str_word += str_text[i][k]
                    j += len(str_text[i][k])
                    k += 1
        print(str_word)
    print()  
                        
# Замена алгебраических операций на их результат(6)
# Поиск симболов + или -, и подсчет соответствующих значений
# с учетом перевода типа строки в число
def evalar(text):
    str_text = []
    str_2 = []
    print('Преобразованный текст')
    for i in range(len(text)):
        s = text[i].split()
        str_text.append(s)
    str_2 = [text[i].split() for i in range(len(text))]
    for i in range(len(str_text)):
        for j in range(len(str_text[i])):
            if '-' in str_text[i][j]:
                p = str_text[i][j].find('-')
                k1 = str_text[i][j][:p]
                k2 = str_text[i][j][p:]
                k1 = str(k1)
                k2 = str(k2)
                k12 = int(k1)-int(k2)
                print(k12)
                str_text[i][j] = str(k12)
            elif '+' in str_text[i][j]:
                p = str_text[i][j].find('+')
                k1 = str_text[i][j][:p]
                k2 = str_text[i][j][p:]
                k1 = str(k1)
                k2 = str(k2)
                k12 = int(k1)+int(k2)
                str_text[i][j] = str(k12)
    # Форматированный вывод        
    for i in range(len(text)):
        k = 0
        j = 0
        str_word = ''
        while j<=len(text[i])-1:
            if text[i][j] == ' ':
                str_word += ' '
                j += 1
            else:
                str_word += str_text[i][k]
                j += len(str_2[i][k])##################
                k += 1
        print(str_word)
    print()

# Самое короткое слово в самомо длинном предложении(7)
def min_word_input(text):
    # Разбиение на предложения
    str_text = []
    s = ''
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j]!='.':
                s += text[i][j]
                #print(text[i][j])
            else:
                s += text[i][j]
                #print(text[i][j])
                str_text.append(s)
                s = ''
                
    #for i in str_text:
    #    print(i)

    print()
    # Предложения в виде массива слов
    for i in range(len(str_text)):
        s = str_text[i].split()
        str_text[i] = s

    # Поиск максимального предложения по длине слов
    max_sen = ''    
    for i in range(len(str_text)):
        if len(str_text[i])>len(max_sen):
            max_sen = str_text[i]
            max_num_sen = i
    #print(max_sen)
    #print(max_num_sen)

    # Поиск минимально слова в максимальном по колическу слов предложении
    len_min_word = len(str_text[max_num_sen][0])
    for i in range(len(str_text[max_num_sen])):
        if len(str_text[max_num_sen][i])<len_min_word:
            len_min_word = len(str_text[max_num_sen][i])
            min_word = str_text[max_num_sen][i]
            
    # Подсчет минимальных слов в максимальном предлождении
    #k = 0
    #for i in range(len(str_text[max_num_sen])):
    #    print(str_text[max_num_sen][i])
    #    if str_text[max_num_sen][i]==min_word:
    #        k += 1
    #for i in range(len(text)):
    #    s = text[i].split()
    #    if min_word in s:
    #        exit_i = i
    #print('Самое короткое слово в самом длинном предложении: ',min_word,'\n')
    #if k == 0:
    #    print('Данное слово находится в {0} строке исходного текста'.format(exit_i+1))
    #else:
    #    print('Данное слово встречается в {0} предложении {1} разa\n'
    #          'и последнее его вхождение находится в {2} строке \
    #исходного текста'.format(max_num_sen+1,k,exit_i+1))
    
    print('Самое короткое слово в самом длинном предложении: ',min_word,'\n')
    print('Предложение(самое длинное), в котором находится самое \
короткое слово:')

    k = 0
    for i in range(len(max_sen)):
        if k<60:
            k += len(max_sen[i])+1
            print(max_sen[i],' ',end='')#
        else:
            k = len(max_sen[i])+1
            print()
            print(max_sen[i],' ',end='')
    print()
    print()
# Печать предложения в стоблик по словам(по буквам)(8)
def min_sen_row(text):
    print('Самое короткое предложение текста')
    # Разбиение на предложения
    str_text = []
    s = ''
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j]!='.':
                s += text[i][j]
                #print(text[i][j])
            else:
                s += text[i][j]
                #print(text[i][j])
                str_text.append(s)
                s = ''
                
    #for i in str_text:
    #    print(i)

    # Предложения в виде массива слов
    for i in range(len(str_text)):
        s = str_text[i].split()
        str_text[i] = s

    # Поиск максимального предложения по длине слов
    len_min_sen = len(str_text[0])
    min_sen = ''
    for i in range(len(str_text)):
        if len(str_text[i])<=len_min_sen:
            len_min_sen = len(str_text[i])
            min_sen = str_text[i]
            min_num_sen = i
            
    # Если есть ',' или '.', то удаляем этот символ
    for i in range(len(min_sen)):
        if min_sen[i][len(min_sen[i])-1] in mark:
            min_sen[i] = min_sen[i][:len(min_sen[i])-1]
    len_max_word = 0        
    for i in range(len(min_sen)):
        if len(min_sen[i])>len_max_word:
            len_max_word = len(min_sen[i])

    # Форматирование преложение в квадратную матрицу    
    for i in range(len(min_sen)):
        s = ''; k = 0
        for j in range(len(min_sen[i])):
            if min_sen[i][j] != ' ':
                s += min_sen[i][j]
                k += 1
        while k<len_max_word:
            s += ' '
            k += 1
        min_sen[i] = s
        
    # Вывод в столбик    
    k = 0
    for i in range(len_max_word):
        for i in range(len(min_sen)):
            print(min_sen[i][k],'   ',end='')
        k += 1
        print()
    print()

    
while True:
    result = menu()

    if result == 1:
        on_weight(first_treatment(input_text))
    elif result == 2:
        on_left(first_treatment(input_text))
    elif result == 3:
        on_right(first_treatment(input_text))
    elif result == 4:
        replace_word(input_text)
    elif result == 5:
        delet_word(input_text)
    elif result == 6:
        evalar(input_text)
    elif result == 7:
        min_word_input(input_text)
    elif result == 8:
        min_sen_row(input_text)
    elif result == 9:
        max_word_replacer(input_text)
    elif result == 0:
        break
