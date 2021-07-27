from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Направления ИАЭП
menu_dist_maga_80 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление качеством",
                             callback_data="Quality_managementt_maga_dis_1")
    ],
])