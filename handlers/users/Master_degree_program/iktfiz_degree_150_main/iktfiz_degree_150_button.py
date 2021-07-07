from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.degree_inline.info_degree_150_inbut.deg_150_inbut import menu_150iktfiz_degree_button, \
    menu_150iktfiz_degree_button_1, back_deg_150_button
from keyboards.inline.degree_inline.main_degree_inbut import menu_iltfiz_degree_button_150


import logging


# ИАНТЭ

@dp.callback_query_handler(text="IANT_degree_2")
async def iant_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Вы выбрали <b><ins>Институт авиации, наземного транспорта и энергетики</ins></b>\n"
                           f"Направления:", reply_markup=menu_150iktfiz_degree_button)


# 145
@dp.callback_query_handler(text="Shipbuilding_deg_2")
async def iant_deg_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <b><em>Кораблестроение</em></b>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>4 года</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>25</ins>\n\n"
        f"💯<b>Проходной балл по целевому приему в 2020 году</b>: 145\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №3; ул. Толстого, 15, ауд. 508\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 2, 3, 7, 8\n\n"
        f"💼Выпускающая кафедра: конструкции и проектирования летательных аппаратов\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"🧑🏻‍🦱Першин Евгений Александрович - +7 (843) 231 03 18\n"
        f"E-mail - eapershin@kai.ru")

    await c.message.answer(
        f"Основная цель образовательной программы – подготовка молодых специалистов (бакалавров) в области профессиональной деятельности, связанной с созданием судов морского и речного флота, а также средств океанотехники.\n"
        f"Проектная деятельность обучающихся включает в себя участие в проектировании и расчётах объектов морской и речной техники, а также их подсистем в соответствии с техническим заданием, с использованием стандартных средств автоматизации проектно-конструкторских работ. Научно-исследовательская деятельность студентов заключается:\n"
        f"• в разработке планов и программ отдельных этапов работ\n"
        f"• сборе, обработке, анализе и систематизации научно-технической информации по тематике исследований\n"
        f"• участие в выполнение экспериментов, составлении их описаний и анализе результатов\n\n"
        f"🚢Ключевые дисциплины учебного плана:\n"
        f"• Объекты морской техники\n"
        f"• Теория корабля\n"
        f"• Проектирование судов и кораблей\n"
        f"• Конструкция корпуса корабля\n"
        f"• Сварка в кораблестроении и др.")

    await c.message.answer(f"Преподаватели:\n"
                           f"• 👨🏼‍🦱Гайнутдинов В.Г., доктор технических наук, профессор\n"
                           f"• 🧔Першин Е.А., кандидат технических наук, доцент\n"
                           f"• 👨Левшонков Н.В., кандидат технических наук, доцент\n"
                           f"• 👨🏽‍🦰Петрушенко Р.Ю., кандидат технических наук, доцент\n"
                           f"• 👴🏻Гусев А.Л., старший преподаватель\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"ВКР включает в себя разработку полного проекта транспортного судна морского, смешанного или внутреннего плавания:\n"
                           f"• определение основных характеристик, эксплуатационных и мореходных качеств и их проверка на соответствие требованиям квалификационных органов\n"
                           f"• конструирование судовых механизмов и устройств\n"
                           f"• проектирование трюмных систем\n"
                           f"• выбор и обоснование энергетической установки\n\n"
                           f"Например: Морское сухогрузное судно дедвейтом 12000 т класса КМ«ICE3[1] R2 AUT2, предназначенный для перевозки генеральных и насыпных грузов, включая контейнеры международного стандарта в трюмах и на люковых крышках; район эксплуатации Владивосток–Петропавловск-Камчатский–Магадан; автономность 14 суток; скорость 13 узлов; экипаж 14 человек.")

    await c.message.answer(f"👩‍🏫☔️Практика и стажировки:\n"
                           f"• АО «Зеленодольское проектно-конструкторское бюро», г. Зеленодольск, РТ\n"
                           f"• АО «Зеленодольский завод им. А.М. Горького», г. Зеленодольск, РТ\n"
                           f"• выездные практики\n"
                           f"• практика в виде научно-исследовательской работы на кафедре\n\n"
                           f"🚤Трудоустройство:\n"
                           f"• АО «Зеленодольское проектно-конструкторское бюро», г. Зеленодольск, РТ\n"
                           f"• АО «Зеленодольский завод им. А.М. Горького», г. Зеленодольск, РТ",
                           reply_markup=back_deg_150_button)


