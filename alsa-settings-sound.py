import tkinter as tk
import menu_settings
from tkinter import ttk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New File", "New File selected")

def open_file():
    messagebox.showinfo("Open File", "Open File selected")

def save_file():
    messagebox.showinfo("Save File", "Save File selected")

def exit_app():
    root.quit()

# Создаем основное окно
root = tk.Tk()
root.title("Современное Меню Tkinter")
root.geometry("600x400")  # Устанавливаем размер окна

# Создаем меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Создаем выпадающее меню "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Создаем выпадающее меню "Help"
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a modern menu example"))

# Настраиваем стиль для ttk
style = ttk.Style()
style.configure('TMenu', background='#ffffff', foreground='#000000', relief='flat', padding=5)
style.configure('TMenuButton', background='#0078d4', foreground='#ffffff', padding=5)
style.map('TMenuButton', background=[('active', '#005a9e')])

# Основной цикл обработки событий
root.mainloop()