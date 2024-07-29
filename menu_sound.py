from menu_systeminfo import *
from variable import Tabs
from tkinter import ttk
def menu_sound(frames):
# Вкладка звукового конфига ---------------------------------
    frame2 = frames[Tabs.TAB2]
    selected = IntVar()
    selected.set(0)
    selected.set(1)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='green', foreground='black', padding=15)
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
