import os
import tkinter as tk
from tkinter import messagebox
from menu_systeminfo import *
from variable import Tabs
from tkinter import ttk
from models import *
import subprocess
import json

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

    def show_tooltip(self, event):
        if self.tooltip or not self.text:
            return
        x = event.x_root + 20
        y = event.y_root + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", borderwidth=1,
                         font=("Arial", 10, "normal"))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def attach(self):
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

def save_all_configs(selected_values):
    for model, selected_value in selected_values.items():
        save_config(model, selected_value)

def save_config(model, selected_value):
    config_file = f"/etc/modprobe.d/{model}.conf"
    command = f'echo "options {model} {selected_value}" | pkexec tee {config_file} > /dev/null'

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Сохранение", f"Конфигурация для {model} успешно сохранена!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить конфигурацию: {e}")

def load_previous_configs():
    try:
        with open('sound_config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_to_file(selected_values):
    with open('sound_config.json', 'w') as file:
        json.dump(selected_values, file)

def menu_sound(frames):
    frame2 = frames[Tabs.TAB1]

    style = ttk.Style()
    style.theme_use("clam")
    style.configure('design1.TRadiobutton', background='#B2DFDB', foreground='black', padding=0)

    canvas = tk.Canvas(frame2)
    scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar_frame = ttk.Frame(canvas)

    scrollbar_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollbar_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    row_counter = 0

    selected_values = load_previous_configs()  # Загрузка предыдущих настроек

    current_selections = {}  # Словарь для текущих выборов

    for model, options in hda_codec_mod.items():
        lbl2 = tk.Label(scrollbar_frame, text=f"Настройка звуковых карт {model}")
        lbl2.grid(row=row_counter, column=0, columnspan=2, sticky='w', pady=5)
        row_counter += 1

        selected = tk.IntVar()

        # Установка значения из конфигурации
        selected.set(selected_values.get(model, 1))
        current_selections[model] = selected

        comments = hda_codec_com.get(model, [])

        for i, (text, value) in enumerate(options):
            col = i % 2
            if col == 0 and i != 0:
                row_counter += 1

            rad = ttk.Radiobutton(scrollbar_frame, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.grid(row=row_counter, column=col, sticky='w', padx=5, pady=2)

            if i < len(comments):
                tooltip = Tooltip(rad, comments[i])
                tooltip.attach()

        row_counter += 2

    # Общая кнопка для сохранения всех конфигураций
    save_all_button = tk.Button(scrollbar_frame, text="Сохранить все конфигурации", command=lambda: [save_all_configs({model: var.get() for model, var in current_selections.items()}), save_to_file({model: var.get() for model, var in current_selections.items()})])
    save_all_button.grid(row=row_counter, column=0, columnspan=2, padx=5, pady=10)


