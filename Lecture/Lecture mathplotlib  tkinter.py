# Объединение библиотек mathplotlib и tkinter, программа создает график
# sin(x) и позволяет изменить область просмотра

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def sh():
    but1.config(state = tk.NORMAL)
    a = int(e.get())
    b = int(e1.get())
    pointNum = int(e2.get())
    x = np.linspace(a,b,pointNum)
    y = np.sin(x)
    plt.cla()
    plt.plot(x,y,'b')
    plt.show()

def change():
    plt.axis([int(e3.get()),int(e4.get()),int(e5.get()),int(e6.get())])
    plt.show()

root = tk.Tk()            # Создание окна
root.title('Input')       # Название окна
root.geometry('220x250')  # Размер
app = tk.Frame(root)      # Создание рамки для элементов
app.grid()                # Размещение рамки

lbl0 = tk.Label(app,text = 'Graph')         # Надписи
lbl0.grid(row = 1, column = 1, sticky = tk.W)
lbl1 = tk.Label(app,text = 'Xmin:')
lbl1.grid(row = 2, column = 0, sticky = tk.W)
lbl2 = tk.Label(app,text = 'Xmax:')
lbl2.grid(row = 3, column = 0, sticky = tk.W)
lbl3 = tk.Label(app,text = 'Points number:')
lbl3.grid(row = 4, column = 0, sticky = tk.W)

e = tk.Entry(app)                            # Поля ввода
e.grid(row = 2,column = 1, sticky = tk.W)
e1 = tk.Entry(app)
e1.grid(row = 3,column = 1, sticky = tk.W)
e2 = tk.Entry(app)
e2.grid(row = 4,column = 1, sticky = tk.W)

but = tk.Button(app, text = 'Create',command = sh) # Кнопка
but.grid(row = 5, column = 1, sticky = tk.W)

lbl4 = tk.Label(app,text = 'Axis')          # Надписи
lbl4.grid(row = 7, column = 1, sticky = tk.W)
lbl5 = tk.Label(app,text = 'X First')
lbl5.grid(row = 8, column = 0, sticky = tk.W)
lbl6 = tk.Label(app,text = 'X Last')
lbl6.grid(row = 9, column = 0, sticky = tk.W)
lbl7 = tk.Label(app,text = 'Y First')
lbl7.grid(row = 10, column = 0, sticky = tk.W)
lbl8 = tk.Label(app,text = 'Y Last')
lbl8.grid(row = 11, column = 0, sticky = tk.W)

e3 = tk.Entry(app)                          # Поля ввода
e3.grid(row = 8,column = 1, sticky = tk.W)
e4 = tk.Entry(app)
e4.grid(row = 9,column = 1, sticky = tk.W)
e5 = tk.Entry(app)
e5.grid(row = 10,column = 1, sticky = tk.W)
e6 = tk.Entry(app)
e6.grid(row = 11,column = 1, sticky = tk.W)

but1 = tk.Button(app, text = 'Move',command = change)
but1.grid(row = 12, column = 1, sticky = tk.W)

root.mainloop() # запуск цикла обработки событий
