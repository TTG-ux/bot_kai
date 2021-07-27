from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 211
menu_211iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_15")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_15")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_15")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_15")
    ],
    [
        InlineKeyboardButton(text="Электроника, микросистемная техника", callback_data="Electronics_15")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_211_1")
    ]
])

# ИАЭП направления 211
menu_211iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_15")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_15")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_15")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_15")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях",
                             callback_data="Environmental_engineering_15")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_211_1")
    ]
])

# ИАНТЭ направоение 211
menu_211iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_15")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_15")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_15")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_15")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии",
                             callback_data="Resource_efficient_technologies_15")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_15")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_15")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация", callback_data="Road_transport_15")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_15")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_211_1")
    ]
])

# ФМФ направоение 211
menu_211iktfiz_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Лазерные технологии и 3D-прототипирование", callback_data="Laser_technologies_15")
    ],
    [
        InlineKeyboardButton(text="Наноинженерия", callback_data="Nanoengineering_15")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_211_1")
    ]
])

# назад к факультетам
back_211_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_211")
    ]
])
