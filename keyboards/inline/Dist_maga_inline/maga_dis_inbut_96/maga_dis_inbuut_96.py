from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Направления ИАЭП
menu_dist_maga_96 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление качеством",
                             callback_data="Quality_managementt_maga_dis_3")
    ],
    [
        InlineKeyboardButton(text="Техносферная безопасность",
                             callback_data="Technosphere_safety_maga_dis_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_dis_96_3")
    ]
])

# назад
back_maga_dis_inline_button_96 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_dis_96")
    ]
])