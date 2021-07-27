from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 203
menu_203iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_11")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_11")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_11")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_11")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_203_1")
    ]
])

# ИАЭП направления 203
menu_203iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_11")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_11")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_11")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_11")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_203_1")
    ]
])

# ИАНТЭ направоение 203
menu_203iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_11")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_11")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_11")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_11")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии", callback_data="Resource_efficient_technologies_11")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_11")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_11")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_203_1")
    ]
])

# назад к факультетам
back_203_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_203")
    ]
])
