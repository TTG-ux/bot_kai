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

    await m.answer(f"Привет, {m.from_user.full_name}!\n"
                   f"Твоему вниманию представлено <ins><b>Главное меню</b></ins>🎩\n\n"
                   f"<em>Высшее</em> - <b>Университет КНИТУ-КАИ и его факультеты</b> (бакалавр/специалитет)\n\n"
                   f"<em>Среднее</em> - <b>Колледжи при КНИТУ-КАИ их специальности</b>\n\n"
                   f"В пункте (<ins>❓Часто задаваемые вопросы❓</ins>) ты можешь задать мне вопрос👱‍♀️\n\n"
                   f"Дальнейшие пункты хранят в себя важные ссылки/контакты🗣👀",
                   reply_markup=determined_button)
