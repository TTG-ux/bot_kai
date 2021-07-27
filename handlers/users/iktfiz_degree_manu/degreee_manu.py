from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.degree_states.degree_main_state import Degree_1

from keyboards.inline.degree_inline.main_degree_inbut import menu_iltfiz_degree_button_145, \
    menu_iltfiz_degree_button_150, \
    menu_iltfiz_degree_button_159, menu_iltfiz_degree_button_165, menu_iltfiz_degree_button_171, \
    menu_iltfiz_degree_button_166, \
    menu_iltfiz_degree_button_168, menu_iltfiz_degree_button_177, menu_iltfiz_degree_button_179, \
    menu_iltfiz_degree_button_176, \
    menu_iltfiz_degree_button_183, menu_iltfiz_degree_button_187, menu_iltfiz_degree_button_190, \
    menu_iltfiz_degree_button_191, \
    menu_iltfiz_degree_button_195, menu_iltfiz_degree_button_200, menu_iltfiz_degree_button_211, \
    menu_iltfiz_degree_button_202, \
    menu_iltfiz_degree_button_205, menu_iltfiz_degree_button_207, menu_iltfiz_degree_button_249
from keyboards.inline.choice_buttons import vibor_button, menu_Form_of_training_button
from keyboards.inline.iktfiz.close_input import menu_close

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Degree_1)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=menu_Form_of_training_button)

    await state.finish()


@dp.callback_query_handler(text="Targeted_training")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>целевую</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️", reply_markup=menu_close)
    await Degree_1.deg_1.set()


@dp.message_handler(content_types=['text'], state=Degree_1.deg_1)
async def item1(message: Message, state: FSMContext):

    if message.text == '145':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_145)

    elif '146' <= message.text <= '149':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_145)

    elif '150' <= message.text <= '158':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_150)

    elif '159' <= message.text <= '164':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_159)

    elif message.text == '165':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_165)

    elif '166' <= message.text <= '167':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_166)

    elif '168' <= message.text <= '170':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_168)

    elif '171' <= message.text <= '175':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_171)

    elif message.text == '176':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_176)

    elif '177' <= message.text <= '178':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_177)

    elif '179' <= message.text <= '182':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_179)

    elif '183' <= message.text <= '186':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_183)

    elif '187' <= message.text <= '189':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_187)

    elif message.text == '190':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_190)

    elif '191' <= message.text <= '194':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_191)

    elif '195' <= message.text <= '199':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_195)

    elif '200' <= message.text <= '201':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_200)

    elif '202' <= message.text <= '204':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_202)

    elif '205' <= message.text <= '206':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_205)

    elif '207' <= message.text <= '210':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_207)

    elif '211' <= message.text <= '248':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_211)

    elif '249' <= message.text <= '310':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления по бакл/цел в КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_249)

    else:
        await message.delete()
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗️\n"
                             "Или у вас не хватает баллов, минимальный порог 145❗️", reply_markup=vibor_button)

    await state.finish()
