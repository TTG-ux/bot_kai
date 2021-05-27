import logging
from asyncio import sleep
from aiogram import Dispatcher, types
from states.state import Mailing
from data.config import admins
from loader import dp
from utils.dp_api.database import User
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)


@dp.message_handler(user_id=admins, commands=["tell_everyone"])
async def mailing(message: types.Message):
    await message.answer("Пришлите текст рассылки")
    await Mailing.Text.set()


@dp.message_handler(user_id=admins, state=Mailing.Text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    markup = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [InlineKeyboardButton(text="Русский", callback_data="ru")]
        ]
    )
    await message.answer(("Пользователям на каком языке разослать это сообщение?\n\n"
                          "Текст:\n"
                          "{text}").format(text=text),
                         reply_markup=markup)
    await Mailing.LVL1.set()


@dp.callback_query_handler(user_id=admins, state=Mailing.LVL1)
async def mailing_start(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    await state.reset_state()
    await call.message.edit_reply_markup()

    users = await User.query.where(User.full_name == call.data).gino.all()
    for user in users:
        try:
            await bot.send_message(chat_id=user.user_id,
                                   text=text)
            await sleep(0.3)
        except Exception:
            pass
    await call.message.answer("Рассылка выполнена.")
