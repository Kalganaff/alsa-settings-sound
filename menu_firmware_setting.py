from menu_systeminfo import *
from tkinter import *
from tkinter.ttk import *

def firmware(frames):
    # Вкладка прошивки
    frame = frames[Tabs.TAB2]
    lbl = Label(frame, text="Настройка конфигурации прошивки ядра 1 - 3")
    lbl.grid(column=0, row=0)