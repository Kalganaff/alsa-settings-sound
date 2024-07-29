import os
import subprocess

# Функция для получения названия звуковой карты
def test_error(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды: {e}"

def get_sound_card_name():
    command = "cat /proc/asound/card*/codec* | awk -F: '/Codec/{print $2}'"
    output = test_error(command)
    return output

def get_firmware_info():
    command = "cat /etc/modprobe.d/alsa-sof-firmware-settings.conf | cut -d = -f 2"
    output = test_error(command)
    return output

def get_alsa_version():
    command = "alsactl -v | awk '{print$3}'"
    output = test_error(command)
    return output

# Функция для получения версии ядра
def get_kernel_version():
        command = "uname -r | cut -d . -f -2 "
        output = test_error(command)
        return output

def reboot():
    print("Выполняю перезагрузку")