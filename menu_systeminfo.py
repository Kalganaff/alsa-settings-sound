import tkinter as tk
from menu_settings import *
from tkinter import ttk
from sysinfo import *
from tkinter import ttk
from menu_sound import *
#Создаем выпадающее меню "Системная информация"
def menu_sys():
    #Вкладка системной инфы
    help_menu = ttk.Notebook()
    help_menu.pack(expand=1, fill=BOTH)
    frame1 = ttk.Frame(help_menu)
    frame1.pack(fill=BOTH, expand=True)
    help_menu.add(frame1, text="Системная информация")
    lbl1 = Label(frame1, text=get_message_sys())
    lbl1.grid(column=0, row=0)
#    menu_sound()
    #Вкладка звукового конфига
    frame2 = ttk.Frame(help_menu)
    frame2.pack(fill=BOTH, expand=True)
    help_menu.add(frame2, text="Конфигурация параметра модуля snd")
    lbl2 = Label(frame2, text="fmkfdldf")
    lbl2.grid(column=0, row=0)

    help_menu.pack()

