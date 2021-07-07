from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 165
menu_165iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_4")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_165_deg_4")
    ]
])

# Направления 165
menu_165iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_4")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств", callback_data="Design_technology_degree_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_165_deg_4")
    ]
])

# назад к факультетам
back_deg_165_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_165")
    ]
])
