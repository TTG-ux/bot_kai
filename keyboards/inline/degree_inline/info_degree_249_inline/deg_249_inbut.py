from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 249 ИАНТЭ
menu_249iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_21")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_21")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_deg_21")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_deg_21")
    ],
    [
        InlineKeyboardButton(text="Технологии производства авиакосмической и беспилотной техники из композиционных материалов. Авиокосмическое материаловедение", callback_data="Aerospace_Science_deg_21")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_249_deg_21")
    ]
])

# Направления 249 ИРЭФ-ЦТ
menu_249iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_21")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_21")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_deg_21")
    ],
    [
      InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации", callback_data="Quantum_communications_deg_21")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_249_deg_21")
    ]
])

# Направления 249 ИКТЗИ
menu_249iktfiz_degree_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Защита информации в компьютерных сетях", callback_data="Information_protection_deg_21")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_deg_21")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем", callback_data="Computer_administration_deg_21")
    ],
    [
      InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="Intelligent_information_systems_deg_21")
    ],
    [
        InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BIGDATA", callback_data="BIGDATA_Management_models_deg_21")
    ],
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_deg_21")
    ],
    [
        InlineKeyboardButton(text="Робототехника и цифоровая экономика", callback_data="Robotics_and_digital_economy_deg_21")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_249_deg_21")
    ]
])

# Направления 249 ИАЭП
menu_249iktfiz_degree_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оптико-электронные системы", callback_data="Optoelectronic_systems_deg_21")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_deg_21")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="Environmental_engineering_deg_21")
    ],
    [
        InlineKeyboardButton(text="Управление беспилотными летательными аппаратами. Интеллектуальные технические системмы. Робототехника", callback_data="Control_of_unmanned_aerial_vehicle_deg_21")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_deg_21")
    ],
    [
        InlineKeyboardButton(text="Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="Electrical_of_enterprises_deg_21")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_249_deg_21")
    ]
])

# назад к факультетам
back_deg_249_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_249")
    ]
])
