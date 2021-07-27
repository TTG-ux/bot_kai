from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления ИАНТЭ 206
menu_206khem_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_khem_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_khem_206_2")
    ]
])

# Направления ИАЭП 206
menu_206khem_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Биотехнические и медицинские аппараты и системы",
                             callback_data="Environmental_engineering_khem_206")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_khem_206_2")
    ]
])

# назад
back_206_khem_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_khem_206")
    ]
])

