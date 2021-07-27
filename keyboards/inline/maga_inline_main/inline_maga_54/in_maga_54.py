from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИРЭТ
menu_maga_inline_button_54 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_8")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи",
                             callback_data="Infocommunication_technologies_8")
    ],
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_54_8")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_54_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_54_8")
    ]
])

# Направления ИКТЗИ
menu_maga_ineline_button_54_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_8")
    ],
    [
        InlineKeyboardButton(text="Информационные системы и технологии",
                             callback_data="Information_systems_and_technologies_8")
    ],
    [
        InlineKeyboardButton(text="Информатика и вычислительная техника",
                             callback_data="Computer_science_and_engineering_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_54_8")
    ]
])

# Направления ФМФ
menu_maga_ineline_button_54_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наноматериалы",
                             callback_data="Nanomaterials_maga_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_54_8")
    ]
])

# назад
back_maga_inline_button_54 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_54")
    ]
])
