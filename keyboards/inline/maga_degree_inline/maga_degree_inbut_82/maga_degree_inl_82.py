from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ИАЭНТЭ направления
menu_maga_degreet_82 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Материаловедение и технология материалов",
                             callback_data="Materials_science_and_technology_of_materials_maga_degree_4")
    ],
    [
        InlineKeyboardButton(text="Конструкторско-технологическое обеспечение машиностроительных производств",
                             callback_data="Design_and_technological_support_maga_degree_4")
    ],
    [
        InlineKeyboardButton(text="Авиастроение", callback_data="Aircraft_construction_maga_degeree_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_82_4")
    ]
])

# ИАЭП направления
menu_maga_degreet_82_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Электроэнергетика и электротехника",
                             callback_data="Electric_power_and_electrical_engineering_maga_degree_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_82_4")
    ]
])

# назад
back_maga_degree_82 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_82")
    ]
])