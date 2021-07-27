from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.distance_state.state_dis import Dis_state

from keyboards.inline.distans_ikt_inline.main_dis_ika import menu_iltfiz_dis_button_121, menu_iltfiz_dis_button_122, \
    menu_iltfiz_dis_button_123, menu_iltfiz_dis_button_128, menu_iltfiz_dis_button_133, menu_iltfiz_dis_button_189, \
    menu_iltfiz_dis_button_205, menu_iltfiz_dis_button_234
from keyboards.inline.choice_buttons import vibor_button, menu_Form_of_training_button
from keyboards.inline.iktfiz.close_input import menu_close

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Dis_state)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=menu_Form_of_training_button)

    await state.finish()


@dp.callback_query_handler(text="Distance_learning")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>заочную</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️", reply_markup=menu_close)
    await Dis_state.d_1.set()


@dp.message_handler(content_types=['text'], state=Dis_state.d_1)
async def item1(message: Message, state: FSMContext):

    if message.text == '121':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_121)

    elif message.text == '122':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_dis_button_122)

    elif message.text == '123':
        await message.delete()
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_dis_button_123)

    elif '124' <= message.text <= '127':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_123)

    elif '128' <= message.text <= '132':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_128)

    elif '133' <= message.text <= '188':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_133)

    elif '189' <= message.text <= '204':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_189)

    elif '205' <= message.text <= '233':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_205)

    elif '234' <= message.text <= '310':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления бакл/заоч в КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_dis_button_234)

    else:
        await message.delete()
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗️", reply_markup=vibor_button)

    await state.finish()
