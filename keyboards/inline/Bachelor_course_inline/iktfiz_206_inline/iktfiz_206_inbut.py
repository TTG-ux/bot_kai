from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 206
menu_206iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_12")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_12")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_12")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_12")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_206_1")
    ]
])

# ИАЭП направления 206
menu_206iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_12")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_12")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_12")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_12")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="Environmental_engineering_12")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_206_1")
    ]
])

# ИАНТЭ направоение 206
menu_206iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_12")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_12")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_12")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_12")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии", callback_data="Resource_efficient_technologies_12")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_12")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_12")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация", callback_data="Road_transport_12")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_206_1")
    ]
])

# назад к факультетам
back_206_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_206")
    ]
])
