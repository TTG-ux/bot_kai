from aiogram import types, bot
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
from keyboards.inline.choice_buttons import determined_button


@dp.message_handler(CommandStart())
async def bot_start(m: types.Message):
    if (not db.subscriber_exists(m.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(m.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(m.from_user.id, True)

    await m.answer_sticker(r'CAACAgEAAxkBAAEHmQFg4-i3Czzdi5T7zV7589t-R8KO1wACTwkAAr-MkAT3aSKIYCtSqiAE')
    await m.answer(f"Привет, {m.from_user.full_name}!\n"
                   f"Я помогу тебе:\n\n"
                   f"📍 <ins><em>Определиться</em></ins> с выбором <em><b>факультета и направлением</b></em> 👀\n"
                   f"📍 <ins><em>Отвечу</em></ins> на твои <em>вопросы</em> ❗️\n"
                   f"📍 <ins><em>Покажу</em></ins> все <b>контакты</b> <em>колл центра</em> и <em>важные ссылки</em> 👌\n\n"  
                   f"Для того чтобы открыть главное меню нажми или введи 👉 /menu",)

