from tkinter import *
from tkinter.ttk import *

import time


root = Tk()
root.title('Clock')
def time_1():
    time_ = time.strftime('%H:%M:%S')
    label.config(text=time_)
    label.after(1000,time_1)

label = Label(root,font=('data/font/DIGITAL.TXT',80),background='black',foreground='white')
label.pack(anchor='center')

time_1()
mainloop()