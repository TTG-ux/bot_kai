from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Направления ИАЭП
menu_dist_maga_89 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление качеством",
                             callback_data="Quality_managementt_maga_dis_2")
    ],
    [
        InlineKeyboardButton(text="Техносферная безопасность",
                             callback_data="Technosphere_safety_maga_dis_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_dis_89_2")
    ]
])

# назад
back_maga_dis_inline_button_89 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_dis_89")
    ]
])