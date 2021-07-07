from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu_adm_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="✅Рассылка✅")
    ],
    [
        KeyboardButton(text="❌Отмена❌")
    ]
],
    resize_keyboard=True
)