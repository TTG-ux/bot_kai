import logging
from data.config import admins
from asyncio import sleep
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from states.state import Mailing, Careitems, Careitems_1, text_one, test
from aiogram.dispatcher import FSMContext

from states.feed_state.feed_b_state import feed_back_b
from keyboards.inline.Fidback_inline.button_fid import menu_feed_button, menu_reply_button, exit_button

from keyboards.inline.inline_adm.panel_adm import menu_adm_button
from keyboards.inline.cansel_posting.cansel_post import menu_cans_post_1

from keyboards.keyboard.FAQ.tabs_1 import menu_FAQ, menu_FAQ_cancel, menu_FAQ_vibor

from keyboards.inline.midle_school_inline.main_midle_school_inl_1 import menu_midle_button_school

from keyboards.inline.choice_buttons import vibor_button, determined_button, menu_univer_button, \
    back_button232IKT, Informat_IRET4_button, IKit_la4, boom_kar, ViborOBS_button, Obsagha_button1, IIaiP_button1, \
    back_button140OBS, Obsagha_button1_angl, ViborOBS_button_angl, IIaiP_button1_angl, back_button140OBS_angl, temi_1, \
    back_buttonplatkair, platka_iret1, platka_iktziii, baaip_platka, programm_spo4_button, \
    back_spo_kit, kit_button, programm_spo4tk_button, back_spo_tk, colledge_button, tk_slo_button, vibor_button_maga, \
    menu_one_300, menu_theend
from keyboards.inline.Fidback_inline.button_fid import menu_feed_button
from loader import dp, db, bot

import datetime

now_day = datetime.datetime.now()


# Оставить отзыв
@dp.message_handler(Text(equals=['⚡️Оставить отзыв🖍']))
async def feed_b(m: Message):
    await m.delete()
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmphg5GCNMNtE-EjadXMd6KtJSY3XBQACbQkAAr-MkAQgBEK1gxDuvSAE')
    await m.answer(f"Для того чтобы оставить отзыв, нажми на кнопку 👉 <b>Написать отзыв</b>🖌\n"
                   f"Чтобы просмотреть отзывы перейди по ссылке", reply_markup=menu_feed_button)
    await m.answer(f"<a href='https://t.me/joinchat/kI3mZ8s2f15jOWQ6'> Ссылка </a>")

    await feed_back_b.f_1.set()


@dp.message_handler(Text(equals=['Назад⬅️']), state=feed_back_b)
async def feed_backi(m: Message, state: FSMContext):
    await m.delete()
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmr5g5GdaUfc_nrwFkfT0lIrQC97yKgACcgkAAr-MkAQvBrlOwuVncCAE')
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)

    await state.finish()


@dp.message_handler(Text(equals=['✅Подтвердить✅']), state=feed_back_b)
async def confirm(m: Message, state: FSMContext):
    await m.delete()
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmypg5Hvr8TQcvapNYFl14UWTW3qdIAACZQkAAr-MkASUq_kdsVeamCAE')
    await m.answer(f"🥰Ваш отзыв отправлен, в течении недели я его опублиую в нашем чате🥰\n",
                   reply_markup=determined_button)
    await bot.send_message(chat_id=-1001520180765, text=f"Отзыв пользователя чат-ботом Alina\n\n"
                                                        f"<em><b>link</b></em> - @{m.from_user.username}\n"
                                                        f"<em><b>Имя</b></em> - {name}\n"
                                                        f"<em><b>Отзыв</b></em> - {tixt}\n"
                                                        f"------------------------------")
    await bot.send_message(chat_id=-1001520180765, text=f"👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n\n"
                                                        f"Отзыв пользователя чат-ботом Alina\n\n"
                                                        f"<em><b>link</b></em> - @{m.from_user.username}\n"
                                                        f"<em>ID</em> - {m.from_user.id}\n"
                                                        f"------------------------------")

    await state.finish()


@dp.message_handler(Text(equals=['❗️Отмена❗️']), state=feed_back_b)
async def exit_log(m: Message, state: FSMContext):
    await m.delete()
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)
    await state.finish()


@dp.message_handler(Text(equals=['Исправить❌']), state=feed_back_b)
async def cansel_log(m: Message):
    await m.answer(f"Напиши своё имя", reply_markup=exit_button)
    await feed_back_b.f_2.set()


# Рег комента
@dp.message_handler(Text(equals=['Написать отзыв🖌']), state=feed_back_b.f_1)
async def fed_deed(m: Message):
    await m.delete()
    await m.answer_sticker(r'CAACAgEAAxkBAAEHsypg7yxdgyOlyd_cQe6NElZ6-rtrFgAC7wcAAuN4BAABkebeWD0vAbogBA')
    await m.answer(f"Напиши своё имя", reply_markup=exit_button)
    await feed_back_b.f_2.set()


