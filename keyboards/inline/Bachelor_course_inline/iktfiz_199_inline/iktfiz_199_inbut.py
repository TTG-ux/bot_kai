from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 199
menu_199iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_10")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_10")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_10")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_199_1")
    ]
])

# ИАЭП направления 199
menu_199iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_10")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_10")
    ],
    [
        InlineKeyboardButton(text="Стандартизация, сертификация и метрология", callback_data="Standardization_10")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_10")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_199_1")
    ]
])

# ИАНТЭ направоение 199
menu_199iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_10")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_10")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_10")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_10")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии", callback_data="Resource_efficient_technologies_10")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_10")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_199_1")
    ]
])

# назад к факультетам
back_199_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_199")
    ]
])
