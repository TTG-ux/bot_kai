from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИРЭТ
menu_maga_inline_button_48 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_7")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи",
                             callback_data="Infocommunication_technologies_7")
    ],
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_48_7")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_48_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_48_7")
    ]
])

# Направления ИКТЗИ
menu_maga_ineline_button_48_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_7")
    ],
    [
        InlineKeyboardButton(text="Информационные системы и технологии",
                             callback_data="Information_systems_and_technologies_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_48_7")
    ]
])

# Направления ФМФ
menu_maga_ineline_button_48_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Наноматериалы",
                             callback_data="Nanomaterials_maga_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_48_7")
    ]
])

# назад
back_maga_inline_button_48 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_48")
    ]
])
