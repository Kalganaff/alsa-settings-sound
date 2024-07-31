from enum import Enum


class Tabs(Enum):
      TAB1 = "Модуль звука"
      TAB2 = "Настройка прошивки"
      TAB3 = "Системная информация"

default_conf_rad = {
      'variable': 'selected',
      'style': 'design.TRadiobutton'
}