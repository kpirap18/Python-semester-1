# Передвижение шарика
from tkinter import *

# Передвижение шарика
def up():
    canv.move(obj,0,-10)
def down():
    canv.move(obj,0,10)
def left():
    canv.move(obj,-10,0)
def right():
    canv.move(obj,10,0)

'''def time_move(n):
    if n<487:
        canv.move(obj,0,1)
        canv.after(5, lambda:time_move(n+1))'''

draw = Tk()
control = Tk()
control.geometry('50x200+1000+500') # Меню

# Поле для шарика
canv = Canvas(draw, height = 800, width = 600, background = '#FFFF00') 

# Кнопки(вверх, вниз, влево, вправо, выход)
btn_up = Button(control,text = 'up', command = up)
btn_down = Button(control,text = 'down', command = down)
btn_left = Button(control,text = 'left', command = left)
btn_right = Button(control,text = 'right', command = right)
btn_exit = Button(control,text = 'exit', command = exit)

# Шарик
obj = canv.create_oval(10,10,30,30,fill = '#FFFFFF', width = 2)

'''canv.after (5,lambda:time_move(0))'''

# Размеры кнопок
btn_up.pack(padx = 20, pady = 5)
btn_down.pack(padx = 20, pady = 5)
btn_left.pack(padx = 20, pady = 5)
btn_right.pack(padx = 20, pady = 5)
btn_exit.pack(padx = 20, pady = 5)

canv.pack()
draw.mainloop()
control.mainloop()
