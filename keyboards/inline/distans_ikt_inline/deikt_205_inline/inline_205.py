from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления  ИРЭФ-ЦТ 205
menu_iktfiz_dis_button_205 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_dis_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_205_dis_7")
    ]
])

# Направления ИАНТЭ 205
menu_iktfiz_dis_button_205_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_dis_7")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_dis_7")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация",
                             callback_data="Road_transport_dis_7")
    ],
    [
        InlineKeyboardButton(text="Обслуживание судов и двигателей, обеспечение безопасности полетов",
                             callback_data="Ship_and_engine_maintenance_dis_7")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_dis_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_205_dis_7")
    ]
])

# Направления ИКТЗИ 205
menu_iktfiz_dis_button_205_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_dis_7")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальные информационные системы",
                             callback_data="Intelligent_information_systems_dis_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_205_dis_7")
    ]
])

# Направления ИАЭП 205
menu_iktfiz_dis_button_205_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Стандартизация, сертификация и метрология", callback_data="Standardization_dis_7")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_dis_7")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_205_dis_7")
    ]
])

# назад к факультетам
back_dis_205_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_dic_205_7")
    ]
])
