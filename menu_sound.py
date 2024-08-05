from menu_systeminfo import *
from variable import Tabs
from tkinter import ttk
from models import *

def menu_sound1(frames):
    # Вкладка звукового конфига
    frame2 = frames[Tabs.TAB1] # Здесь нужно заменить индекс на нужный вам
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='#B2DFDB', foreground='black', padding=0)
    
    rely_counter = 0.15
    relx_counter = 0

    for model, options in hda_codec_mod.items():
        lbl2 = Label(frame2, text=f"Настройка звуковых карт {model}")
        lbl2.place(relx=relx_counter, rely=0.1*rely_counter, anchor="w")
        rely_counter += 0.05

        
        selected = IntVar()
        selected.set(1)
        
        # Цикл для создания радиокнопок
        for i, (text, value) in enumerate(options):
            if i % 2 == 0 and i != 0:
                rely_counter += 0.05
                relx_counter += 0.03

            relx = 0.1 * relx_counter
            rely = 0.1 * rely_counter
            rad = Radiobutton(frame2, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.place(relx=relx, rely=rely, anchor="w")

            rely_counter += 1

        rely_counter = 0
        relx_counter += 1




def menu_sound2(frames):
    # Вкладка звукового конфига
    frame2 = frames[Tabs.TAB1] # Здесь нужно заменить индекс на нужный вам

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='#B2DFDB', foreground='black', padding=0)

    row_counter = 0
    col_counter = 0

    for model, options in hda_codec_mod.items():
        lbl2 = Label(frame2, text=f"Настройка звуковых карт {model}")
        lbl2.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=5)
        row_counter += 1

        selected = IntVar()
        selected.set(1)

        # Цикл для создания радиокнопок
        for i, (text, value) in enumerate(options):
            if i % 2 == 0 and i != 0:
                row_counter += 1
                col_counter += 1
            
            rad = Radiobutton(frame2, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=2)
            row_counter += 1

        # Сброс счетчиков для следующей модели
        row_counter += 1
        col_counter = 0


def menu_sound(frames):
    # Вкладка звукового конфига
    frame2 = frames[Tabs.TAB1] # Здесь нужно заменить индекс на нужный вам

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='#B2DFDB', foreground='black', padding=0)

    row_counter = 0
    col_counter = 0

    for index, (model, options) in enumerate(hda_codec_mod.items()):
        if index % 2 == 0 and index != 0:
            row_counter = 0
            col_counter += 1

        lbl2 = Label(frame2, text=f"Настройка звуковых карт {model}")
        lbl2.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=5)
        row_counter += 1

        selected = IntVar()
        selected.set(1)

        # Цикл для создания радиокнопок
        for text, value in options:
            rad = Radiobutton(frame2, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=2)
            row_counter += 1

        row_counter += 1  # Добавляем пустую строку между группами



def menu_sound3(frames):
    # Вкладка звукового конфига
    frame2 = frames[Tabs.TAB1] # Здесь нужно заменить индекс на нужный вам

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='#B2DFDB', foreground='black', padding=0)

    row_counter = 0
    col_counter = 0

    for index, (model, options) in enumerate(hda_codec_mod.items()):
        if index % 2 == 0 and index != 0:
            row_counter = 0
            col_counter += 1

        lbl2 = Label(frame2, text=f"Настройка звуковых карт {model}")
        lbl2.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=5)
        row_counter += 1

        selected = IntVar()
        selected.set(1)

        # Цикл для создания радиокнопок
        for text, value in options:
            rad = Radiobutton(frame2, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.grid(column=col_counter, row=row_counter, sticky='w', padx=10, pady=2)
            row_counter += 1

        row_counter += 1  # Добавляем пустую строку между группами


