from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 191
menu_191iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_6")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_6")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_6")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_1")
    ]
])

# ИАЭП направления 191
menu_191iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_6")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_6")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_1")
    ]
])

# ИАНТЭ направоение 191
menu_191iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_1")
    ]
])

# назад к факультетам
back_191_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191")
    ]
])
