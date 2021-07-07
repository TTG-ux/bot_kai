from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu_feed_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Написать отзыв🖌")
    ],
    [
        KeyboardButton(text="Назад⬅️")
    ]
],
    resize_keyboard=True
)

menu_reply_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='✅Подтвердить✅')
    ],
    [
        KeyboardButton(text='Исправить❌')
    ]
],
    resize_keyboard=True
)

exit_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="❗️Отмена❗️")
    ]
],
    resize_keyboard=True
)
