from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.choice_buttons import determined_button


@dp.message_handler(CommandStart())
async def bot_start(m: types.Message):
    await m.answer(f"Привет, {m.from_user.full_name}!\n"
                   f"Твоему вниманию представлено главное меню🎩\n\n"
                   "Высшее - Университет КНИТУ-КАИ и его факультеты(бакалвр/специалитет)\n\n"
                   "Среднее - Колледжи при КНИТУ-КАИ их специальности\n\n"
                   "В пункте (Часто задаваемые вопросы) ты можешь задать мне вопрос👱‍♀️\n\n"
                   "Дальнейшие пункты хранят в себя важные ссылки/контакты🗣👀\n\n"
                   , reply_markup=determined_button)
