from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 150
menu_150iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_150_deg_2")
    ]
])

# Направления 150
menu_150iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_150_deg_2")
    ]
])

# назад к факультетам
back_deg_150_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_150")
    ]
])
