from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 182
menu_181iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="Transmission_systems_iktfiz_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_181_1")
    ]
])

# ИАЭП направления 182
menu_181iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_3")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_181_1")
    ]
])

# ИАНТЭ направоение 181
menu_181iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение", callback_data="Aerospace_Science_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_181_1")
    ]
])

# назад
back_181_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_181")
    ]
])