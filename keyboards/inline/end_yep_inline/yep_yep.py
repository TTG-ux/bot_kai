from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ВШПИТ
menu_theend_yep_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Коммерческая разработа и текхнологическое предпринимательство",
                             callback_data="Commercial_development_end_1")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="bb_end_1")
    ]
])

# ИАНТЭ
menu_theend_yep_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Обслуживание судов и двигателей. Обеспечение безопасности полетов",
                             callback_data="MAINTENANCE_OF_SHIPS_end_1")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="bb_end_1")
    ]
])

# ИАЭП
menu_theend_yep_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Биотехнические и медицинские аппараты и системы",
                             callback_data="Biotechnical_and_medical_devices_end_1")
    ],
    [
        InlineKeyboardButton(text="Инженерная экология. Защита в чрезвычайных ситуациях",
                             callback_data="Environmental_engineering_end_1")
    ],
    [
        InlineKeyboardButton(text="Природоустройство и водопользование",
                             callback_data="Nature_management_end_1")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="bb_end_1")
    ]
])

# ИИЭиП
menu_theend_yep_4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Финансовые технологии",
                             callback_data="FINANCIAL_TECHNOLOGIES_end_1")
    ],
    [
        InlineKeyboardButton(text="Экономика и управление цифровым предприятием. инвестиционное проектирование. Промышленная коммерция",
                             callback_data="ECONOMICS_AND_MANAGEMENT_end_1")
    ],
    [
        InlineKeyboardButton(text="Управление проектами. Производственный менеджмент",
                             callback_data="PROJECT_MANAGEMENT_end_1")
    ],
    [
        InlineKeyboardButton(text="Управление человеческими ресурсами",
                             callback_data="HUMAN_RESOURCE_MANAGEMENT_end_1")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="bb_end_1")
    ]
])

bb_end_yy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",
                             callback_data="bbb_end")
    ]
])