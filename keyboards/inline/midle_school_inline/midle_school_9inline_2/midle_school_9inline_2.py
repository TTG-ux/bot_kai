from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Выбор классов
menu_midle_buttonsc_43 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Экономика и бухгалтерский учет",
                             callback_data="Economics_and_accounting_ms_2")
    ],
    [
        InlineKeyboardButton(text="Технология металлообрабатывающего производства",
                             callback_data="Technology of metalworking production_ms_2")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_33_2")
    ]
])

# назад
back_ms_inline_button_33 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_33")
    ]
])
