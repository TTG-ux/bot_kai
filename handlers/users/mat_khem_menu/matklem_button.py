from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from aiogram.dispatcher import FSMContext
import logging
from states.state import khemical_1
from keyboards.inline.khem_inline.khem_buttons import menu_kchem_button_181, menu_kchem_button_206
from keyboards.inline.iktfiz.close_input import menu_close
from keyboards.inline.choice_buttons import vibor_button


@dp.callback_query_handler(text="close_ikt", state=khemical_1)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Выберите предметы ЕГЭ\n\n"
                           "✅✅✅✅✅✅✅✅✅✅\n\n"
                           "<ins><strong>C 2021 года</strong></ins>\n"
                           "При поступлении с <b><em>ИКТ</em></b> ты можешь <ins><b>подать заявление</b></ins> на факультеты в которых поступают с предметом:<b><em>Физ</em></b>\n\n"
                           "✅✅✅✅✅✅✅✅✅✅", reply_markup=vibor_button)

    await state.finish()


@dp.callback_query_handler(text="Khemical")
async def khem_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data
    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали:\n\n"
                           "<ins><b>Математика Русский  Химия</b></ins>\n\n"
                           "Введите ваши суммарные баллы ✏️", reply_markup=menu_close)

    await khemical_1.u_1.set()


@dp.message_handler(content_types=['text'], state=khemical_1.u_1)
async def khem_1(m: Message, state: FSMContext):

    if m.text == '181':
        await m.answer(f"Твои баллы: {m.text}\n"
                       f"Ты неплохо постарался\n"
                       f"Возможные напрваления в:", reply_markup=menu_kchem_button_181)

    elif '182' <= m.text <= '205':
        await m.answer(f"Твои баллы: {m.text}\n"
                       f"Ты неплохо постарался\n"
                       f"Возможные напрваления в:", reply_markup=menu_kchem_button_181)

    elif '206' <= m.text <= '310':
        await m.answer(f"Твои баллы: {m.text}\n"
                       f"Ты неплохо постарался\n"
                       f"Возможные напрваления в:", reply_markup=menu_kchem_button_206)

    else:
        await m.delete()
        await m.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await m.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                       "Вводи только числа, не текст❗️\n"
                       "Или у тебя не хватает баллов, минимальный порог 181❗️", reply_markup=vibor_button)

    await state.finish()