@dp.message_handler(state=feed_back_b.f_2)
async def fed_1(m: Message):
    await m.delete()
    global name
    name = m.text
    await m.answer(f"Напишите отзыв\n\n"
                   f"➖➖➖Внимание➖➖➖\n"
                   f"Пишите одним предложением")
    await feed_back_b.f_3.set()


@dp.message_handler(state=feed_back_b.f_3)
async def feed_2(m: Message):
    await m.delete()
    global tixt
    tixt = m.text
    await m.answer(f"Ваш отзыв:\n\n"
                   f"<em>Имя</em> - {name}\n"
                   f"<em>Отзыв</em> - {tixt}\n\n"
                   f"Если данные не верны, то нажмите <b>Исправить</b>❌", reply_markup=menu_reply_button)


# test
@dp.message_handler(commands=['testi'])
async def menu0_1(m: Message):
    await m.delete()
    await m.answer('CAACAgEAAxkBAAEHmo9g5F3pQxdcA-dzGSyMlem_GQ7IVQACUAkAAr-MkARUHxoRiaqBRyAE')
    await test.t_1.set()
    await m.delete()


@dp.message_handler(state=test.t_1)
async def cl_12(m: Message, state: FSMContext):
    await m.answer('кс')
    tt = m.text
    await m.answer(f"{tt}")
    await state.finish()


# Гл меню
@dp.message_handler(commands=['menu'])
async def menu0_1(m: Message):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmo9g5F3pQxdcA-dzGSyMlem_GQ7IVQACUAkAAr-MkARUHxoRiaqBRyAE')
    await m.answer("🏛Главное меню🏛\n"
                   "<ins><b>Это главное меню</b></ins>\n\n\n"
                   "▫️ «🔷 <b>Поступление</b>☑️» - Информация о факультетах и направлениях Вуза\n\n"
                   "▫️ «❓<b>Часто задаваемые вопросы</b>❓» - Возможность задать мне вопрос\n\n"
                   "▫️ «❗<b>Все важные ссылки</b>❗» - Хранятся все важные ссылки\n\n"
                   "▫️ «🚀<b>Платное обучение</b>🚀» - Информация об платном обучение\n\n"
                   "▫️ «👉 <b>Без баллов ЕГЭ</b> 👈» - Информация о новый Факультетах/направлениях\n\n"
                   "▫️ «<b>Оставить отзыв</b>🖍» - Здесь ты можешь оставить свой отзыв🥺",
                   reply_markup=determined_button)


@dp.message_handler(Text(equals=['🏛Главное меню🏛']))
async def main_manu(m: Message):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmqJg5GI3SrfZlXjP-vyLTDOUxsy_GAACcAkAAr-MkATlCLRcwrvl-SAE')
    await m.answer("🏛Главное меню🏛", reply_markup=determined_button)


# Без баллов ЕГЭ
@dp.message_handler(Text(equals=['👉 Без баллов ЕГЭ 👈']))
async def no_set(m: Message):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHxWFg9xSDtHwG53u-fcqS94kMXRKkeAACTQkAAr-MkATr0aj0SUfsPyAE')
    await m.answer(
        "<em><b>Здесь находится информация о факультетах и их направленияx, <ins>которые не набрали в прошлом году определённое количество человек "
        "для определения ср.бала ЕГЭ или появились новые Факультеты/направления</ins></b></em>",
        reply_markup=menu_theend)


# Отмена рассылки

@dp.message_handler(Text(equals=['❌Отмена❌']), state=Mailing)
async def cans_1(m: Message, state: FSMContext):
    await m.answer(f"Отменила рассылку", reply_markup=determined_button)
    await state.finish()


# confirm
@dp.message_handler(Text(equals=['✅Рассылка✅']), state=Mailing)
async def prime(m: Message, state: FSMContext):
    if text_adm:
        subscriptions = db.get_subscriptions()

        for s in subscriptions:
            await bot.send_message(s[1], text=text_adm)

    await m.answer("Рассылка выполнена!", reply_markup=determined_button)
    await state.finish()


# Рассылка
@dp.message_handler(user_id=admins, commands=['tell_all'])
async def push(m: Message):
    await m.answer(f"Введи текст рассылки", reply_markup=menu_cans_post_1)
    await Mailing.Text.set()


@dp.message_handler(user_id=admins, state=Mailing.Text)
async def pushing(m: Message, state: FSMContext):
    global text_adm
    text_adm = m.text
    await m.answer(f"Выберите", reply_markup=menu_adm_button)


