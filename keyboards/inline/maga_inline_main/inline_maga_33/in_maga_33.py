from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Направления ИРЭТ
menu_maga_inline_button_33 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_maga_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_33_2")
    ]
])

# Направления ИАЭП
menu_maga_ineline_button_33_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление в технических системах",
                             callback_data="Equipment_Management_maga_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_33_2")
    ]
])

# назад
back_maga_inline_button_33 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_33")
    ]
])


