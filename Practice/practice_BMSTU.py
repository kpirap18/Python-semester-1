'''                           Кроссворд
# Данная программа составляет двойной линейный кроссворд заданной
# длины из введенных слов.
# Соблюдаю правила:
# - Слова из первого разложения могут не появиться во втором и наоборот.
# - Кроме того, ни одно слово не может быть повторено в любом разложении. 
# - Ни одно слово в одной декомпозиции не может заканчиваться в том же
# - месте строки,где заканчивается слово в другой композиции, за исключением,
# - естественно, конца строки (в противном случае кроссворд может быть
# - разделен на два независимых кроссворда).
# Ввод(входной файл):
# 17
# 19
# all
# an
# and
# area
# as
# ask
# at
# data
# do
# for
# last
# of
# or
# ort
# read
# real
# task
# to
# tor
# Вывод:
# andatareadofortor
'''

# Функция FindFonemsInWord находит фонемы в слове, которые есть
# в других словах заданного массива
# analyzable_word
# analyzable_words 
# fonems_words
# fonema
# index_analyzable_word
# index_fonema
# lenght_word
# names_fonems
def FindFonemsInWord(analyzable_word, words):
    fonems_words = []
    length_word = len(analyzable_word)
    index_analyzable_word = words.index(analyzable_word)
    analyzable_words = words[index_analyzable_word+1:]
    names_fonems = []
    for i in range(length_word):
        for j in range(i+1,length_word+1):
            fonema = analyzable_word[i:j]
            print(fonema)
            if fonema in names_fonems:
                continue
            fonems_words.append([fonema[:], [analyzable_word[:]]])
            names_fonems.append(fonema[:])
            index_fonema = len(fonems_words) - 1
            for word in analyzable_words:
                if fonema in word:
                    fonems_words[index_fonema][1].append(word)
            if fonems_words[index_fonema][1] == [analyzable_word[:]]:
                del fonems_words[index_fonema]
    i = 0
    while i < len(fonems_words):
        if TestNewFonema(fonems_words[i], fonems_words):
            del fonems_words[i]
            i -= 1
        i += 1
    return fonems_words

# Функция TestNewFonema проверяет, чтобы фонема не являлась
# частью другой фонемы
# condition
# fonems
# fonema
def TestNewFonema(fonema, fonems):
    condition = False
    for i in fonems:
        fonema[1].sort()
        i[1].sort()
        if ((fonema[0] in i[0]) and (fonema[0]!=i[0]) and
            (fonema[1] == i[1])):
            condition = True
    return condition
    

# Функция CombineAllFonems добавляет новые фонемы в общий список фонем
# name_of_old_fonems
def CombineAllFonems(old_fonems, new_fonems):
    names_of_old_fonems = []
    for i in range(len(old_fonems)):
        names_of_old_fonems.append(old_fonems[i][0])
    for i in new_fonems:
        if not (i[0] in names_of_old_fonems):
            old_fonems.append(i)
    return old_fonems

# Функция FindFirstFonema находит первые слова для кроссворда,
# одно из которых должно быть частью другого слова
def FindFirstFonema(words,fonems,num):
    end = False
    for word1 in words:
        length = len(word1)
        for word2 in words:
            if word1 == word2:
                continue
            if word1 == word2[:length]:
                string1 = word1
                string2 = word2
                used_words = [word1[:],word2[:]]
                string1,string2,en = NewFonema(string1,string2,
                                           fonems,used_words,num)
                if en:
                    end = True
                    break
        if end:
            break
    return string1,string2,used_words,en


# Функция NewFonema добавляет слова в кроссворд
# delta
# end
# quantity
# 
def NewFonema(string1,string2,fonems,used_words,q1):
    if len(string1)>len(string2):
        string1,string2 = string2,string1
    str1 = string1
    str2 = string2
    index_start = len(str1)
    index_finish = len(str2)+1
    delta = len(str2)-len(str1)
    end = False
    for i in range(index_start+1,index_finish):
        old_fonema = str2[index_start:i]
        for fonema in fonems:
            if old_fonema == fonema[0]:
                for word in fonema[1]:
                    if len(word) == delta:
                        quantity = len(str1)+len(word)
                        if quantity == q1:
                            condition = (word == str2[index_start:])
                        else:
                            condition = False
                    elif len(word) > delta:
                        condition = (str2[index_start:] in word)
                    else:
                        condition = (word in str2[index_start:])
                    if (old_fonema == word[:len(old_fonema)] and
                        not(word in used_words) and condition):
                        str1 += word
                        used_words.append(word)
                        str1,str2,e = NewFonema(str1,str2,fonems,used_words, q1)
                        if (str1 == str2) and (len(str1) == q1):
                            end = True
                            break
                        else:
                            del used_words[used_words.index(word)]
                            str1 = string1
                            str2 = string2
            if end:
                break
        if end:
            break
    return str1,str2,end

# Считывание значений
# Words - список слов из которых надо составить кроссворд
# n - длина кроссворда
Words = []
F = open('input.txt')
n = int(F.readline())
i = F.readline()
for i in F:
    Words.append(i)
for i in range(len(Words)):
    Words[i] = Words[i][:len(Words[i])-1]
F.close()
# Основная программа
# String1 - первая расшифровка
# String2 - вторая расшифровка
# UsedWords - слова, которые используются в кроссворде
# End - для определения, можно составить кроссворд или нет
#Fonems = FindFonemsInWord(Words[0],Words)###########################
AllFonems = []
for i in range(len(Words)-1):
    FonemsInCurrentWord = FindFonemsInWord(Words[i],Words)
    CombineAllFonems(AllFonems,FonemsInCurrentWord)
#Used_Words = []#####################################################
String1,String2,UsedWords,End = FindFirstFonema(Words,AllFonems,n)


# Вывод
Output = open('Output.txt','w')
if not End:
    Output.write('NO SOLUTION')
else:
    Output.write(String1)
Output.close()
