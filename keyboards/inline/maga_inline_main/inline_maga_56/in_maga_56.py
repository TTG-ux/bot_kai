from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИРЭТ
menu_maga_inline_button_56 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_9")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи",
                             callback_data="Infocommunication_technologies_9")
    ],
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_9")
    ],
    [
      InlineKeyboardButton(text="Электроника и наноэлектроника",
                           callback_data="Electronics_and_nanoelectronics_maga_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_56_9")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_56_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_56_9")
    ]
])

# Направления ИКТЗИ
menu_maga_ineline_button_56_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_9")
    ],
    [
        InlineKeyboardButton(text="Информационные системы и технологии",
                             callback_data="Information_systems_and_technologies_9")
    ],
    [
        InlineKeyboardButton(text="Информатика и вычислительная техника",
                             callback_data="Computer_science_and_engineering_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_56_9")
    ]
])

# Направления ФМФ
menu_maga_ineline_button_56_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наноматериалы",
                             callback_data="Nanomaterials_maga_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_56_9")
    ]
])

# назад
back_maga_inline_button_56 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_56")
    ]
])
