import os
import subprocess

# Функция для получения версии ядра
def get_kernel_version():
    return os.uname().release

# Функция для получения версии ALSA
def get_alsa_version():
    result = subprocess.run(['cat', '/proc/asound/version'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

# Функция для получения названия звуковой карты
def get_sound_card_name():
    result = subprocess.run(['cat', '/proc/asound/cards'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()