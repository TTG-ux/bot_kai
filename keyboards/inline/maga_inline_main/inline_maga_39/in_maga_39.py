from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Направления ИРЭТ
menu_maga_inline_button_39 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_4")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи", callback_data="Infocommunication_technologies_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_39_4")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_39_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_39_4")
    ]
])

# Направления ИРЭТ
menu_maga_ineline_button_39_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Прикладная математика и информатика",
                             callback_data="Applied_athematics_maga_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_39_4")
    ]
])


# назад
back_maga_inline_button_39 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_39")
    ]
])


