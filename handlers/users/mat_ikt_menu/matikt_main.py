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

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="Mat")
async def fmf_hi(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                              f"Какая форма обучения тебя интерисует?🕵🏻‍♀️", reply_markup=menu_Form_of_training_button)


@dp.callback_query_handler(text="full_time_training")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>очную</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️")
    await Careitems.item1.set()


@dp.message_handler(content_types=['text'], state=Careitems.item1)
async def item1(message: Message, state: FSMContext):

    # if message.text < '':
    #     await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
    #     await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
    #                          "Вводи только числа, не текст❗️", reply_markup=vibor_button)

    if message.text <= '169':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_169)

    elif message.text <= '177':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_177)

    elif message.text <= '181':
        await message.delete()
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_181)

    elif message.text <= '188':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_188)

    elif message.text <= '189':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_189)

    elif message.text <= '191':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_191)

    elif message.text <= '193':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_193)

    elif message.text <= '194':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_194)

    elif message.text <= '196':
        await message.answer(f'Твои баллы: {message.text}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_196)

    elif message.text <= '199':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_199)

    elif message.text <= '203':
        await message.answer(f"Твои баллы: {message.text}\n"
                             "Ты неплохо постарался\n"
                             "Возможные направления в:", reply_markup=menu_iltfiz_button_203)

    elif message.text <= '206':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_206)

    elif message.text <= '208':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_208)

    elif message.text <= '210':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_210)

    elif message.text <= '211':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_211)

    elif message.text <= '212':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_212)

    elif message.text <= '216':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_216)

    elif message.text <= '218':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_218)

    elif message.text <= '221':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_221)

    elif message.text <= '229':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_229)

    elif message.text <= '233':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_233)

    elif message.text <= '246':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_246)


    elif message.text <= '247':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_247)

    elif message.text <= '249':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_249)

    elif message.text <= '251' or message.text >= '251':
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_iltfiz_button_251)

    # elif message.text > '400':
    #     await message.delete()
    #     await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
    #     await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
    #                          "Вводи только числа, не текст❗️", reply_markup=vibor_button)

    await state.finish()
