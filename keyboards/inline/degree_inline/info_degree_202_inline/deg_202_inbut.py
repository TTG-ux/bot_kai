from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 202 ИАНТЭ
menu_202iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_17")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_17")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_deg_17")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_deg_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_202_deg_17")
    ]
])

# Направления 202 ИРЭФ-ЦТ
menu_202iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_17")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_17")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_deg_17")
    ],
    [
      InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации", callback_data="Quantum_communications_deg_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_202_deg_17")
    ]
])

# Направления 202 ИКТЗИ
menu_202iktfiz_degree_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Защита информации в компьютерных сетях", callback_data="Information_protection_deg_17")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_deg_17")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем", callback_data="Computer_administration_deg_17")
    ],
    [
      InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="Intelligent_information_systems_deg_17")
    ],
    [
        InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BIGDATA", callback_data="BIGDATA_Management_models_deg_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_202_deg_17")
    ]
])

# Направления 202 ИАЭП
menu_202iktfiz_degree_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оптико-электронные системы", callback_data="Optoelectronic_systems_deg_17")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_deg_17")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="Environmental_engineering_deg_17")
    ],
    [
        InlineKeyboardButton(text="Управление беспилотными летательными аппаратами. Интеллектуальные технические системмы. Робототехника", callback_data="Control_of_unmanned_aerial_vehicle_deg_17")
    ],
    [
        InlineKeyboardButton(text="Информационно-измерительные системы", callback_data="Information_systems_deg_17")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_202_deg_17")
    ]
])

# назад к факультетам
back_deg_202_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_202")
    ]
])
