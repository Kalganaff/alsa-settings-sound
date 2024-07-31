hda_codec_com = {
    "ALC880": [
        "3stack: 3-разъемный вход сзади и выход для наушников",
        "3stack-digout: 3-разъемный вход сзади, выход для наушников и цифровой выход SPDIF",
        "5stack: 5-разъемный вход сзади, 2-разъемный спереди",
        "5stack-digout: 5-разъемный вход сзади, 2-разъемный спереди, цифровой выход SPDIF",
        "6stack: 6-разъемный вход сзади, 2-разъемный спереди",
        "6stack-digout: 6-разъемный вход с цифровым выходом SPDIF",
        "6stack-automute: 6-разъемный вход с определением разъема для наушников"
    ],
    "ALC260": [
        "gpio1: Включить GPIO1",
        "coef: Включить EAPD через таблицу COEF",
        "fujitsu: Особые настройки для Fujitsu-Siemens S7020",
        "fujitsu-jwse: Особые настройки для Fujitsu-Siemens S7020 с режимами разъемов и поддержкой микрофона в наушниках"
    ],
    "ALC262": [
        "inv-dmic: Обходной путь для инвертированного встроенного микрофона",
        "fsc-h270: Исправления для Fujitsu-Siemens Celsius H270",
        "fsc-s7110: Исправления для Fujitsu-Siemens Lifebook S7110",
        "hp-z200: Исправления для HP Z200",
        "tyan: Исправления для Tyan Thunder n6650W",
        "lenovo-3000: Исправления для Lenovo 3000",
        "benq: Исправления для Benq ED8",
        "benq-t31: Исправления для Benq T31",
        "bayleybay: Исправления для Intel BayleyBay"
    ],
    "ALC267/268": [
        "inv-dmic: Обходной путь для инвертированного встроенного микрофона",
        "hp-eapd: Отключение HP EAPD на NID 0x15",
        "spdif: Включить цифровой выход SPDIF на NID 0x1e"
    ],
    "ALC22x/23x/25x/269/27x/28x/29x": [
        "laptop-amic: Ноутбуки с аналоговым входом для микрофона",
        "laptop-dmic: Ноутбуки с цифровым входом для микрофона",
        "alc269-dmic: Включить обходной путь для цифрового микрофона ALC269(VA)",
        "alc271-dmic: Включить обходной путь для цифрового микрофона ALC271X",
        "inv-dmic: Обходной путь для инвертированного встроенного микрофона",
        "headset-mic: Обозначает комбинированный разъем для наушников и микрофона",
        "headset-mode: Более полная поддержка гарнитур для ALC269 и аналогов",
        "headset-mode-no-hp-mic: Поддержка режима гарнитуры без микрофона для наушников",
        "lenovo-dock: Включает ввод-вывод док-станции для некоторых моделей Lenovo",
        "hp-gpio-led: Поддержка светодиодов GPIO на ноутбуках HP",
        "hp-dock-gpio-mic1-led: Док-станция HP с поддержкой светодиода микрофона",
        "dell-headset-multi: Разъем для гарнитуры, который также может использоваться как вход для микрофона",
        "dell-headset-dock: Разъем для гарнитуры (без микрофона), а также ввод-вывод док-станции",
        "dell-headset3: Разъем для гарнитуры (без микрофона), а также ввод-вывод док-станции, вариант 3",
        "dell-headset4: Разъем для гарнитуры (без микрофона), а также ввод-вывод док-станции, вариант 4",
        "alc283-dac-wcaps: Исправления для Chromebook с ALC283",
        "alc283-sense-combo: Обнаружение комбинированного разъема на ALC283",
        "tpt440-dock: Конфигурации контактов для поддержки док-станции Lenovo Thinkpad",
        "tpt440: Настройки Lenovo Thinkpad T440s",
        "tpt460: Настройки Lenovo Thinkpad T460/560",
        "tpt470-dock: Настройки док-станции Lenovo Thinkpad T470",
        "dual-codecs: Ноутбуки Lenovo с двумя кодеками",
        "alc700-ref: Эталонная плата Intel с кодеком ALC700",
        "vaio: Исправления контактов для ноутбуков Sony VAIO",
        "dell-m101z: Настройка COEF для Dell M101z",
        "asus-g73jw: Исправление контактов сабвуфера для ASUS G73JW",
        "lenovo-eapd: Инвертированная настройка EAPD для ноутбуков Lenovo",
        "sony-hweq: Настройка COEF для аппаратного эквалайзера для ноутбуков Sony",
        "pcm44k: Фиксированные ограничения PCM 44kHz (для проблемных устройств)",
        "lifebook: Исправления контактов док-станции для Fujitsu Lifebook",
        "lifebook-extmic: Исправление контактов микрофона гарнитуры для Fujitsu Lifebook",
        "lifebook-hp-pin: Исправление контактов наушников для Fujitsu Lifebook",
        "lifebook-u7x7: Исправления для Lifebook U7x7",
        "alc269vb-amic: Исправление контактов аналогового микрофона для ALC269VB",
        "alc269vb-dmic: Исправление контактов цифрового микрофона для ALC269VB",
        "hp-mute-led-mic1: Светодиод отключения звука через контакт Mic1 на HP",
        "hp-mute-led-mic2: Светодиод отключения звука через контакт Mic2 на HP",
        "hp-mute-led-mic3: Светодиод отключения звука через контакт Mic3 на HP",
        "hp-gpio-mic1: Светодиод GPIO и Mic1 на HP",
        "hp-line1-mic1: Светодиод отключения звука через контакты Line1 и Mic1 на HP",
        "noshutup: Пропустить вызов shutup",
        "sony-nomic: Исправление контактов микрофона гарнитуры для ноутбуков Sony",
        "aspire-headset-mic: Исправление контактов гарнитуры для Acer Aspire",
        "asus-x101: Исправления для ASUS X101",
        "acer-ao7xx: Исправления для Acer AO7xx",
        "acer-aspire-e1: Исправления для Acer Aspire E1",
        "acer-ac700: Исправления для Acer AC700",
        "limit-mic-boost: Ограничение усиления встроенного микрофона на ноутбуках Lenovo",
        "asus-zenbook: Исправления для ASUS Zenbook",
        "asus-zenbook-ux31a: Исправления для ASUS Zenbook UX31A",
        "ordissimo: Исправления для Ordissimo EVE2 (или Malata PC-B1303)",
        "asus-tx300: Исправления для ASUS TX300",
        "alc283-int-mic: Настройка COEF для встроенного микрофона на Lenovo с ALC283",
        "mono-speakers: Исправления для сабвуфера и гарнитуры на Dell Inspiron",
        "alc290-subwoofer: Исправления сабвуфера для Dell Vostro",
        "thinkpad: Связь с драйвером thinkpad_acpi для ноутбуков Lenovo",
        "dmic-thinkpad: Связь thinkpad_acpi + поддержка цифрового микрофона",
        "alc255-acer: Исправления для Acer с кодеком ALC255",
        "alc255-asus: Исправления для ASUS с кодеком ALC255",
        "alc255-dell1: Исправления для Dell с кодеком ALC255",
        "alc255-dell2: Исправления для Dell с кодеком ALC255, вариант 2",
        "alc293-dell1: Исправления для Dell с кодеком ALC293",
        "alc283-headset: Исправления контактов гарнитуры для ALC283",
        "aspire-v5: Исправления для Acer Aspire V5",
        "hp-gpio4: Светодиоды GPIO и исправления контактов Mic1 на HP",
        "hp-gpio-led: Светодиоды GPIO на HP",
        "hp-gpio2-hotkey: Светодиоды GPIO с обработкой горячих клавиш на HP",
        "hp-dock-pins: Светодиоды GPIO и поддержка док-станции на HP",
        "hp-dock-gpio-mic: Светодиоды GPIO, светодиод отключения микрофона и поддержка док-станции на HP",
        "hp-9480m: Исправления для HP 9480m",
        "alc288-dell1: Исправления для Dell с кодеком ALC288",
        "alc288-dell-xps13: Исправления для Dell XPS13 с кодеком ALC288",
        "dell-e7x: Исправления для Dell E7x",
        "alc293-dell: Исправления для Dell с кодеком ALC293",
        "alc298-dell1: Исправления для Dell с кодеком ALC298",
        "alc298-dell-aio: Исправления для Dell AIO с кодеком ALC298",
        "alc275-dell-xps: Исправления для Dell XPS с кодеком ALC275",
        "lenovo-spk-noise: Обходной путь для шума динамиков на ноутбуках Lenovo",
        "lenovo-hotkey: Поддержка горячих клавиш через контакт Mic2 на ноутбуках Lenovo",
        "dell-spk-noise: Обходной путь для шума динамиков на ноутбуках Dell",
        "alc255-dell1: Исправления для Dell с кодеком ALC255",
        "alc295-disable-dac3: Отключение маршрутизации DAC3 на ALC295",
        "alc280-hp-headset: Исправления для гарнитуры на HP Elitebook",
        "alc221-hp-mic: Исправления контактов переднего микрофона на HP",
        "alc298-spk-volume: Обходной путь для маршрутизации динамиков на ALC298",
        "dell-inspiron-7559: Исправления для Dell Inspiron 7559",
        "ativ-book: Исправления для Samsung Ativ Book 8",
        "alc221-hp-mic: Исправления для гарнитуры на HP с кодеком ALC221",
        "alc256-asus-mic: Исправления для ASUS с кодеком ALC256"
    ]
}

