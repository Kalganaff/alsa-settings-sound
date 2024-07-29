from variable import Tabs
from menu_settings import *
from tkinter import *
from tkinter.ttk import *

def menu_sys(frames):
    #Вкладка системной инфы
    frame = frames[Tabs.TAB3]
    lbl = Label(frame, text=alsa_version())
    lbl = Label(frame, text=kernel_label())
    lbl = Label(frame, text=sound_card_label())
    lbl.grid(column=0, row=0)

