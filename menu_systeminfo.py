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
    lbl1 = Label(frame1, text=alsa_version())
    lbl1 = Label(frame1, text=kernel_label())
    lbl1 = Label(frame1, text=sound_card_label())
    lbl1.grid(column=0, row=0)
    # Вкладка звукового конфига ---------------------------------
    frame2 = ttk.Frame(help_menu)
    selected = IntVar()
    selected.set(0)
    selected.set(1)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='green', foreground='black', padding=15)
    frame2.pack(fill=BOTH, expand=True)
    help_menu.add(frame2, text="Конфигурация snd-intel")
    lbl2 = Label(frame2, text="Настройка звуковых карт")
    lbl2 = Label(frame2, text="ALC280")
    lbl2.grid(column=0, row=0)
    # Настройка кнопок
    rad1 = Radiobutton(frame2, text='3stack', value=1, variable=selected, style='design1.TRadiobutton')
    rad2 = Radiobutton(frame2, text='3stack-digout', value=2, variable=selected, style='design1.TRadiobutton')
    rad3 = Radiobutton(frame2, text='5stack', value=3, variable=selected)
    rad4 = Radiobutton(frame2, text='5stack-digout', value=4, variable=selected)
    rad5 = Radiobutton(frame2, text='6stack', value=5, variable=selected)
    rad6 = Radiobutton(frame2, text='6stack-digout', value=6, variable=selected)

    rad1.grid(column=0, row=1)
    rad2.grid(column=0, row=3)
    rad3.grid(column=0, row=4)
    rad4.grid(column=0, row=5)
    rad5.grid(column=0, row=6)
    rad6.grid(column=0, row=7)


    #Вкладка прошивки
    frame3 = ttk.Frame(help_menu)
    frame3.pack(fill=BOTH, expand=True)
    help_menu.add(frame3, text="Настройка прошивки")
    lbl3 = Label(frame3, text="Настройка конфигурации прошивки ядра 1 - 3")
    lbl3.grid(column=0, row=0)

    # подменю
    #podframe = ttk.Frame(frame2)
    #podframe.pack()
    #label = Label(podframe, text="Подвкладка")

    #Конец
    help_menu.pack()

