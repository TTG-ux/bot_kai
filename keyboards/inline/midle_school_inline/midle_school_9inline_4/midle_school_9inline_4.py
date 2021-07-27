from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Выбор классов
menu_midle_buttonsc_45 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Экономика и бухгалтерский учет",
                             callback_data="Economics_and_accounting_ms_4")
    ],
    [
        InlineKeyboardButton(text="Технология металлообрабатывающего производства",
                             callback_data="Technology of metalworking production_ms_4")
    ],
    [
        InlineKeyboardButton(text="Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей",
                             callback_data="Maintenance_and_repair_ms_4")
    ],
    [
        InlineKeyboardButton(text="Управление качеством продукции, процессов и услуг",
                             callback_data="Quality_management_of_products_ms_4")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_45_4")
    ]
])

# назад
back_ms_inline_button_45 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_45")
    ]
])
