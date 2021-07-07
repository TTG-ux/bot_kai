from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu_sosity_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ИИЭиП", callback_data="IIAiP_sosity_1")
    ]
])

sosity_IIAip_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Экономика и управление цифровым предприятием. Инвестиционное проектирование. Промышленная коммерция", callback_data="sosity_Economics_and_Management_1")
    ],
    [
        InlineKeyboardButton(text="Управление проектами. Производственный менеджмент", callback_data="sosity_Project_management_1")
    ],
    [
        InlineKeyboardButton(text="Управление человеческими ресурсами", callback_data="sosity_Resource_management_1")
    ]
])

back_socity_button_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="b_sosity_1")
    ]
])