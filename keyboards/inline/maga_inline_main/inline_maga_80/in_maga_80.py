from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИРЭТ
menu_maga_inline_button_80 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_17")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи",
                             callback_data="Infocommunication_technologies_17")
    ],
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_17")
    ],
    [
        InlineKeyboardButton(text="Электроника и наноэлектроника",
                             callback_data="Electronics_and_nanoelectronics_maga_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80_17")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_80_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_17")
    ],
    [
        InlineKeyboardButton(text="Электроэнергетика и электротехника",
                             callback_data="Electric_power_and_electrical_engineering_maga_17")
    ],
    [
        InlineKeyboardButton(text="Приборостроение",
                             callback_data="Instrumentation_maga_17")
    ],
    [
        InlineKeyboardButton(text="Оптотехника",
                             callback_data="Optotechnics_maga_17")
    ],
    [
        InlineKeyboardButton(text="Техносферная безопасность",
                             callback_data="Technosphere_safety_maga_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80_17")
    ]
])

# Направления ИКТЗИ
menu_maga_ineline_button_80_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_17")
    ],
    [
        InlineKeyboardButton(text="Информационные системы и технологии",
                             callback_data="Information_systems_and_technologies_17")
    ],
    [
        InlineKeyboardButton(text="Информатика и вычислительная техника",
                             callback_data="Computer_science_and_engineering_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80_17")
    ]
])

# Направления ФМФ
menu_maga_ineline_button_80_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наноматериалы",
                             callback_data="Nanomaterials_maga_17")
    ],
    [
        InlineKeyboardButton(text="Лазерная техника и лазерные технологии",
                             callback_data="Laser_equipment_and_laser_technologies_maga_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80_17")
    ]
])

# Направления ИАНТЭ
menu_maga_ineline_button_80_4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Теплоэнергетика и теплотехника",
                             callback_data="Heat_power_engineering_and_heat_engineering_maga_17")
    ],
    [
        InlineKeyboardButton(text="Конструкторско-технологическое обеспечение машиностроительных производств",
                             callback_data="Design_and_technological_support_maga_17")
    ],
    [
        InlineKeyboardButton(text="Двигатели летательных аппаратов",
                             callback_data="Aircraft_engines_maga_17")
    ],
    [
        InlineKeyboardButton(text="Авиастроение",
                             callback_data="Aircraft_construction_maga_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80_17")
    ]
])

# назад
back_maga_inline_button_80 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_80")
    ]
])
