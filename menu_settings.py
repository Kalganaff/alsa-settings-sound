import tkinter
from sysinfo import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo, askyesno
from tkinter import ttk
from tkinter import messagebox
from variable import Tabs


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




