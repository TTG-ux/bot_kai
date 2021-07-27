from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 208
menu_208iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_13")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_13")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_13")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_13")
    ],
    [
        InlineKeyboardButton(text="Электроника, микросистемная техника", callback_data="Electronics_13")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_208_1")
    ]
])

# ИАЭП направления 208
menu_208iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_13")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_13")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_13")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_13")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="Environmental_engineering_13")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_208_1")
    ]
])

# ИАНТЭ направоение 208
menu_208iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_13")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_13")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_13")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_13")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии", callback_data="Resource_efficient_technologies_13")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_13")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_13")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация", callback_data="Road_transport_13")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_208_1")
    ]
])

# назад к факультетам
back_208_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_208")
    ]
])
