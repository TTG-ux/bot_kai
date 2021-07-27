from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 193
menu_193iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_7")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_7")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_7")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_193_1")
    ]
])

# ИАЭП направления 193
menu_193iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_7")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_7")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_7")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="Electrical_of_enterprises_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_193_1")
    ]
])

# ИАНТЭ направоение 191
menu_193iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_193_1")
    ]
])

# назад к факультетам
back_193_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_193")
    ]
])
