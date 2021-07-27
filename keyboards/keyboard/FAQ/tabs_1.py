from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu_FAQ = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="📝Написать свой вопрос📝")
    ],
    [
        KeyboardButton(text="🏛Главное меню🏛")
    ]
],
    resize_keyboard=True
)

menu_FAQ_cancel = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="❌ОТМЕНИТЬ❌")
    ]
],
    resize_keyboard=True
)

menu_FAQ_vibor = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🤞Отправить🤞")
    ],
    [
        KeyboardButton(text="🤦‍♀️Исправить🤦‍♀️")
    ],
    [
        KeyboardButton(text="🏛Главное меню🏛")
    ]

],
    resize_keyboard=True
)
