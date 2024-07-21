import tkinter
import sysinfo
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# Создание главного окна
root = tkinter.Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Добавление меток с информацией
kernel_version = sysinfo.get_kernel_version()
alsa_version = sysinfo.get_alsa_version()
sound_card_name = sysinfo.get_sound_card_name()

kernel_label = ttk.Label(text=f"Версия ядра: {kernel_version}", style="BW.TLabel")
alsa_label = ttk.Label(text=f"Версия ALSA: {alsa_version}")
sound_card_label = ttk.Label(text=f"Звуковая карта: {sound_card_name}", style="BW.TLabel")


kernel_label.pack(pady=10)
alsa_label.pack(pady=10)
sound_card_label.pack(pady=10)

# Запуск главного цикла обработки событий
root.mainloop()
