from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_maga_degreet_741 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Материаловедение и технология материалов",
                             callback_data="Materials_science_and_technology_of_materials_maga_degree_2")
    ],
    [
        InlineKeyboardButton(text="Конструкторско-технологическое обеспечение машиностроительных производств",
                             callback_data="Design_and_technological_support_maga_degree_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_741_2")
    ]
])

# назад
back_maga_degree_741 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_maga_degree_741")
    ]
])