# help
@dp.message_handler(Command("help"))
async def help_1(m: Message):
    await m.answer(text="❗️❗️❗️❗️❗️<b><em>Внимание</em></b>❗️❗️❗️❗️❗️\n"
                        "Все ниже приведенные пункты находяться по вызову команды /menu\n\n\n"
                        "▪️ Все <ins>ссылки</ins>  \n   👇  \n«❗️<b>Все важные ссылки</b>❗️»\n\n"
                        "▪️ Все <ins>контакты</ins>  \n     👇  \n«☎️<b>Контакты</b>☎️»\n\n"
                        "▪️ Информация по поводу <ins>факультетов и направлений</ins>  \n   👇  \n«🔷 <b>Поступление</b>☑️»\n\n"
                        "▪️ Информация по поводу <ins>платного обучения</ins>  \n   👇  \n«🚀<b>Платное обучение</b>🚀»\n\n"
                        "▪️ <ins>Просмотреть новые Факультеты/направления</ins>  \n   👇  \n«👉 <b>Без баллов ЕГЭ</b> 👈»\n\n"
                        "▪️ Оставь свой отзыв можно здесь  \n   👇  \n«<b>⚡️Оставить отзыв</b>🖍»")


# midle-scool
@dp.message_handler(Text(equals=["🔹 Среднее профессиональное образование"]))
async def get_midle(message: Message):
    await message.answer(f"Выбери после какого класса поступаешь🏅", reply_markup=menu_midle_button_school)


@dp.message_handler(Text(equals=['🔷 Поступление☑️']))
async def get_vibor_univer(m: Message):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmqBg5GFX4nc2D3x7YJeCwpKBT5KSJQACWwkAAr-MkAQsaI3Hls79fCAE')
    await m.answer("Куда ты хочешь поступить?🧖‍♀️", reply_markup=menu_univer_button)


# high-scool
@dp.message_handler(Text(equals=["🔹 Бакалавриат"]))
async def get_classic(message: Message):
    await message.answer(f"Выберите предметы ЕГЭ\n\n"
                         f"✅✅✅✅✅✅✅✅✅✅\n\n"
                         "<ins><strong>C 2021 года</strong></ins>\n"
                         "При поступлении с <b><em>ИКТ</em></b> ты можешь <ins><b>подать заявление</b></ins> на факультеты в которых поступают с предметом:<b><em>Физ</em></b>\n\n"
                         "✅✅✅✅✅✅✅✅✅✅", reply_markup=vibor_button)


# Maga high-scool
@dp.message_handler(Text(equals=["🔹 Магистратура"]))
async def get_maga(message: Message):
    await message.answer(f"Выбери форму обучения💁‍♀️\n\n"
                         f"Какая форма обучения тебя интерисует?🕵🏻‍♀️", reply_markup=vibor_button_maga)


