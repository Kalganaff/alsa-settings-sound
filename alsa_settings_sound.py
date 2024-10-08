import tkinter as tk
from tkinter import ttk
from menu_firmware_setting import firmware
from menu_sound import *
from variable import Tabs
from menu_settings import *

class Applications(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Настройка звука")
        self.geometry("600x400")
        # Создаем меню
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')
     #   self.resizable(width=False, height=False)
        self.frames = {}
        # Добавляем вкладки
        self.create_tabs()
        # Наполняем содержимым
        self.populate_tabs()

    def create_tabs(self):
        for tab in Tabs:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=tab.value)
            self.frames[tab] = frame
    def populate_tabs(self):
        menu_sound(self.frames)
        firmware(self.frames)
        alsa_version(self.frames)
        kernel_label(self.frames)
        sound_card_label(self.frames)

if __name__ == "__main__":
    app = Applications()
    app.mainloop()
