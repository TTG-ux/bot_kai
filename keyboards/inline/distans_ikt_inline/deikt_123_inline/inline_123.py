from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления  ИРЭФ-ЦТ 123
menu_iktfiz_dis_button_123 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_dis_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_123_dis_3")
    ]
])

# Направления ИАНТЭ 123
menu_iktfiz_dis_button_123_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_dis_3")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_dis_3")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация",
                             callback_data="Road_transport_dis_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_123_dis_3")
    ]
])

# Направления ИКТЗИ 123
menu_iktfiz_dis_button_123_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_dis_3")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="Intelligent_information_systems_dis_3")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_123_dis_3")
    ]
])

# назад к факультетам
back_dis_123_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_dic_123_3")
    ]
])

