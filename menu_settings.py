import tkinter
from sysinfo import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk

def get_message_sys():
    # Создание главного окна
    # root = tkinter.Tk()

    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", background="white")

    # Добавление меток с информацией
    kernel_version = get_kernel_version()
    alsa_version = get_alsa_version()
    sound_card_name = get_sound_card_name()

    kernel_label = ttk.Label(text=f"Версия ядра: {kernel_version}", style="BW.TLabel")
    alsa_label = ttk.Label(text=f"Версия ALSA: {alsa_version}")
    sound_card_label = ttk.Label(text=f"Звуковая карта: {sound_card_name}", style="BW.TLabel")

    kernel_label.pack(pady=10)
    alsa_label.pack(pady=10)
    sound_card_label.pack(pady=10)

    # Запуск главного цикла обработки событий
    #root.mainloop()


def new_file():
    messagebox.showinfo("New File", "New File selected")

def open_file():
    messagebox.showinfo("Open File", "Open File selected")

def save_file():
    messagebox.showinfo("Save File", "Save File selected")

def exit_app():
    root.quit()






