from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.maga_state.state_ismag import Maga_1

from keyboards.inline.maga_inline_main.midle_maga_inline import menu_maga_button_30, menu_maga_button_33, \
    menu_maga_button_38, \
    menu_maga_button_39, menu_maga_button_40, menu_maga_button_44, menu_maga_button_48, menu_maga_button_54, \
    menu_maga_button_56, \
    menu_maga_button_63, menu_maga_button_65, menu_maga_button_66, menu_maga_button_67, menu_maga_button_68, \
    menu_maga_button_74, \
    menu_maga_button_79, menu_maga_button_80, menu_maga_button_83, menu_maga_button_84, menu_maga_button_89, \
    menu_maga_button_92, menu_maga_button_78

from keyboards.inline.iktfiz.close_input import menu_close
from keyboards.inline.choice_buttons import vibor_button_maga

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Maga_1)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Выбери форму обучения💁‍♀️\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=vibor_button_maga)

    await state.finish()


@dp.callback_query_handler(text="Free_maga")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>Очную</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️\n\n"
                           f"➖➖➖Внимание➖➖➖\n"
                           f"Если твои баллы не целое число, то вводи не через запятую, а через точку❗️", reply_markup=menu_close)
    await Maga_1.m_1.set()


@dp.message_handler(content_types=['text'], state=Maga_1.m_1)
async def item1(message: Message, state: FSMContext):
    if message.text == '30':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_30)

    elif message.text == '100':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/очное в  КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_92)

    elif message.text < '29':
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗\n"
                             "Или же у вас не хватает баллов, минмальный порог 30❗", reply_markup=vibor_button_maga)

    elif '31' >= message.text <= '32':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_30)

    elif '33' <= message.text <= '37':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_33)

    elif message.text == '38':
        await message.delete()
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_38)

    elif message.text == '39':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_39)

    elif message.text == '40':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_40)

    elif '41' <= message.text <= '43':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_40)

    elif '44' <= message.text <= '47':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_44)

    elif message.text == '48':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_48)

    elif '49' <= message.text <= '53':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_48)

    elif '54' <= message.text <= '55':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_54)

    elif '56' <= message.text <= '62':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_56)

    elif '63' <= message.text <= '64':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_63)

    elif message.text == '65':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_maga_button_65)

    elif message.text == '66':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_66)

    elif message.text == '67':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_67)

    elif message.text == '68':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_68)

    elif '69' <= message.text <= '73':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_68)

    elif '74' <= message.text <= '77':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_74)

    elif message.text == '78':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_78)

    elif message.text == '79':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_79)

    elif message.text == '80':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_80)

    elif '81' <= message.text <= '82':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_80)

    elif message.text == '83':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_83)

    elif '84' >= message.text <= '88':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_84)

    elif '89' <= message.text <= '91':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_89)

    elif '92' <= message.text <= '99':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/очное в  КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_maga_button_92)

    else:
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗\n"
                             "Или же у вас не хватает баллов, минмальный порог 30❗", reply_markup=vibor_button_maga)

    await state.finish()
