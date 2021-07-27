from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления  ИРЭФ-ЦТ 122
menu_iktfiz_dis_button_122 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_dis_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_122_dis_2")
    ]
])

# Направления ИАНТЭ 122
menu_iktfiz_dis_button_122_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_dis_2")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_dis_2")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация",
                             callback_data="Road_transport_dis_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_122_dis_2")
    ]
])

# Направления ИКТЗИ 122
menu_iktfiz_dis_button_122_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_dis_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_122_dis_2")
    ]
])

# назад к факультетам
back_dis_122_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_dic_122_2")
    ]
])

