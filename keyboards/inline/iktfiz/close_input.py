from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_close = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="❌Отменить❌", callback_data="close_ikt")
    ]
])