from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 166
menu_166iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_5")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_5")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение", callback_data="Aircraft_and_helicopter_construction_deg_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_166_deg_5")
    ]
])

# Направления 166
menu_166iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_5")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_166_deg_5")
    ]
])

# назад к факультетам
back_deg_166_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_166")
    ]
])
