from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.inline.Fidback_inline.button_fid import menu_feed_button, menu_reply_button, exit_button
from keyboards.inline.choice_buttons import determined_button
from aiogram.dispatcher import FSMContext
from states.feed_state.feed_b_state import feed_back_b


@dp.message_handler(Text(equals=['Оставить отзыв🖍']))
async def feed_b(m: Message):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmphg5GCNMNtE-EjadXMd6KtJSY3XBQACbQkAAr-MkAQgBEK1gxDuvSAE')
    await m.answer(f"Для того чтобы оставить отзыв, нажми на кнопку 👉 <b>Написать отзыв</b>🖌\n"
                   f"Чтобы просмотреть отзывы перейди по ссылке", reply_markup=menu_feed_button)
    await m.answer(f"<a href='https://t.me/joinchat/kI3mZ8s2f15jOWQ6'> Ссылка </a>")


@dp.message_handler(Text(equals=['Назад⬅️']))
async def feed_backi(m: Message):
    await m.delete()
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmr5g5GdaUfc_nrwFkfT0lIrQC97yKgACcgkAAr-MkAQvBrlOwuVncCAE')
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)


@dp.message_handler(Text(equals=['✅Подтвердить✅']), state=feed_back_b)
async def confirm(m: Message, state: FSMContext):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmypg5Hvr8TQcvapNYFl14UWTW3qdIAACZQkAAr-MkASUq_kdsVeamCAE')
    await m.answer(f"🥰Ваш отзыв отправлен, в течении недели я его опублиую в нашем чате🥰\n")
    await bot.send_message(chat_id=-1001520180765, text=f"Отзыв пользователя чат-ботом Alina\n\n"
                                                    f"<em><b>id</b></em> - {m.from_user.id}\n"
                                                    f"<em><b>Имя</b></em> - {name}\n"
                                                    f"<em><b>Отзыв</b></em> - {tixt}\n"
                                                    f"------------------------------")
    await state.finish()


@dp.message_handler(Text(equals=['❗️Отмена❗️']), state=feed_back_b)
async def exit_log(m: Message, state: FSMContext):
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)
    await state.finish()


@dp.message_handler(Text(equals=['Исправить❌']), state=feed_back_b)
async def cansel_log(m: Message):
    await m.answer(f"Напиши своё имя", reply_markup=exit_button)
    await feed_back_b.f_1.set()


# Рег комента
@dp.message_handler(Text(equals=['Написать отзыв🖌']))
async def fed_deed(m: Message):
    await m.answer(f"Напиши своё имя", reply_markup=exit_button)
    await feed_back_b.f_1.set()


@dp.message_handler(state=feed_back_b.f_1)
async def fed_1(m: Message):
    global name
    name = m.text
    await m.answer(f"Напишите отзыв\n\n"
                   f"---ВНИМАНИЕ---\n"
                   f"Пишите одним предложением")
    await feed_back_b.f_2.set()


@dp.message_handler(state=feed_back_b.f_2)
async def feed_2(m: Message):
    global tixt
    tixt = m.text
    await m.answer(f"Ваш отзыв:\n\n"
                   f"<em>Имя</em> - {name}\n"
                   f"<em>Отзыв</em> - {tixt}\n\n"
                   f"Если данные не верны, то нажмите <b>Исправить</b>❌", reply_markup=menu_reply_button)
