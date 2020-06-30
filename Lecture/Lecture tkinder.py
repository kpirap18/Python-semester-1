# Графические примитивы
from tkinter import *
root = Tk()

canv = Canvas(root, width = 500, height = 500, bg = 'lightblue', cursor = 'pencil') # создание холста

# Линия
canv.create_line(200,50,300,50,fill = 'blue') 
canv.create_line(0,0,100,100,arrow = LAST)

# Прямоугольник
x = 75
y = 110
canv.create_rectangle(x,y,x+80,y+50,fill = 'white', outline = 'blue')

# Многоугольники 
canv.create_polygon([250,100],[200,150],[300,150],fill = 'yellow') # Треуголдьник
canv.create_polygon([300,80],[400,80],[450,75],[450,200],[300,180],\
                    [330,160],outline = 'white', smooth = 1)

# Эллипс
canv.create_oval([20,200],[150,300],fill = 'gray50')

# Дуги
canv.create_arc([160,230],[230,330],start = 0, extent = 140,fill = 'lightgreen')
canv.create_arc([250,230],[320,330],start = 0, extent = 140,style = CHORD,fill = 'green')
canv.create_arc([340,230],[410,330],start = 0, extent = 140,style = ARC,outline = 'darkgreen')

# Текст
canv.create_text(20,330,text = 'Опыты с графическими примитивами\nна холсте', font = 'Verdana 12',anchor = 'w',justify = CENTER,fill = 'red')

# Много квадратов
x = 10
while x<450:
    canv.create_rectangle(x,400,x+50,450)
    x += 60

    
canv.pack()
root.mainloop()
