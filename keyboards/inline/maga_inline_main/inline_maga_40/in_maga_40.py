from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Направления ИРЭТ
menu_maga_inline_button_40 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_5")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи", callback_data="Infocommunication_technologies_5")
    ],
    [
        InlineKeyboardButton(text="Радиотехника", callback_data="Radio_engineering_maga_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_40_5")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_40_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_40_5")
    ]
])

# Направления ИРЭТ
menu_maga_ineline_button_40_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_40_5")
    ]
])


# назад
back_maga_inline_button_40 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_40")
    ]
])


