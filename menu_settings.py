import tkinter
from sysinfo import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo, askyesno
from tkinter import ttk
from tkinter import messagebox


def alsa_version():
    alsa_version = get_alsa_version()
    alsa_label = ttk.Label(text=f"Версия ALSA: {alsa_version}")
    alsa_label.pack()
def kernel_label():
    kernel_version = get_kernel_version()
    kernel_label = ttk.Label(text=f"Версия ядра Linux: {kernel_version}", style="BW.TLabel")
    kernel_label.pack()
def sound_card_label():
    sound_card_name = get_sound_card_name()
    sound_card_label = Label(text=f"Звуковая карта: {sound_card_name}", style="BW.TLabel")
    sound_card_label.pack()
def new_file():
    messagebox.showinfo("New File", "New File selected")

def open_file():
    result = askyesno(title="Предупреждение", message="Чтобы изменения вступили в силу, нужно перезагрузить компьютер. Сделать ее сейчас?")
    if result:
        showinfo("Результат", "Сейчас будет выполнена перезагрузка")
        reboot()

    else:
        showinfo("Результат", "Отмена")
def save_file():
    messagebox.showinfo("Save File", "Save File selected")

def exit_app():
    root = tkinter.Tk()
    root.quit()




