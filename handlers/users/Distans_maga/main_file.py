from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp
from states.maga_state.state_maga_dist import Maga_2

from keyboards.inline.Dist_maga_inline.main_inline import menu_dis_maga_80, menu_dis_maga_89, menu_dis_maga_96

from keyboards.inline.choice_buttons import vibor_button_maga
from keyboards.inline.iktfiz.close_input import menu_close

from aiogram.dispatcher import FSMContext
import logging


@dp.callback_query_handler(text="close_ikt", state=Maga_2)
async def cl_ikt(c: CallbackQuery, state: FSMContext):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <em><b>математика русский физика или информатика</b></em>\n"
                           "Какая форма обучения тебя интерисует?🕵🏻‍♀️",
                           reply_markup=vibor_button_maga)

    await state.finish()


@dp.callback_query_handler(text="night_maga")
async def full_time(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b>Заочную</b> форму обучения\n"
                           f"Введи свои суммарные баллы ✏️\n\n"
                           f"➖➖➖Внимание➖➖➖\n"
                           f"Если твои баллы не целое число, то вводи не через запятую, а через точку❗️", reply_markup=menu_close)
    await Maga_2.m2_1.set()


@dp.message_handler(content_types=['text'], state=Maga_2.m2_1)
async def item1(message: Message, state: FSMContext):
    res = message.text

    if res == '80':
        await message.answer(f'Твои баллы: {res}\n'
                             'Ты неплохо постарался\n'
                             'Возможные направления в:', reply_markup=menu_dis_maga_80)

    elif '80' <= res <= '88':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_dis_maga_80)

    elif '89' <= res <= '95':
        await message.answer(f'Твои баллы: 👀 <b><em>{message.text}</em></b> 👀\n'
                             'Красавчик/ица😎\n'
                             'Возможные направления в:', reply_markup=menu_dis_maga_89)

    elif '96' <= res <= '99':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/заочное в  КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_dis_maga_96)

    elif res == '100':
        await message.answer_sticker(r'CAACAgEAAxkBAAEHszBg7y6SnaZxZVMLwgABXBptGSRU61oAAmwJAAK_jJAE9YU2ZdlIbSEgBA')
        await message.answer(f'Твои баллы: ⚡️<em><b>{message.text}</b></em>⚡️\n'
                             '🔥🔥Вау, ты можешь просмотреть все факультеты и направления мага/заочное в КАИ️💋🔥🔥\n'
                             'Возможные направления в:', reply_markup=menu_dis_maga_96)

    else:
        await message.delete()
        await message.answer_sticker(r'CAACAgIAAxkBAAEHnTVg5XCoEBbZZYySgIATT1iPbf1mmAACwF8AAulVBRhfrj9Y75JYGyAE')
        await message.answer("⛔️Введено некорректное сообщение⛔️\n\n"
                             "Вводи только числа, не текст❗️\n"
                             "Или у тебя не хватает баллов, минимальный порог 80❗️", reply_markup=vibor_button_maga)

    await state.finish()
