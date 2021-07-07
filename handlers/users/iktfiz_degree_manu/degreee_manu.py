from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.degree_states.degree_main_state import Degree_1

from keyboards.inline.degree_inline.main_degree_inbut import menu_iltfiz_degree_button_145, menu_iltfiz_degree_button_150,\
    menu_iltfiz_degree_button_159, menu_iltfiz_degree_button_165, menu_iltfiz_degree_button_171, menu_iltfiz_degree_button_166,\
    menu_iltfiz_degree_button_168, menu_iltfiz_degree_button_177, menu_iltfiz_degree_button_179, menu_iltfiz_degree_button_176,\
    menu_iltfiz_degree_button_183, menu_iltfiz_degree_button_187, menu_iltfiz_degree_button_190, menu_iltfiz_degree_button_191,\
    menu_iltfiz_degree_button_195, menu_iltfiz_degree_button_200, menu_iltfiz_degree_button_211, menu_iltfiz_degree_button_202,\
    menu_iltfiz_degree_button_205, menu_iltfiz_degree_button_207, menu_iltfiz_degree_button_249

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="Targeted_training")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>целевую</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️")
    await Degree_1.deg_1.set()


@dp.message_handler(content_types=['text'], state=Degree_1.deg_1)
async def item1(message: Message, state: FSMContext):
    if message.text <= '145':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_145)

    elif message.text <= '150':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_150)

    elif message.text <= '159':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_159)

    elif message.text <= '165':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_165)

    elif message.text <= '166':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_166)

    elif message.text <= '168':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_168)

    elif message.text <= '171':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_171)

    elif message.text <= '176':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_176)

    elif message.text <= '177':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_177)

    elif message.text <= '179':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_179)

    elif message.text <= '183':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_degree_button_183)

    elif message.text <= '187':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_187)

    elif message.text <= '190':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_190)

    elif message.text <= '191':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_191)

    elif message.text <= '195':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_195)

    elif message.text <= '200':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_200)

    elif message.text <= '202':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_202)

    elif message.text <= '205':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_205)

    elif message.text <= '207':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_207)

    elif message.text <= '211':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_211)

    elif message.text <= '249' or message.text >= '249':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_degree_button_249)


    await state.finish()
