from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления  ИРЭФ-ЦТ 128
menu_iktfiz_dis_button_128 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_dis_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_128_dis_4")
    ]
])

# Направления ИАНТЭ 128
menu_iktfiz_dis_button_128_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_dis_4")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_dis_4")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация",
                             callback_data="Road_transport_dis_4")
    ],
    [
        InlineKeyboardButton(text="Обслуживание судов и двигателей, обеспечение безопасности полетов",
                             callback_data="Ship_and_engine_maintenance_dis_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_128_dis_4")
    ]
])

# Направления ИКТЗИ 128
menu_iktfiz_dis_button_128_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_dis_4")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальные информационные системы",
                             callback_data="Intelligent_information_systems_dis_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_128_dis_4")
    ]
])

# назад к факультетам
back_dis_128_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_dic_128_4")
    ]
])
