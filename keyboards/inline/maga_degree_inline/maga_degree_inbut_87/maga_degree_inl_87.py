from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ИАЭНТЭ направления
menu_maga_degreet_87 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Материаловедение и технология материалов",
                             callback_data="Materials_science_and_technology_of_materials_maga_degree_5")
    ],
    [
        InlineKeyboardButton(text="Конструкторско-технологическое обеспечение машиностроительных производств",
                             callback_data="Design_and_technological_support_maga_degree_5")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_maga_degeree_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_87_5")
    ]
])

# ИАЭП направления
menu_maga_degreet_87_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Электроэнергетика и электротехника",
                             callback_data="Electric_power_and_electrical_engineering_maga_degree_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_87_5")
    ]
])

# МРЭФ-ЦТ направления
menu_maga_degreet_87_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Радиотехника",
                             callback_data="Radio_engineering_maga_degree_5")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_87_5")
    ]
])

# назад
back_maga_degree_87 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_87")
    ]
])