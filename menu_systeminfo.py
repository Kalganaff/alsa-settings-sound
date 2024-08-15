from variable import Tabs
from menu_settings import *
from tkinter import *
from tkinter.ttk import *

def alsa_version(frames):
    frame = frames[Tabs.TAB3]
    alsa_version = get_alsa_version()
    alsa_label = ttk.Label(frame, text=f"Версия ALSA: {alsa_version}")
    alsa_label.pack()
def kernel_label(frames):
    frame = frames[Tabs.TAB3]
    kernel_version = get_kernel_version()
    kernel_label = ttk.Label(frame, text=f"Версия ядра Linux: {kernel_version}", style="BW.TLabel")
    kernel_label.pack()
def sound_card_label(frames):
    frame = frames[Tabs.TAB3]
    sound_card_name = get_sound_card_name()
    sound_card_label = Label(frame, text=f"Звуковая карта: {sound_card_name}", style="BW.TLabel")
    sound_card_label.pack()