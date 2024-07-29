from menu_systeminfo import *
from tkinter import *
from tkinter.ttk import *

def firmware(frames):
    # Вкладка прошивки

    selected = IntVar()
    selected.set(0)
    selected.set(1)
    frame = frames[Tabs.TAB2]
    lbl = Label(frame, text="Настройка конфигурации прошивки ядра 1 - 3")
    rad1 = Radiobutton(frame, text='Опция - 1', value=0, variable=selected)
    rad3 = Radiobutton(frame, text='Опция - 3', value=1, variable=selected)
    lbl.grid(column=0, row=0)
    rad1.grid(column=0, row=1)
    rad3.grid(column=0, row=2)