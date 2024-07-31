from menu_systeminfo import *
from variable import Tabs
from tkinter import ttk
def menu_sound(frames):
# Вкладка звукового конфига ---------------------------------
    frame2 = frames[Tabs.TAB1]
#    canvas = Canvas(frame2, bg="white", width=520, height=300)
#    canvas.pack(anchor=CENTER, expand=1)
    selected = IntVar()
    selected.set(0)
    selected.set(1)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("design.TRadiobutton",
                    foreground='black',
                    font="helvetika 8",
                    padding=0,
                    background="#B2DFDB")

    lbl2 = Label(frame2, text="Настройка звуковых карт")
    lbl2 = Label(frame2, text="ALC280")

    # Настройка кнопок
    rad1 = Radiobutton(frame2, text='3stack', value=1, variable=selected, style='design.TRadiobutton')
    rad2 = Radiobutton(frame2, text='3stack-digout', value=2, variable=selected, style='design.TRadiobutton')
    rad3 = Radiobutton(frame2, text='5stack', value=3, variable=selected, style='design.TRadiobutton')
    rad4 = Radiobutton(frame2, text='5stack-digout', value=4, variable=selected, style='design.TRadiobutton')
    rad5 = Radiobutton(frame2, text='6stack', value=5, variable=selected, style='design.TRadiobutton')
    rad6 = Radiobutton(frame2, text='6stack-digout', value=6, variable=selected, style='design.TRadiobutton')
    btn = Button(frame2,
                 text="Cохранить",
                 command=save_file)
    lbl2.place(relx=0, rely=0.15, anchor="w")
    rad1.place(relx=0, rely=0.20, anchor="w")
    rad2.place(relx=0, rely=0.25, anchor="w")
    rad3.place(relx=0, rely=0.30, anchor="w")
    rad4.place(relx=0, rely=0.35, anchor="w")
    rad5.place(relx=0, rely=0.40, anchor="w")
    rad6.place(relx=0, rely=0.45, anchor="w")
    btn.place(relx=0, rely=0.8, anchor="w")