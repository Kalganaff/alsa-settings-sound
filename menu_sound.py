from menu_systeminfo import *
from variable import Tabs
from tkinter import ttk
from models import *
import tkinter as tk
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

        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10, "normal"))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def attach(self):
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)


def menu_sound(frames):
    frame2 = frames[Tabs.TAB1]  # Здесь нужно заменить индекс на нужный вам

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

    for model, options in hda_codec_mod.items():
        lbl2 = tk.Label(scrollbar_frame, text=f"Настройка звуковых карт {model}")
        lbl2.grid(row=row_counter, column=0, columnspan=2, sticky='w', pady=5)
        row_counter += 1

        selected = tk.IntVar()
        selected.set(1)

        # Получаем комментарии для текущей модели
        comments = hda_codec_com.get(model, [])

        # Цикл для создания радиокнопок
        for i, (text, value) in enumerate(options):
            col = i % 2
            if col == 0 and i != 0:
                row_counter += 1

            rad = ttk.Radiobutton(scrollbar_frame, text=text, value=value, variable=selected, style='design1.TRadiobutton')
            rad.grid(row=row_counter, column=col, sticky='w', padx=5, pady=2)

            # Добавляем всплывающую подсказку
            if i < len(comments):
                tooltip = Tooltip(rad, comments[i])
                tooltip.attach()

        row_counter += 2



