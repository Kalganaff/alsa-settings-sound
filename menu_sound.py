

#Меню для создания файла и выбора режима sound.conf
from menu_settings import *
#from tkinter import ttk
#from sysinfo import *
from tkinter import ttk


def menu_sound():
    help_menu = ttk.Notebook()
    frame2 = ttk.Frame(help_menu)
    frame2.pack(fill=BOTH, expand=True)
    help_menu.add(frame2, text="Конфигурация параметра модуля snd")
    label2 = ttk.Label(frame2, text="fmkfdldf")

