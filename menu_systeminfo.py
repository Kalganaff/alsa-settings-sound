from variable import Tabs
from menu_settings import *
from tkinter import *
from tkinter.ttk import *

def menu_sys(frames):
    #Вкладка системной инфы
    frame = frames[Tabs.TAB1]
    lbl1 = Label(frame, text=alsa_version())
    lbl1 = Label(frame, text=kernel_label())
    lbl1 = Label(frame, text=sound_card_label())
    lbl1.grid(column=0, row=0)

