from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 179 ИАНТЭ
menu_179iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_10")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_10")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_deg_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_179_deg_10")
    ]
])

# Направления 179 ИРЭФ-ЦТ
menu_179iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_10")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_10")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_deg_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_179_deg_10")
    ]
])

# Направления 179 ИКТЗИ
menu_179iktfiz_degree_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Защита информации в компьютерных сетях", callback_data="Information_protection_deg_10")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_deg_10")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем", callback_data="Computer_administration_deg_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_179_deg_10")
    ]
])

# Направления 179 ИАЭП
menu_179iktfiz_degree_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оптико-электронные системы", callback_data="Optoelectronic_systems_deg_10")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_deg_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_179_deg_10")
    ]
])

# назад к факультетам
back_deg_179_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_179")
    ]
])
