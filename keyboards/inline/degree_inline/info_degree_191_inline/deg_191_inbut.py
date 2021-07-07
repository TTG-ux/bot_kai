from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления 191 ИАНТЭ
menu_191iktfiz_degree_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кораблестроение", callback_data="Shipbuilding_deg_14")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_deg_14")
    ],
    [
        InlineKeyboardButton(text="Самолето - и вертолетостроение",
                             callback_data="Aircraft_and_helicopter_construction_deg_14")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_deg_14")
    ]
])

# Направления 191 ИРЭФ-ЦТ
menu_191iktfiz_degree_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы",
            callback_data="Transmission_degree_systems_iktfiz_14")
    ],
    [
        InlineKeyboardButton(text="Конструирование и технология электронных средств",
                             callback_data="Design_technology_degree_14")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей",
                             callback_data="Intelligent_radio_electronics_deg_14")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_deg_14")
    ]
])

# Направления 191 ИКТЗИ
menu_191iktfiz_degree_button_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Защита информации в компьютерных сетях", callback_data="Information_protection_deg_14")
    ],
    [
        InlineKeyboardButton(text="Информационная безопасность", callback_data="Information_security_deg_14")
    ],
    [
        InlineKeyboardButton(text="Программирование и администрирование компьютерных систем", callback_data="Computer_administration_deg_14")
    ],
    [
      InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="Intelligent_information_systems_deg_14")
    ],
    [
        InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BIGDATA", callback_data="BIGDATA_Management_models_deg_14")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_deg_14")
    ]
])

# Направления 191 ИАЭП
menu_191iktfiz_degree_button_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оптико-электронные системы", callback_data="Optoelectronic_systems_deg_14")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_deg_14")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="Environmental_engineering_deg_14")
    ],
    [
        InlineKeyboardButton(text="Управление беспилотными летательными аппаратами. Интеллектуальные технические системмы. Робототехника", callback_data="Control_of_unmanned_aerial_vehicle_deg_14")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_191_deg_14")
    ]
])

# назад к факультетам
back_deg_191_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_deg_191")
    ]
])