# Ирэт
@dp.callback_query_handler(text="IREF_CT_degree_2")
async def IANT_2(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer("Вы выбрали <b><ins>Институт Радиоэлектроники, фотоники и цифровых технологий</ins></b>\n\n"
                           "Направления:", reply_markup=menu_150iktfiz_degree_button_1)


# 150
@dp.callback_query_handler(text="Transmission_degree_systems_iktfiz_2")
async def iret_iktfiz_1(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(
        f"Вы выбрали <em><b>Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы</b></em>\n\n"
        f"🗓<b>Срок обучения</b>: <ins>5,5 лет</ins>\n\n"
        f"💂‍♂️<b>Военная кафедра</b> - <ins>есть</ins>\n\n"
        f"🆓<b>Количество бюджетных мест</b>: <ins>46</ins>\n\n"
        f"💯<b>Проходной балл в 2020</b>: 150\n\n"
        f"🔖Государственная аккредитация: есть\n\n"
        f"🏠Дирекция:учебный корпус №5; ул. Карла Маркса, 31/7, ауд. 302\n\n"
        f"🏛Обучение проводится в учебных корпусах №: 5, 7, 8\n\n"
        f"💼Выпускающая кафедра: радиоэлектронных и телекоммуникационных систем\n\n"
        f"<b>Контактное лицо по работе с абитуриентами</b>:\n"
        f"👨🏼‍🦳Надеев Адель Фирадович - +7 (843) 231 59 11\n"
        f"E-mail - afnadeev@kai.ru\n\n")

    await c.message.answer(
        f"Данная специальность развивает лучшие традиции отечественной системы подготовки инженерных кадров и в течение полноценного 5,5 летнего цикла обеспечивает подготовку настоящих инженеров в области радиоэлектронных систем.\n"
        f"Полноценная физико-математическая подготовка, знания специализированных дисциплин, профессиональное владение современными средствами компьютерного проектирования радиоэлектронных устройств и систем, обеспечивают высокую конкурентоспособность и востребованность выпускников в самых высокотехнологичных и динамично развивающихся отраслях. С каждым годом стремительно расширяется масштаб применения радиоэлектронных систем во всех сферах человеческой деятельности:\n"
        f"• телекоммуникации\n"
        f"• транспорт\n"
        f"• авиация\n"
        f"• космос\n"
        f"• энергетика\n"
        f"• медицина\n"
        f"• строительство\n"
        f"• городская инфраструктура и многое другое\n"
        f"Передача и обработка сигналов, навигация, локация, управление, робототехника раскрывают фантастические возможности современной микроэлектроники, микропроцессорной техники, информационных технологий.\n\n"
        f"🖥Ключевые дисциплины учебного плана:\n"
        f"• Физика\n"
        f"• Инженерная и компьютерная графика\n"
        f"• Радиоматериалы и компоненты\n"
        f"• Прикладные информационные технологии\n"
        f"• Основы теории цепей\n"
        f"• Электроника\n"
        f"• Радиотехнические цепи и сигналы\n"
        f"• Электромагнитные поля и волны\n"
        f"• Основы теории систем\n"
        f"• Радиоизмерения\n"
        f"• Схемотехника аналоговых электронных устройств\n"
        f"• Модемы и кодеки радиосистем\n"
        f"• Устройства генерирования и формирования сигналов\n"
        f"• Основы компьютерного проектирования и моделирования РЭС\n"
        f"• Геоинформационные технологии\n"
        f"• Основы физического и математического моделирования\n"
        f"• Радиоавтоматика\n"
        f"• Устройства приема и преобразования сигналов\n"
        f"• Электродинамика и распространение радиоволн\n"
        f"• Электропреобразовательные устройства радиоэлектронных средств\n"
        f"• Статистическая радиотехника\n"
        f"• Цифровые устройства и микропроцессоры\n"
        f"• Устройства сверхвысоких частот и антенны\n"
        f"• Статистические методы обработки сигналов\n"
        f"• Цифровая обработка сигналов\n"
        f"• Измерительные системы\n"
        f"• Основы теории радиолокационных систем и комплексов\n"
        f"• Телевизионные системы\n"
        f"• Основы конструирования и производства радиоэлектронных средств\n"
        f"• Вычислительные устройства и системы\n"
        f"• Основы теории радионавигационных систем и комплексов\n"
        f"• Основы теории радиосистем и комплексов управления\n"
        f"• Основы теории радиосистем передачи информации\n"
        f"• Введение в системотехническое проектирование\n"
        f"• Надежность радиотехнических систем\n"
        f"• Основы теории систем и комплексов радиоэлектронной борьбы\n"
        f"• Электромагнитная совместимость\n"
        f"• Антенны летательных аппаратов\n"
        f"• Методы и устройства синхронизации в радиосистемах передачи информации\n"
        f"• Широкополосные системы передачи информации\n"
        f"• Квантовые системы\n"
        f"• Мобильные системы передачи информации\n")

    await c.message.answer(f"Преподаватели:\n"
                           f"<em>Профессора</em>:\n"
                           f"академик АН РТ 👤Чабдаров Ш.М.\n"
                           f"д.т.н. 👤Даутов О.Ш.\n"
                           f"д.т.н. 👤Морозов Г.А.\n"
                           f"д.ф-м.н. 👤Надеев А.Ф.\n"
                           f"д.т.н. 👤Боголюбов В.М.\n"
                           f"д.т.н. 👤Седельников Ю.Е.\n"
                           f"д.т.н. 👤Козлов С.В.\n"
                           f"к.т.н. 👤Щербаков Г.И.\n"
                           f"<em>Доценты</em>:\n"
                           f"к.т.н. 👤Чони Ю.И.\n"
                           f"к.т.н. 👤Авксентьев А.А.\n"
                           f"к.т.н. 👤Горохов С.Н.\n"
                           f"к.т.н. 👤Карловский А.П.\n"
                           f"к.т.н. 👤Карманов И.В.\n"
                           f"к.т.н. 👤Коробков А.А.\n"
                           f"к.т.н. 👤Лаврушев В.Н.\n"
                           f"к.т.н. 👤Можгинский В.Л.\n"
                           f"к.т.н. 👤Потапова О.В.\n"
                           f"к.т.н. 👤Седов С.С.\n"
                           f"к.т.н. 👤Скачков В.А.\n"
                           f"д.т.н. 👤Спирина Е.А.\n"
                           f"к.т.н. 👤Стахова Н.Е.\n"
                           f"к.т.н. 👤Фадеева Л.Ю.\n"
                           f"к.т.н. 👤Щербакова Т.Ф.\n\n"
                           f"📕Темы выпускных работ:\n"
                           f"• Разработка автомобильного радара предотвращения столкновений\n"
                           f"• Разработка программно-определяемой радиосистемы передачи информации\n"
                           f"• Разработка системы навигации и передачи видеоинформации с борта беспилотного летательного аппарата\n"
                           f"• Разработка береговой радиолокационной системы управления судами в проливах и акваториях морских портов\n"
                           f"• Разработка бортовой РЛС обнаружения и автосопровождения низколетящих целей\n"
                           f"• Разработка мобильной метеорологической РЛС изучения атмосферы Земли\n"
                           f"• Разработка вертолетного радиолокационного комплекса\n"
                           f"• Разработка авиационного радиовысотомера\n"
                           f"• Разработка системы спутниковой связи с подвижными наземными объектами\n"
                           f"• Разработка радиоэлектронной системы контроля функционального состояния водителя транспортного средства\n\n"
                           f"👩‍🏫Практика и стажировки:\n"
                           f"• ПАО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко (г. Казань)\n"
                           f"• ПАО «Радиоприбор» (г. Казань)\n"
                           f"• АО «ЭЛЕКОН» (г. Казань)\n"
                           f"• АО «Ижевский радиозавод»\n"
                           f"• Региональный центр National Instruments (г. Казань, КНИТУ-КАИ)\n"
                           f"• ПАО «Туполев» (г. Казань)\n"
                           f"• «Рубеж-М» (г. Москва) и многих других, а также на научно-производственных предприятиях целевой подготовки выпускников\n\n"
                           f"👨🏽‍🔧⚙️Трудоустройство:\n"
                           f"<b>Выпускники</b> данного направления уже более 60 лет обеспечивают развитие радиоэлектронной отрасли нашей страны, составляют основу кадрового обеспечения высокотехнологичных научно-производственных объединений, осуществляющих разработку, производство и эксплуатацию радиоэлектронной аппаратуры. Среди выпускников данной специальности целая плеяда прославленных генеральных конструкторов, руководителей НИИ и предприятий, ученых, ведущих специалистов таких предприятий как:\n"
                           f"• ПАО «Научно-производственное объединение «Радиоэлектроника» им. В.И. Шимко (г. Казань)\n"
                           f"• ПАО «Радиоприбор» (г. Казань)\n"
                           f"• ПАО «Казанский электротехнический завод»\n"
                           f"• ОАО «Казанский завод «Электроприбор»\n"
                           f"• ПАО «Туполев» (г. Казань)\n"
                           f"• ПАО «Казанский вертолетный завод»\n"
                           f"• АО «Научно-производственное объединение «Государственный институт прикладной оптики» (г. Казань)\n"
                           f"• АО «Ижевский радиозавод»\n"
                           f"• АО «Ижевский электромеханический завод «Купол»\n"
                           f"• ПАО «МТС»\n"
                           f"• ПАО «МТС»\n"
                           f"• ПАО «Мегафон»\n"
                           f"• АО «Информационные спутниковые системы» им. М.Ф. Решетнева (г. Красноярск) и многих других\n"
                           f"Многие наши выпускники организуют собственные инжиниринговые компании, высокотехнологичные фирмы и предприятия.",
                           reply_markup=back_deg_150_button)


# назад
@dp.callback_query_handler(text="back_150_deg_2")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_iltfiz_degree_button_150)


# исклик то назад к факультетам
@dp.callback_query_handler(text="back_deg_150")
async def b_177(c: CallbackQuery):
    await c.answer(cache_time=60)

    callback_data = c.data

    logging.info(f"{callback_data=}")

    await c.message.delete()
    await c.message.answer(f"Выбери факультет", reply_markup=menu_iltfiz_degree_button_150)