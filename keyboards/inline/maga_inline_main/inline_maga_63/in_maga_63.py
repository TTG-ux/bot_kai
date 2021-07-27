from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИРЭТ
menu_maga_inline_button_63 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_10")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи",
                             callback_data="Infocommunication_technologies_10")
    ],
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_10")
    ],
    [
      InlineKeyboardButton(text="Электроника и наноэлектроника",
                           callback_data="Electronics_and_nanoelectronics_maga_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63_10")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_63_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63_10")
    ]
])

# Направления ИКТЗИ
menu_maga_ineline_button_63_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_10")
    ],
    [
        InlineKeyboardButton(text="Информационные системы и технологии",
                             callback_data="Information_systems_and_technologies_10")
    ],
    [
        InlineKeyboardButton(text="Информатика и вычислительная техника",
                             callback_data="Computer_science_and_engineering_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63_10")
    ]
])

# Направления ФМФ
menu_maga_ineline_button_63_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наноматериалы",
                             callback_data="Nanomaterials_maga_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63_10")
    ]
])

# Направления ИАНТЭ
menu_maga_ineline_button_63_4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Теплоэнергетика и теплотехника",
                             callback_data="Heat_power_engineering_and_heat_engineering_maga_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63_10")
    ]
])

# назад
back_maga_inline_button_63 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_63")
    ]
])
