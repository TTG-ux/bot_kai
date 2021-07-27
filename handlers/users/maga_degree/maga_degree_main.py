from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.maga_state.state_maga_degree import Maga_3

from keyboards.inline.maga_degree_inline.maga_degee_main_inbut import menu_maga_degree_62, menu_maga_degree_82, \
    menu_maga_degree_87, \
    menu_maga_degree_741, menu_maga_degree_742

from keyboards.inline.choice_buttons import vibor_button_maga
from keyboards.inline.iktfiz.close_input import menu_close

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Maga_3)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Выбери форму обучения💁‍♀️\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=vibor_button_maga)

    await state.finish()


@dp.callback_query_handler(text="high_maga")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>Целевую</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️\n\n"
                           "➖➖➖Внимание➖➖➖\n"
                           "Вводи свои средние баллы через <em><b>ТОЧКУ</b></em> и до <b><em>ТЫСЯЧНЫХ</em></b>\n\n"
                           "Пример -> ✅4.000 ✅5.000 ✅3.345\n"
                           "❌3 ❌3.5 ❌4.25", reply_markup=menu_close)
    await Maga_3.m3_1.set()


@dp.message_handler(content_types=['text'], state=Maga_3.m3_1)
async def item1(message: Message, state: FSMContext):
    if message.text == '62.100':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_62)

    elif message.text == '100.000':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/цел в  КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_87)

    elif '62.200' <= message.text <= '74.149':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_62)

    elif '74.150' <= message.text <= '74.159':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_741)

    elif '74.160' <= message.text <= '74.599':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_741)

    elif '74.600' <= message.text <= '81.999':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_742)

    elif '82.000' <= message.text <= '87.499':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_82)

    elif '87.500' <= message.text <= '99.999':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/цел в  КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_maga_degree_87)

    else:
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗\n"
                             "Или же у вас не хватает баллов, минмальный порог 30❗", reply_markup=vibor_button_maga)

    await state.finish()