# Список моделей кодеков с цифрами для кнопок
hda_codec_mod = {
    "ALC880": [
        ("3stack", 1),
        ("3stack-digout", 2),
        ("5stack", 3),
        ("5stack-digout", 4),
        ("6stack", 5),
        ("6stack-digout", 6),
        ("6stack-automute", 7)
    ],
    "ALC260": [
        ("gpio1", 1),
        ("coef", 2),
        ("fujitsu", 3),
        ("fujitsu-jwse", 4)
    ],
    "ALC262": [
        ("inv-dmic", 1),
        ("fsc-h270", 2),
        ("fsc-s7110", 3),
        ("hp-z200", 4),
        ("tyan", 5),
        ("lenovo-3000", 6),
        ("benq", 7),
        ("benq-t31", 8),
        ("bayleybay", 9)
    ],
    "ALC267/268": [
        ("inv-dmic", 1),
        ("hp-eapd", 2),
        ("spdif", 3)
    ],
    "ALC22x/23x/25x/269/27x/28x/29x": [
        ("laptop-amic", 1),
        ("laptop-dmic", 2),
        ("alc269-dmic", 3),
        ("alc271-dmic", 4),
        ("inv-dmic", 5),
        ("headset-mic", 6),
        ("headset-mode", 7),
        ("headset-mode-no-hp-mic", 8),
        ("lenovo-dock", 9),
        ("hp-gpio-led", 10),
        ("hp-dock-gpio-mic1-led", 11),
        ("dell-headset-multi", 12),
        ("dell-headset-dock", 13),
        ("dell-headset3", 14),
        ("dell-headset4", 15),
        ("alc283-dac-wcaps", 16),
        ("alc283-sense-combo", 17),
        ("tpt440-dock", 18),
        ("tpt440", 19),
        ("tpt460", 20),
        ("tpt470-dock", 21),
        ("dual-codecs", 22),
        ("alc700-ref", 23),
        ("vaio", 24),
        ("dell-m101z", 25),
        ("asus-g73jw", 26),
        ("lenovo-eapd", 27),
        ("sony-hweq", 28),
        ("pcm44k", 29),
        ("lifebook", 30),
        ("lifebook-extmic", 31),
        ("lifebook-hp-pin", 32),
        ("lifebook-u7x7", 33),
        ("alc269vb-amic", 34),
        ("alc269vb-dmic", 35),
        ("hp-mute-led-mic1", 36),
        ("hp-mute-led-mic2", 37),
        ("hp-mute-led-mic3", 38),
        ("hp-gpio-mic1", 39),
        ("hp-line1-mic1", 40),
        ("noshutup", 41),
        ("sony-nomic", 42),
        ("aspire-headset-mic", 43),
        ("asus-x101", 44),
        ("acer-ao7xx", 45),
        ("acer-aspire-e1", 46),
        ("acer-ac700", 47),
        ("limit-mic-boost", 48),
        ("asus-zenbook", 49),
        ("asus-zenbook-ux31a", 50),
        ("ordissimo", 51),
        ("asus-tx300", 52),
        ("alc283-int-mic", 53),
        ("mono-speakers", 54),
        ("alc290-subwoofer", 55),
        ("thinkpad", 56),
        ("dmic-thinkpad", 57),
        ("alc255-acer", 58),
        ("alc255-asus", 59),
        ("alc255-dell1", 60),
        ("alc255-dell2", 61),
        ("alc293-dell1", 62),
        ("alc283-headset", 63),
        ("aspire-v5", 64),
        ("hp-gpio4", 65),
        ("hp-gpio-led", 66),
        ("hp-gpio2-hotkey", 67),
        ("hp-dock-pins", 68),
        ("hp-dock-gpio-mic", 69),
        ("hp-9480m", 70),
        ("alc288-dell1", 71),
        ("alc288-dell-xps13", 72),
        ("dell-e7x", 73),
        ("alc293-dell", 74),
        ("alc298-dell1", 75),
        ("alc298-dell-aio", 76),
        ("alc275-dell-xps", 77),
        ("lenovo-spk-noise", 78),
        ("lenovo-hotkey", 79),
        ("dell-spk-noise", 80),
        ("alc255-dell1", 81),
        ("alc295-disable-dac3", 82),
        ("alc280-hp-headset", 83),
        ("alc221-hp-mic", 84),
        ("alc298-spk-volume", 85),
        ("dell-inspiron-7559", 86),
        ("ativ-book", 87),
        ("alc221-hp-mic", 88),
        ("alc256-asus-mic", 89)
    ]
}
