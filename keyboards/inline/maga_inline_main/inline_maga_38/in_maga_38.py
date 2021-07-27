from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Направления ИРЭТ
menu_maga_inline_button_38 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_3")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные технологии и системы связи", callback_data="Infocommunication_technologies_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_38_3")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_38_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_38_3")
    ]
])

# назад
back_maga_inline_button_38 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_38")
    ]
])