# paid-training
@dp.message_handler(Text(equals=["🚀Платное обучение🚀"]))
async def get_classicioooc(message: Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEHmtdg5GitW484G1cXwdpmVJoRs5I2mgACewYAAkb7rATgeh7nHSg28yAE')
    await message.answer("➖➖➖<b><em>Факультеты КАИ <ins>бак/мага</ins> </em></b>➖➖➖\n\n"
                         "🪔<em>ИАНТЭ <b>ср.цена</b></em> = <ins>165 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>ИAЭП <b>ср.цена</b></em> = <ins>135 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>ИИЭиП <b>ср.цена</b></em> = <ins>116 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>ИКТЗИ <b>ср.цена</b></em> = <ins>134 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>ФМФ <b>ср.цена</b></em> = <ins>176 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>ИРЭФ-ЦТ <b>ср.цена</b></em> = <ins>135 тыс.руб.</ins>〽️\n"
                         "<b>Направление: Инфокоммуникационные системы и их информационная защита</b> = <ins>300 тыс.руб.</ins>\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=menu_one_300)

    await message.answer("➖➖➖<b><em>Образовательные программы КАИ <ins>СПО</ins> </em></b>➖➖➖\n\n"
                         "🪔<em>ТК <b>ср.цена</b></em> = <ins>65 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                         "🪔<em>КИТ <b>ср.цена</b></em> = <ins>65 тыс.руб.</ins>〽️\n"
                         "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

    await message.answer("<em>Все выше приведенные стоимости <b>оплачиваются за 1 год обучения</b></em>❗️")


@dp.callback_query_handler(text="wie")
async def voprosi_11(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(
        f"Вы выбрали <em><b>Инфокоммуникационные системы и их информационная защита</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>5,5 лет</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>25</ins>\n\n"
        f"💰<b>Количество платных мест</b>: <ins>5</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 188\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №5; ул. Карла Маркса, 31/7, ауд. 302\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 5, 7, 8\n\n"
        f"💼Выпускающая кафедра: нанотехнологий в электронике\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"🧑🏻‍🦰Зиатдинова Язиля Фоатовна - +7 (937) 615 83 42\n"
        f"WhatsApp - https://api.whatsapp.com/send?phone=+7%20(937)%20615%2083%2042\n"
        f"E-mail - yafziatdinova@kai.ru")

    await call.message.answer(
        f"Специальность готовит инженеров по разработке, диагностике и эксплуатации радиоэлектронной аппаратуры на транспорте (наземном, воздушном, морском).  Объектами профессиональной деятельности специалиста являются:\n"
        f"• радиолокационные, радионавигационные и связные системы\n"
        f"• системы и средства контроля и диагностики технического состояния эксплуатируемого оборудования\n"
        f"• системы передачи информации о движении транспортных средств и внешних условиях их эксплуатации\n"
        f"• системы комплексной обработки, отображения и регистрации информации о движении транспортных средств и внешних условиях\n"
        f"• системы управления движением транспортных средств и системы предупреждения их опасных сближений\n"
        f"Область профессиональной деятельности выпускников включает техническую эксплуатацию транспортного радиотехнического оборудования, в том числе радиолокационные, "
        f"радионавигационные, радиотехнические, инфокоммуникационные связные системы и комплексы, средства информационной защиты, обеспечивающие безопасность, регулярность и эффективность транспортных услуг.\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Проблемно-ориентированные пакеты прикладных программ в радиотехнике\n"
        f"• Программируемые микроэлектронные устройства\n"
        f"• Бортовые радиотехнические комплексы\n"
        f"• Радиолокационные системы управления воздушным движением\n"
        f"• Техническая эксплуатация радиоэлектронного оборудования\n"
        f"• Техническая диагностика радиоэлектронного оборудования\n"
        f"• Статистическая радиотехника\n"
        f"• Электромагнитная совместимость")
    await call.message.answer(f"Преподаватели:\n"
                              f"• 🧔🏽‍Файзуллин Р.Р., д.т.н., профессор\n"
                              f"• 👨🏽‍🦲Идиатуллов З.Р., к.т.н., доцент\n"
                              f"• 🧔🏽Куншин С.Е., к.т.н., доцент\n"
                              f"• 👨🏻Аюпов Т.А., к.т.н., доцент\n"
                              f"• 🧑🏻‍🦰Зиатдинова Я.Ф., старший преподаватель\n"
                              f"• 🧔🏻‍Русяев Н.Н., к.т.н., доцент\n"
                              f"• 👨🏾‍🦰Лернер И.М., к.т.н., доцент\n\n"
                              f"📕Темы выпускных работ:\n"
                              f"• Оптимизация технического обслуживания радиоэлектронного оборудования, подверженных полумарковским потокам отказов\n"
                              f"• Разработка методов оценки эксплуатационной надежности радиоэлектронного оборудования с учетом привнесенных отказов\n"
                              f"• Разработка наземной автоматизированной системы контроля (НАСК) для радиоэлектронного оборудования, входящего в состав ЦПНО (цифрового пилотажно-навигационного оборудования)\n"
                              f"• Оптимизация технического обслуживания радиоэлектронного оборудования, не влияющего на безопасность полетов\n"
                              f"• Оптимизация технического обслуживания радиоэлектронного оборудования, с учетом информации в момент контроля\n"
                              f"• Разработка универсального устройства прогнозирования состояния радиоэлектронного оборудования\n\n"
                              f"👩‍🏫Практика и стажировки:\n"
                              f"Базами практики являются профильные организации в области профессиональной деятельности будущих выпускников специальности. Профильные предприятия оснащены:\n"
                              f"• современным радиоэлектронным оборудованием\n"
                              f"• современными спутниковыми навигационными приборами\n"
                              f"• средствами радиосвязи\n"
                              f"• вычислительной и измерительной техникой\n"
                              f"❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗\n"
                              f"Обучение на такой современной лабораторной базе позволяет обучающимся решать технические задачи, приближенные к реальным условиям, и получать практические навыки по технической эксплуатации и ремонту транспортного радиооборудования различного уровня сложности, необходимые будущим радиоинженерам.\n"
                              f"❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗\n"
                              f"Практика для студентов организована на профильных предприятиях:\n"
                              f"• Казанский авиационный завод им. С.П. Горбунова – филиал ПАО «Туполев»\n"
                              f"• ПАО «Казанский вертолетный завод»\n"
                              f"• АО «Капо Авиа»\n"
                              f"• ООО «Тулпар Техник» и др. авиапредприятия Казани и Татарстана\n\n"
                              f"👨🏽‍🔧⚙️Трудоустройство:\n"
                              f"<b>Выпускники</b> данного направления подготовки могут работать в авиации, речном и морском транспорте, в компаниях, занимающихся автобусным и автомобильным сообщением. Основная задача специалиста – содержание в полной готовности и исправности транспортного радиооборудования, в том числе радиолокационного, радионавигационного, связных систем и комплексов.\n"
                              f"Инженеры-радиотехники руководят работами по модернизации, ремонту и наладке вверенных им систем. Диагностируют и устраняют неисправности. Устанавливают степень износа оборудования. Специалисты по радиотехнике и радиоэлектронике востребованы во всех высокотехнологичных отраслях.")


# referenes
@dp.message_handler(Text(equals=["❗Все важные ссылки❗"]))
async def get_classico(message: Message):
    await message.answer_sticker(r'CAACAgEAAxkBAAEHmttg5Gj3uYT8Pfil4ZVGA9T8tY3LtQACZgkAAr-MkARoAiu8qonXYCAE')
    await message.answer(f"<a href = 'https://lk.kai.ru/'>Официальный сайт Приемной комиссии</a>\n\n"
                         f"<a href = 'https://abiturientu.kai.ru/obsezitia'>Общежития</a>\n\n"
                         f"<a href = 'https://abiturientu.kai.ru/bvi'>Баллы за ваши индивидуальные достижения</a> ")


# contacts
@dp.message_handler(Text(equals=["☎️Контакты☎️"]))
async def get_classic(message: Message):
    await message.answer_sticker(r'CAACAgEAAxkBAAEHmsxg5Geqt0b-2U8sknmR19yXaWftRwACXwkAAr-MkAQRu-CGDx0pPyAE')
    await message.answer(f"📞Телефоны:📞\n\n"
                         f"📑<ins><em>Для справок</em></ins>📑\n\n"
                         f"+7 (800) 23 436 23\n\n"
                         f"+7 (843) 231 00 90\n\n"
                         f"+7 (927) 457 73 53\n\n"
                         f"📑<em><ins>Для справок</ins></em>📑\n\n")


# questions
@dp.message_handler(Text(equals=["❓Часто задаваемые вопросы❓"]))
async def get_classic(message: Message):
    await message.answer_sticker(r'CAACAgEAAxkBAAEHmp5g5GEMgPPu9_1LEUVKkNUCQq9GJQACYwkAAr-MkAQ7t_2k9eBloCAE')
    await message.answer(f"Какая тема тебя интересует?😇", reply_markup=temi_1)


###

# работа над вопросами
# Выход на главное меню
@dp.message_handler(Text(equals=['🏛Главное меню🏛']), state=text_one)
async def gl_manu(m: Message, state=FSMContext):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmqJg5GI3SrfZlXjP-vyLTDOUxsy_GAACcAkAAr-MkATlCLRcwrvl-SAE')
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)
    await state.finish()


# Отмена ввода сообщения
@dp.message_handler(Text(equals=['❌ОТМЕНИТЬ❌']), state=text_one)
async def cancel_write_FAQ(m: Message, state=FSMContext):
    await m.answer_sticker(r'CAACAgEAAxkBAAEHmqJg5GI3SrfZlXjP-vyLTDOUxsy_GAACcAkAAr-MkATlCLRcwrvl-SAE')
    await m.answer(f"🏛Главное меню🏛", reply_markup=determined_button)
    await state.finish()


# написать свой вопрос
@dp.message_handler(Text(equals=['📝Написать свой вопрос📝']), state=text_one)
async def texit_1(m: Message):
    await m.delete()
    await m.answer_sticker(r'CAACAgIAAxkBAAEHsfRg7uEwWmJTuC0JpEeHDrYvYRXh3gACdAEAAs-71A77o37THQ55OCAE')
    await m.answer("Напиши тему вопроса", reply_markup=menu_FAQ_cancel)
    await text_one.text_1.set()


# Отправка вопроса
@dp.message_handler(Text(equals=['🤞Отправить🤞']), state=text_one.complite)
async def text_complite(m: Message, state: FSMContext):
    await m.delete()
    us_id = m.from_user.id
    await m.answer_sticker(r'CAACAgEAAxkBAAEHslFg7uylFefIxacafonQynONuTzElgACVQkAAr-MkASDXlDZ0VvFnSAE')

    await m.answer(f"💖Сообщение оправлено на рассмотрение, отвечу на него в течении недели💖",
                   reply_markup=determined_button)
    await bot.send_message(chat_id=-500864965, text=f"<em><b>ТЕМА ВОПРОСА</b></em> - <ins><b>{subject}</b></ins>\n\n"
                                                    f"<em><b>САМ ВОПРОС</b></em> - <em><b>{maintext}</b></em>\n\n"
                                                    f"<em>дата</em> - {now_day.strftime('%d-%m-%y')}\n\n\n"
                                                    f"<em>link</em> - @{m.from_user.username}")

    await bot.send_message(chat_id=-500864965, text=f"👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆👆\n\n"
                                                    f"Отзыв пользователя чат-ботом Alina\n\n"
                                                    f"<em><b>link</b></em> - @{m.from_user.username}\n"
                                                    f"<em>ID</em> - {m.from_user.id}\n"
                                                    f"------------------------------")
    await state.finish()


# Исправление вопроса
@dp.message_handler(Text(equals=['🤦‍♀️Исправить🤦‍♀️']), state=text_one)
async def text_complite(m: Message, state: FSMContext):
    await m.delete()
    await m.answer_sticker(r'CAACAgIAAxkBAAEHspBg7veECs0TsQEGo4v9XJBZqq6AwQACegIAAvJ-ggxfFDCvI_9FjiAE')

    await m.answer("Напиши тему вопроса", reply_markup=menu_FAQ_cancel)

    await text_one.text_1.set()


@dp.message_handler(state=text_one.text_1)
async def text_Subject(m: Message):
    await m.delete()
    global subject
    subject = m.text
    await m.answer("Напиши свой вопрос\n\n"
                   "🥴🤕😮🙄<code>ВНИМАНИЕ</code>🙄😮🤕🥴\n"
                   "Пиши одним предложением🥰")

    await text_one.text_2.set()


@dp.message_handler(state=text_one.text_2)
async def text_midle(m: Message, state: FSMContext):
    await m.delete()
    global maintext
    maintext = m.text
    await m.answer(f"Тема вопроса: <b><ins>{subject}</ins></b>\n\n"
                   f"Сам вопрос: <b><em>{maintext}</em></b>\n\n"
                   f"Если всё верно жми 👉 🤞<strong>Отправить</strong>🤞\n"
                   f"Если нет, то жми 👉 🤦‍♀️<b>Исправить</b>🤦‍♀️\n"
                   f"Если ты случайно нажал/а или передумал/а писать свой вопрос нажми 👉 🏛<b>Главное меню</b>🏛",
                   reply_markup=menu_FAQ_vibor)

    await text_one.complite.set()


# all about documents
@dp.callback_query_handler(text="doki_postupati")
async def voprosi_11(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали \n\n"
                              f"<em><b>Всё о документах при поступлении в КНИТУ-КАИ</b></em>🗂\n\n"
                              f"Cпроси меня) или скопируй предложенный вопрос✏\n\n"
                              f"➖➖➖Внимание➖➖➖\n"
                              f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                              f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)

    await call.message.answer(f"Когда могу подать документы в КНИТУ-КАИ в 2021 году?")

    await call.message.answer(f"Какие документы необходимы для поступления?")

    await text_one.texit.set()


# all about admission
@dp.callback_query_handler(text="postupat_vopros")
async def vopros_2(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали\n\n"
                              f"<em><b>Всё об поступлении</b></em>📆\n\n"
                              f"Cпроси меня) или скопируй предложенный вопрос✏\n\n"
                              f"➖➖➖Внимание➖➖➖\n"
                              f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                              f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)

    await call.message.answer(
        f"Сколько специальностей можно указать в заявлении? И сколько согласий на зачисление можно подать?")

    await call.message.answer(f"Обязательно ли приезжать в Казань, чтобы подать документы для поступления в КНИТУ-КАИ?")

    await call.message.answer(f"Сколько лет действуют результаты ЕГЭ?")

    await call.message.answer(
        f"Можно ли поступить после среднего профессионального образования (техникум/колледж), не сдавая ЕГЭ?")

    await call.message.answer(
        f"Можно ли поступить в магистратуру на специальность, не связанную со специальностью бакалавриата/специалитета?")

    await call.message.answer(
        f"Есть ли какие-либо преимущества при поступлении, если имеется диплом победителя/призера олимпиады?")

    await text_one.texit.set()


# all about hostel
@dp.callback_query_handler(text="obsgiaga_vopros")
async def vopros_3(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали\n\n"
                              f"<em><b>Всё об общежитии</b></em>🏠\n\n"
                              f"Cпроси меня) или скопируй предложенный вопрос✏\n\n"
                              f"➖➖➖Внимание➖➖➖\n"
                              f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                              f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)

    await call.message.answer(
        f"Предоставляется ли общежитие иногородним на период приемной кампании и на период обучения?")

    await text_one.texit.set()


# foreign citizens
@dp.callback_query_handler(text="inostraci_vopros")
async def vopros_4(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали\n\n"
                              f"<em><b>Для иностранных граждан</b></em>👥🇺🇸\n\n"
                              f"Спроси меня) или скопируй предложенный вопрос✏\n\n"
                              f"➖➖➖Внимание➖➖➖\n"
                              f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                              f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)

    await text_one.texit.set()


# all about military department
@dp.callback_query_handler(text="war")
async def vopros_4(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data}")

    await call.message.delete()
    await call.message.answer(f"Вы выбрали\n\n"
                              f"<em><b>Всё о военной кафедре</b></em>💂‍♀️\n\n"
                              f"Спроси меня) или скопируй предложенный вопрос✏\n\n"
                              f"➖➖➖Внимание➖➖➖\n"
                              f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                              f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)

    await call.message.answer(f"Есть ли в Вашем университете военная кафедра?")

    await text_one.texit.set()


###

# text handler
###
@dp.message_handler(content_types=['text'], state=text_one.texit)
async def jiirrr(message: Message):
    if message.text == "Когда могу подать документы в КНИТУ-КАИ в 2021 году?":
        await message.answer(
            f"<em>Единый день начала приема документов 18 июня 2021 года. Прием документов, необходимых для поступления на очную форму обучения на бюджетные места по программам бакалавриата/специалитета, завершается 25 июля 2021 года. Прием оригиналов документов установленного образца и заявлений о согласии на зачисление для поступающих на очную форму обучения на бюджетные места по программам бакалавриата/специалитета завершается:\n"
            f"• 4 августа – от лиц, поступающих без вступительных испытаний (олимпиадники), на места в пределах квоты приема лиц, имеющих особые права, поступающих на места в пределах квоты целевого приема\n"
            f"• 11 августа – от лиц, включенных в конкурсный список, желающих быть зачисленными по общему конкурсу.</em>")


    elif message.text == "Какие документы необходимы для поступления?":
        await message.answer(f"<em>При подаче заявления о приеме поступающим предоставляются:\n"
                             f"• копия документа, удостоверяющего личность, гражданство (<b>обычно это паспорт</b>)\n"
                             f"• копия или оригинал документа об образовании (<b>не забудьте приложение с оценками!</b>)\n"
                             f"копия страхового свидетельства обязательного пенсионного страхования (СНИЛС, при наличии) (<b>для поступающих на программы бакалавриата, специалитета, магистратуры</b>)\n"
                             f"• копии документов, подтверждающих, что Вы имеете особое право (если Вы поступаете по квоте (<b>дети-инвалиды, инвалиды I и II групп, инвалиды с детства, инвалиды вследствие военной травмы или заболевания, полученных в период прохождения военной службы, дети-сироты, дети, оставшиеся без попечения родителей, до достижения ими возраста 23 лет, ветераны боевых действий</b>)\n"
                             f"• копия договора о целевом обучении (<b>если Вы поступаете по квоте на целевое обучение</b>)\n"
                             f"• копии документов, подтверждающих индивидуальные достижения, результаты которых учитываются при приеме на обучение в соответствии с Правилами приема в КНИТУ-КАИ (<b>если Вы собираетесь учитывать индивидуальные достижения</b>)\n"
                             f"• копии соответствующих медицинских справок (<b>если для поступления на указанные в заявлении специальности/направления требуется обязательный предварительный медосмотр</b>)\n"
                             f"• копии иных документов (<b>представляются по усмотрению поступающего)</b></em>")


    elif message.text == "Сколько специальностей можно указать в заявлении? И сколько согласий на зачисление можно подать?":
        await message.answer(
            f"<em>Если в прошлом году можно было подать заявление на три специальности, то сейчас в КАИ в заявлении можно указать 5 специальностей, при этом предельное количество подаваемых согласий на зачисление составляет 10.</em>")


    elif message.text == "Обязательно ли приезжать в Казань, чтобы подать документы для поступления в КНИТУ-КАИ?":
        await message.answer(
            f"<em>Для подачи документов в КНИТУ-КАИ вам не обязательно приезжать в Казань. Документы, необходимые для поступления, направляются в КНИТУ-КАИ одним из следующих способов:\n"
            f"• через операторов почтовой связи общего пользования\n"
            f"• с использованием средств электронной подачи посредством Личного кабинета абитуриента на официальном сайте Приемной комиссии (https://lk.kai.ru/), а также с использованием суперсервиса «Поступление в вуз онлайн» посредством федеральной государственной информационной системы «Единый портал государственных и муниципальных услуг (функций)»</em>")


    elif message.text == "Какие ЕГЭ или вступительные испытания нужны для поступления на бакалавриат/специалитет?":
        await message.answer(
            f"<em>С перечнем направлений подготовки/специальностей и вступительных испытаний можно ознакомиться по ссылке (https://abiturientu.kai.ru/documents/1470594/10919842/Информация+о+приоритетности+вступительных+испытаний.pdf).\n"
            f"При приеме на обучение на ВСЕ направления подготовки/специальности программ бакалавриата/специалитета КАИ установил несколько предметов по выбору. Вы сами выбираете, результаты какого предмета предоставить (например, обществознание или иностранный язык), либо при сдаче нескольких предметов (например, и физика, и информатика) будет учитываться наивысший результат</em>")


    elif message.text == "Сколько лет действуют результаты ЕГЭ?":
        await message.answer(
            f"<em>Для поступления в КНИТУ-КАИ результаты ЕГЭ учитываются за 4 предыдущих года, предшествующих году поступления, т.е. для поступающих в 2021 году результаты действуют с 2017 года.</em>")


    elif message.text == "Можно ли поступить после среднего профессионального образования (техникум/колледж), не сдавая ЕГЭ?":
        await message.answer(
            f"<em>Да, можно. Абитуриентам, поступающим на базе среднего профессионального образования необходимо сдавать вступительные, проводимые КНИТУ-КАИ самостоятельно</em>")


    elif message.text == "Есть ли в Вашем университете военная кафедра?":
        await message.answer(
            f"<em>Да, поступающие в КНИТУ-КАИ могут получить параллельно военную специальность. Обучение проводится по программам подготовки офицеров запаса, сержантов и солдат запаса. Отбор кандидатов для обучения в военном учебном центре проводится на 2-м курсе. Прием в военный учебный центр осуществляется на конкурсной основе</em>")


    elif message.text == "Можно ли поступить в магистратуру на специальность, не связанную со специальностью бакалавриата/специалитета?":
        await message.answer(
            f"<em>Направление подготовки/специальность не влияет на право обучаться по другому направлению подготовки программы магистратуры</em>")


    elif message.text == "Есть ли какие-либо преимущества при поступлении, если имеется диплом победителя/призера олимпиады?":
        await message.answer(
            f"<em>При поступлении на программы бакалавриата и программы специалитета поступающим предоставляются преимущества, обусловленные уровнями и статусами олимпиад школьников:\n"
            f"а) прием без вступительных испытаний на обучение по специальностям и направлениям подготовки, соответствующим профилю олимпиады школьников\n"
            f"б) приравнивание к лицам, набравшим максимальное количество баллов ЕГЭ по общеобразовательному предмету, соответствующему профилю олимпиады школьников\n"
            f"Преимущества победителю/призеру олимпиады школьников из Перечня Всероссийских олимпиад школьников предоставляются в случае получения ими оценки не менее 75 баллов на ЕГЭ по предмету, соответствующему профилю олимпиады школьников, а также при подтверждении статуса победителя или призера олимпиады школьников не позднее дня завершения приема документов в КНИТУ-КАИ.</em>")


    elif message.text == "Предоставляется ли общежитие иногородним на период приемной кампании и на период обучения?":
        await message.answer(
            f"<em>КНИТУ-КАИ обеспечивает общежитиями иногородних студентов на весь период обучения при соблюдении правил проживания. Оформление договоров на поселение в общежития поступающих на 1 курс в КНИТУ-КАИ бюджетной и платной формы обучения производится, как правило, в единые дни зачисления в университет. При себе иметь паспорт и студенческий билет/извещение о зачислении в КНИТУ-КАИ. Стоимость проживания в общежитиях варьируется от 450 до 600 рублей в месяц в зависимости от условий проживания.\n"
            f"На период приемной кампании университет не предоставляет места в общежитиях. Однако, Вы можете воспользоваться услугами Профилактория, стоимость проживания составляет 500-600 рублей в сутки</em>")

    elif message.text == message.text:
        await message.answer(f"➖➖➖Внимание➖➖➖\n"
                             f"Написать вопрос 👉 📝<b>Написать свой вопрос</b>📝\n\n"
                             f"Чтобы выйти нажми 🏛<b>Главное меню</b>🏛", reply_markup=menu_FAQ)
    await text_one.texit.set()


# Ответ на оскорбления
@dp.message_handler(content_types=['text'])
async def nono_bro(m: Message):
    if m.text == 'хуй':
        await m.answer_sticker(r'CAACAgIAAxkBAAEHsnRg7vUaB6J3OblKaPODkp2GyZ1l6wACNgADZGFxLrwmAk3zSA5fIAQ')
        await m.answer("Еще одно такое сообщение и спам тебе)")

    elif m.text == 'похуй':
        await m.answer_sticker(r'CAACAgIAAxkBAAEHsoJg7vVro94I0KKRUGZKrdrYZYI4CgACUAADZGFxLqIMX8u85c_VIAQ')

    elif m.text == 'ебанат':
        await m.answer_sticker(r'CAACAgIAAxkBAAEHsoZg7vWy9FZg5kP6g1pzxN-CbHh8KgACaAADZGFxLq-cS7Y8iICPIAQ')
