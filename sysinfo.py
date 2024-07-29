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
def test_error_sound_card_name(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды: {e}"

def get_sound_card_name():
    command = "cat /proc/asound/card*/codec* | awk -F: '/Codec/{print $2}'"
    output = test_error_sound_card_name(command)
    return output

print("Название звуковой карты:", get_sound_card_name())
#Название звуковой карты: b'VIA VT1705'