from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ИРЭЫ-ЦТ Направления 251
menu_251iktfiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_systems_iktfiz_25")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_25")
    ],
    [
        InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита",
                             callback_data="information_protection_25")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_25")
    ],
    [
        InlineKeyboardButton(text="Электроника, микросистемная техника", callback_data="Electronics_25")
    ],
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_25")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251_1")
    ]
])

# ИАЭП направления 251
menu_251iktfiz_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оптико-электронные системы", callback_data="Optoelectronic_systems_25")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_25")
    ],
    [
        InlineKeyboardButton(text="Стандартизация, сертификация и метрология", callback_data="Standardization_25")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_25")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей",
                             callback_data="Electrical_of_enterprises_25")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях",
                             callback_data="Environmental_engineering_25")
    ],
    [
        InlineKeyboardButton(
            text="Управление беспилотными летательными аппаратами. Интеллектуальные технические системмы. Робототехника",
            callback_data="Control_of_unmanned_aerial_vehicle_25")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251_1")
    ]
])

# ИАНТЭ направоение 251
menu_251iktfiz_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение",
            callback_data="Aerospace_Science_25")
    ],
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_25")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_25")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_25")
    ],
    [
        InlineKeyboardButton(text="Энерго - и ресурсоэффективные технологии",
                             callback_data="Resource_efficient_technologies_25")
    ],
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_25")
    ],
    [
        InlineKeyboardButton(text="Ракетные двигатели", callback_data="Rocket_engines_25")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация", callback_data="Road_transport_25")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_25")
    ],
    [
        InlineKeyboardButton(text="Двигатели летательных аппаратов", callback_data="Aircraft_engines_25")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_25")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251_1")
    ]
])

# ФМФ направоение 251
menu_251iktfiz_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Лазерные технологии и 3D-прототипирование", callback_data="Laser_technologies_25")
    ],
    [
        InlineKeyboardButton(text="Наноинженерия", callback_data="Nanoengineering_25")
    ],
    [
        InlineKeyboardButton(text="Современные плазменные технологии", callback_data="Modern_plasma_technologies_25")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251_1")
    ]
])

# ИКТЗИ направоение 251
menu_251iktfiz_button_4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Защита информации в компьютерных сетях", callback_data="Information_protection_25")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем",
                             callback_data="Computer_administration_25")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_25")
    ],
    [
        InlineKeyboardButton(text="Программна инженерия", callback_data="Software_engineering_25")
    ],
    [
        InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BIGDATA", callback_data="BIGDATA_Management_models_25")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="Intelligent_information_systems_25")
    ],
    [
        InlineKeyboardButton(text="Робототехника и цифоровая экономика", callback_data="Robotics_and_digital_economy_25")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251_1")
    ]
])

# назад к факультетам
back_251_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_251")
    ]
])
