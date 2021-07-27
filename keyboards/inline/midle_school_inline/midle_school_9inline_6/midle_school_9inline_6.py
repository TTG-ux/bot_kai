from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ТК
menu_midle_buttonsc_485 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Экономика и бухгалтерский учет",
                             callback_data="Economics_and_accounting_ms_6")
    ],
    [
        InlineKeyboardButton(text="Технология металлообрабатывающего производства",
                             callback_data="Technology of metalworking production_ms_6")
    ],
    [
        InlineKeyboardButton(text="Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей",
                             callback_data="Maintenance_and_repair_ms_6")
    ],
    [
        InlineKeyboardButton(text="Управление качеством продукции, процессов и услуг",
                             callback_data="Quality_management_of_products_ms_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_485_6")
    ]
])

# Кит
menu_midle_buttonsc_485_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Сетевое и системное администрирование",
                             callback_data="Network_and_system_administration_ms_6")
    ],
    [
        InlineKeyboardButton(text="Обеспечение информационной безопасности автоматизированных систем",
                             callback_data="Ensuring_information_security_ms_6")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_485_6")
    ]
])

# назад
back_ms_inline_button_485 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_ms_485")
    ]
])
