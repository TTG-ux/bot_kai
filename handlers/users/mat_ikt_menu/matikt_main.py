from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.state import Careitems

from keyboards.inline.ikt_fiz_inline.ikt_fiziks_b import menu_iltfiz_button_169, \
    menu_iltfiz_button_177, menu_iltfiz_button_181, menu_iltfiz_button_188, menu_iltfiz_button_189, \
    menu_iltfiz_button_191, menu_iltfiz_button_193, menu_iltfiz_button_194, menu_iltfiz_button_196, \
    menu_iltfiz_button_199, menu_iltfiz_button_203, menu_iltfiz_button_206, menu_iltfiz_button_208, \
    menu_iltfiz_button_210, menu_iltfiz_button_211, menu_iltfiz_button_212, menu_iltfiz_button_216, \
    menu_iltfiz_button_218, menu_iltfiz_button_221, menu_iltfiz_button_229, menu_iltfiz_button_233, \
    menu_iltfiz_button_246, menu_iltfiz_button_247, menu_iltfiz_button_249, menu_iltfiz_button_251
from keyboards.inline.choice_buttons import menu_Form_of_training_button, vibor_button
from keyboards.inline.iktfiz.close_input import menu_close

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Careitems)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=menu_Form_of_training_button)

    await state.finish()


@dp.callback_query_handler(text="Mat")
async def fmf_hi(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                              f"Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                              reply_markup=menu_Form_of_training_button)


@dp.callback_query_handler(text="full_time_training")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>очную</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️", reply_markup=menu_close)
    await Careitems.item1.set()


@dp.message_handler(content_types=['text'], state=Careitems.item1)
async def item1(message: Message, state: FSMContext):
    res = message.text

    if res == '169':
        await message.answer(f'Твои баллы: {res}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_169)

    elif '170' <= res <= '176':
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_169)

    elif '177' <= res <= '180':
        await message.delete()
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_177)

    elif '181' <= res <= '187':
        await message.answer(f'Твои баллы: {res}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_181)

    elif res == '188':
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_188)

    elif '189' <= res <= '190':
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_189)

    elif '191' <= res <= '192':
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_191)

    elif res == '193':
        await message.answer(f"Твои баллы: {res}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_193)

    elif '194' <= res <= '195':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_193)

    elif '196' <= res <= '198':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_196)

    elif '198' <= res <= '202':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_198)

    elif '203' <= res <= '205':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_203)

    elif '206' <= res <= '207':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_206)

    elif '208' <= res <= '209':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_208)

    elif res == '210':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_210)

    elif res == '211':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_211)

    elif '212' <= res <= '215':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_212)

    elif '216' <= res <= '217':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_216)

    elif '218' <= res <= '220':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_218)

    elif '221' <= res <= '228':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_221)

    elif '229' <= res <= '232':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_229)

    elif '233' <= res <= '245':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_233)


    elif res == '246':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_246)

    elif '247' <= res <= '248':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_247)

    elif '249' <= res <= '250':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_247)

    elif '251' <= res <= '310':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_251)

    else:
        await message.delete()
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗️\n"
                             "Или у тебя не хватает баллов, минимальный порог 169❗️", reply_markup=vibor_button)

    await state.finish()
