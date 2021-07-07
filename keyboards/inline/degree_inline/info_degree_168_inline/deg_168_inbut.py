from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 168 ИАНТЭ
menu_168iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_6")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_6")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение", callback_data="Aircraft_and_helicopter_construction_deg_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_168_deg_6")
    ]
])

# Направления 168 ИРЭФ-ЦТ
menu_168iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_6")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_6")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="Intelligent_radio_electronics_deg_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_168_deg_6")
    ]
])

# назад к факультетам
back_deg_168_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_168")
    ]
])
