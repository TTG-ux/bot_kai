from aiogram import types, bot
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import admins

from utils.dp_api import database

from loader import dp
from keyboards.inline.choice_buttons import determined_button
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton,
                           CallbackQuery, LabeledPrice, PreCheckoutQuery)

db = database.DBCommands()


@dp.message_handler(CommandStart())
async def bot_start(m: types.Message):
    chat_id = m.from_user.id
    referral = m.get_args()
    user = await db.add_new_user(referral=referral)
    id = user.id
    count_users = await db.count_users()
    await m.answer(f"Привет, {m.from_user.full_name}!\n"
                   f"Твоему вниманию представлено главное меню🎩\n\n"
                   f"Высшее - Университет КНИТУ-КАИ и его факультеты(бакалвр/специалитет)\n\n"
                   f"Среднее - Колледжи при КНИТУ-КАИ их специальности\n\n"
                   f"В пункте (Часто задаваемые вопросы) ты можешь задать мне вопрос👱‍♀️\n\n"
                   f"Дальнейшие пункты хранят в себя важные ссылки/контакты🗣👀",
                   reply_markup = determined_button)
