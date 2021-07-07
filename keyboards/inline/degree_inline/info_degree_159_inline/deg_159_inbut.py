from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 159
menu_159iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_159_deg_3")
    ]
])

# Направления 159
menu_159iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_3")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств", callback_data="Design_technology_degree_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_159_deg_3")
    ]
])

# назад к факультетам
back_deg_159_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_159")
    ]
])
