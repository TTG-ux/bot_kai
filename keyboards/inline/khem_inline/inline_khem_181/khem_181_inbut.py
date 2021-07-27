from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Направления ИАНТЭ 181
menu_181khem_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
                             callback_data="Aerospace_Science_khem_1")
    ]
])

