import tkinter as tk
from menu_settings import *
from tkinter import ttk
from sysinfo import *

# Создаем основное окно
root = tk.Tk()
root.title("Настройка звука")
root.geometry("600x400")  # Устанавливаем размер окна


# Создаем меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Создаем выпадающее меню "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Меню", menu=file_menu)
file_menu.add_command(label="Конфигурация", command=new_file)
file_menu.add_command(label="Профили", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

# Создаем выпадающее меню "Help"
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Системная информация", menu=help_menu)
#help_menu.add_command(label="", command=get_message_sys)



# Настраиваем стиль для ttk
style = ttk.Style()
style.configure('TMenu', background='#ffffff', foreground='#000000', relief='flat', padding=5)
style.configure('TMenuButton', background='#0078d4', foreground='#ffffff', padding=5)
style.map('TMenuButton', background=[('active', '#005a9e')])



# Основной цикл обработки событий
root.mainloop()