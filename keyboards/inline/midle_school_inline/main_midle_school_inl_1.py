from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Выбор классов
menu_midle_button_school = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="9 класс",
                             callback_data="9_class_but")
    ],
    [
        InlineKeyboardButton(text="11 класс", callback_data="11_class_but")
    ]
])

# Образовательные программы 9 классов

menu_midle_school_vibor_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_1")
    ]
])

menu_midle_school_vibor_431 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_2")
    ]
])

menu_midle_school_vibor_435 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_3")
    ]
])

menu_midle_school_vibor_45 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_4")
    ]
])

menu_midle_school_vibor_48 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_5")
    ],
    [
        InlineKeyboardButton(text="КИТ", callback_data="KIT_5")
    ]
])

menu_midle_school_vibor_485 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_6")
    ],
    [
        InlineKeyboardButton(text="КИТ", callback_data="KIT_6")
    ]
])

menu_midle_school_vibor_4952 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ТК", callback_data="TK_7")
    ],
    [
        InlineKeyboardButton(text="КИТ", callback_data="KIT_7")
    ]
])

menu_vibor_sr_school = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Управление качеством продукции, процессов и услуг", callback_data="TK_ms_1")
    ],
    [
        InlineKeyboardButton(text="Экономика и бухгалтерский учет", callback_data="TK_ms_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_vibor_sr")
    ]
])

back_vibor_srr = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="b_but")
    ]
])
