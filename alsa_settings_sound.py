import tkinter as tk
from tkinter import ttk
from menu_systeminfo import menu_sys
from menu_firmware_setting import firmware
from menu_sound import menu_sound
from variable import Tabs

class Applications(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Настройка звука")
        self.geometry("600x400")
        # Создаем меню
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')
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
        menu_sys(self.frames)
        menu_sound(self.frames)
        firmware(self.frames)


if __name__ == "__main__":
    app = Applications()
    app.mainloop()
