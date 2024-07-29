from menu_systeminfo import *
from tkinter import *
from tkinter.ttk import *

def firmware(frames):
    # Вкладка прошивки
    optnum = get_firmware_info()
    selected = IntVar()
    selected.set(optnum)

    frame = frames[Tabs.TAB2]
    lbl = Label(frame,
                text="""Настройка конфигурации snd-intel-dsp опция 1 позволяет использовать устаревший драйвер HDaudio. Это работает для колонок и гарнитуры, но не позволяет сделать DMIC(Digital Microphone) захват. В то же время опция 3 поддерживает DMIC, DSP(Digital Signal Processor) может обрабатывать звук более эффективно, SOF(Sound Open Firmware) драйверы обеспечивать лучшую совместимость с современными аудиоустройствами.""",
                font=("Arial", 10),
                background="white",
                wraplength=590,
                justify=LEFT)


    rad1 = Radiobutton(frame,
                       text="Опция - 1",
                       value=1,
                       variable=selected)

    rad3 = Radiobutton(frame,
                       text='Опция - 3',
                       value=3,
                       variable=selected)

    lbl.grid(column=0,
             row=0)

    rad1.place(relx=0,
               rely=0.4,
               anchor="w")

    rad3.place(relx=0,
               rely=0.5,
               anchor="w")

