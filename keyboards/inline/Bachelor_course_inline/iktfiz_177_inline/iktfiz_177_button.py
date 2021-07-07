from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# ИРЭЫ-ЦТ Направления 177
menu_177iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="Transmission_systems_iktfiz_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_1")
    ]
])

# ИАЭП направления 177
menu_177iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_1")
    ]
])

# назад
back_177_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177")
    ]
])