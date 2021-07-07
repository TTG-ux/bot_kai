from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 177 ИАНТЭ
menu_177iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_9")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_9")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_deg_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_deg_9")
    ]
])

# Направления 177 ИРЭФ-ЦТ
menu_177iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_9")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_9")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_deg_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_deg_9")
    ]
])

# Направления 177 ИКТЗИ
menu_177iktfiz_degree_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Защита информации в компьютерных сетях", callback_data="Information_protection_deg_9")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_deg_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_deg_9")
    ]
])

# Направления 177 ИАЭП
menu_177iktfiz_degree_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оптико-электронные системы", callback_data="Optoelectronic_systems_deg_9")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_177_deg_9")
    ]
])

# назад к факультетам
back_deg_177_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_177")
    ]
])
