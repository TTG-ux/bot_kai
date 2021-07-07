from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 247
menu_247iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_23")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_23")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_23")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_23")
    ],
    [
        InlineKeyboardButton(text="Электроника, микросистемная техника", callback_data="Electronics_23")
    ],
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации", callback_data="Quantum_communications_23")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247_1")
    ]
])

# ИАЭП направления 247
menu_247iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_23")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_23")
    ],
    [
        InlineKeyboardButton(text="Стандартизация, сертификация и метрология", callback_data="Standardization_23")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_23")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_23")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях",
                             callback_data="Environmental_engineering_23")
    ],
    [
        InlineKeyboardButton(
            text="Управление беспилотными летательными аппаратами. Интеллектуальные технические системмы. Робототехника",
            callback_data="Control_of_unmanned_aerial_vehicle_23")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247_1")
    ]
])

# ИАНТЭ направоение 247
menu_247iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_23")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_23")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_23")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_23")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии",
                             callback_data="Resource_efficient_technologies_23")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_23")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_23")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация", callback_data="Road_transport_23")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_23")
    ],
    [
        InlineKeyboardButton(text="Двигатели летательных аппаратов", callback_data="Aircraft_engines_23")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_23")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247_1")
    ]
])

# ФМФ направоение 247
menu_247iktfiz_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Лазерные технологии и 3D-прототипирование", callback_data="Laser_technologies_23")
    ],
    [
        InlineKeyboardButton(text="Наноинженерия", callback_data="Nanoengineering_23")
    ],
    [
        InlineKeyboardButton(text="Современные плазменные технологии", callback_data="Modern_plasma_technologies_23")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247_1")
    ]
])

# ИКТЗИ направоение 247
menu_247iktfiz_button_4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Защита информации в компьютерных сетях", callback_data="Information_protection_23")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем", callback_data="Computer_administration_23")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_23")
    ],
    [
        InlineKeyboardButton(text="Программна инженерия", callback_data="Software_engineering_23")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247_1")
    ]
])

# назад к факультетам
back_247_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_247")
    ]
])
