from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from aiogram.dispatcher import FSMContext
import logging
from states.state import khemical_1
from keyboards.inline.khem_inline.khrm_buttons import menu_kchem_button_181, menu_kchem_button_206


@dp.callback_query_handler(text="Khemical")
async def khem_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data
    logging.info(f"{callback_data=}")

    await c.message.answer("Вы выбрали:\n\n"
                           "<ins><b>Математика Русский  Химия</b></ins>\n\n"
                           "Введите ваши суммарные баллы ✏️")

    await khemical_1.u_1.set()


@dp.message_handler(content_types=['text'], state=khemical_1.u_1)
async def khem_1(m: Message, state: FSMContext):
    if m.text <= '100':
        await m.answer(f"У тебя слишком маленькие баллы, посмотри пунк в меню\n"
                       f"<b>Платное обучение</b>")

    elif m.text <= '181':
        await m.answer(f"Твои баллы: {m.text}\n"
                       f"Ты неплохо постарался\n"
                       f"Возможные напрваления в:", reply_markup=menu_kchem_button_181)

    if m.text <= '206' or m.text >= '206':
        await m.answer(f"Твои баллы: {m.text}\n"
                       f"Ты неплохо постарался\n"
                       f"Возможные напрваления в:", reply_markup=menu_kchem_button_206)

    await state.finish()