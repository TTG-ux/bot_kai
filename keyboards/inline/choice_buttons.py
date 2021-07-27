from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

languages_markup = InlineKeyboardMarkup(row_width=1)
ln_1 = InlineKeyboardButton(text="Русский", callback_data="lang_ru")
languages_markup.insert(ln_1)

# Платное информация
# ИАЭП
baaip_platka = InlineKeyboardMarkup(row_widht=1)

pl_iiaap1 = InlineKeyboardButton(text="Природообустройство и водопользование (заочное)", callback_data="zao_1")

baaip_platka.insert(pl_iiaap1)

pl_iiaap2 = InlineKeyboardButton(text="Стандартизация, сертификация и метрология (заочное)", callback_data="zao_2")

baaip_platka.insert(pl_iiaap2)

# ИКТЗИ
platka_iktziii = InlineKeyboardMarkup(row_width=1)

pl_iktzi1 = InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BigData",
                                 callback_data="Big Data_iktzi")

platka_iktziii.insert(pl_iktzi1)

# Ирэт
platka_iret1 = InlineKeyboardMarkup(row_width=1)

iretpla_1 = InlineKeyboardButton(text="Информационные сети, мобильная и оптическая связь, квантовые коммуникации",
                                 callback_data="inforeti")

platka_iret1.insert(iretpla_1)
# хенд назад
back_buttonplatkair = InlineKeyboardMarkup(row_width=1)

pl_ir_112 = InlineKeyboardButton(text="Назад", callback_data="pl_ir_11123")

back_buttonplatkair.insert(pl_ir_112)

# Темы вопросов
temi_1 = InlineKeyboardMarkup(row_width=1)

question_1 = InlineKeyboardButton(text="Всё о документах при поступлении в КНИТУ-КАИ🗂", callback_data="doki_postupati")
temi_1.insert(question_1)

question_2 = InlineKeyboardButton(text="Всё об поступлении📆", callback_data="postupat_vopros")
temi_1.insert(question_2)

question_3 = InlineKeyboardButton(text="Всё об общежитии🏠", callback_data="obsgiaga_vopros")
temi_1.insert(question_3)

question_4 = InlineKeyboardButton(text="Для иностранных граждан👥🇺🇸", callback_data="inostraci_vopros")
temi_1.insert(question_4)

question_5 = InlineKeyboardButton(text="Всё о военной кафедре💂‍♀️", callback_data="war")
temi_1.insert(question_5)

# Клава Гумы
# 2
# Выбор баллов
ViborOBS_button_angl = InlineKeyboardMarkup(row_width=1)

Obsnnivibor_1_angl = InlineKeyboardButton(text=">=140", callback_data="Obsiiaga_140_angl")

ViborOBS_button_angl.insert(Obsnnivibor_1_angl)

# Платка Обществознание
Obsagha_button1_angl = InlineKeyboardMarkup(row_width=1)

Obsehtvo_2_angl = InlineKeyboardButton(text="💰Платное обучение💰", callback_data="platka_obsix_1_angl")

Obsagha_button1_angl.insert(Obsehtvo_2_angl)
# Факультеты
IIaiP_button1_angl = InlineKeyboardMarkup(row_width=1)

takoi1fuck_1_angl = InlineKeyboardButton(text="Экономика и управление цифровым предприятием",
                                         callback_data="Akanomi_obsix_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_1_angl)

takoi1fuck_2_angl = InlineKeyboardButton(text="Цифровые технологии в мировой экономике", callback_data="cifri_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_2_angl)

takoi1fuck_3_angl = InlineKeyboardButton(text="Промышленная коммерция", callback_data="korporation_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_3_angl)

takoi1fuck_4_angl = InlineKeyboardButton(text="Производственный менеджмент", callback_data="menedgment_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_4_angl)

takoi1fuck_5_angl = InlineKeyboardButton(text="Управление проектами", callback_data="proekti_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_5_angl)

# Хендлер "Назад"
back_button140OBS_angl = InlineKeyboardMarkup(row_width=1)

OBS_140_angl = InlineKeyboardButton(text="Назад", callback_data="back_140_angl")

back_button140OBS_angl.insert(OBS_140_angl)

# 1
# Выбор баллов
ViborOBS_button = InlineKeyboardMarkup(row_width=1)

Obsnnivibor_1 = InlineKeyboardButton(text=">=140", callback_data="Obsiiaga_140")

ViborOBS_button.insert(Obsnnivibor_1)

# Платка Обществознание
Obsagha_button1 = InlineKeyboardMarkup(row_width=1)

Obsehtvo_2 = InlineKeyboardButton(text="💰Платное обучение💰", callback_data="platka_obsix_1")

Obsagha_button1.insert(Obsehtvo_2)
# Факультеты
IIaiP_button1 = InlineKeyboardMarkup(row_width=1)

takoi1fuck_1 = InlineKeyboardButton(text="Экономика и управление цифровым предприятием",
                                    callback_data="Akanomi_obsix_1")

IIaiP_button1.insert(takoi1fuck_1)

takoi1fuck_2 = InlineKeyboardButton(text="Цифровые технологии в мировой экономике", callback_data="cifri_1")

IIaiP_button1.insert(takoi1fuck_2)

takoi1fuck_3 = InlineKeyboardButton(text="Промышленная коммерция", callback_data="korporation_1")

IIaiP_button1.insert(takoi1fuck_3)

takoi1fuck_4 = InlineKeyboardButton(text="Производственный менеджмент", callback_data="menedgment_1")

IIaiP_button1.insert(takoi1fuck_4)

takoi1fuck_5 = InlineKeyboardButton(text="Управление проектами", callback_data="proekti_1")

IIaiP_button1.insert(takoi1fuck_5)

takoi1fuck_6 = InlineKeyboardButton(text="Управление человеческими ресурсами", callback_data="ludi_1")

IIaiP_button1.insert(takoi1fuck_6)

# Хендлер "Назад"
back_button140OBS = InlineKeyboardMarkup(row_width=1)

OBS_140 = InlineKeyboardButton(text="Назад", callback_data="back_140")

back_button140OBS.insert(OBS_140)

# 209
# Платка не платка в МИР
IKit_la = InlineKeyboardMarkup(row_width=1)

Kito_1 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_1")

IKit_la.insert(Kito_1)

# IRET
UIR_button = InlineKeyboardMarkup(row_width=1)

first_Iret = InlineKeyboardButton(text="⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret1")

UIR_button.insert(first_Iret)

# ИРЭТ ИКТ
Informat_IRET1_button = InlineKeyboardMarkup(row_width=1)

IRINF_1 = InlineKeyboardMarkup(text="Информационные сети, мобильная и оптическая связь, квантовые коммуникации",
                               callback_data="IRINF_infoseti")

Informat_IRET1_button.insert(IRINF_1)

# 232
# Платка не платка в МИР
IKit_la4 = InlineKeyboardMarkup(row_width=1)

Kito_14 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_4")

IKit_la4.insert(Kito_14)

# IRET и ИКТЗИ
boom_kar = InlineKeyboardMarkup(row_width=1)

first_Iret4 = InlineKeyboardButton(text="⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret4")

boom_kar.insert(first_Iret4)

first_IKTZI4 = InlineKeyboardButton(text="ИКТЗИ", callback_data="this_is_iktzi4")

boom_kar.insert(first_IKTZI4)

# ИРЭТ ИКТ
Informat_IRET4_button = InlineKeyboardMarkup(row_width=1)

IRINF_4 = InlineKeyboardMarkup(text="Информационные сети, мобильная и оптическая связь, квантовые коммуникации",
                               callback_data="IRINF_infoseti4")

Informat_IRET4_button.insert(IRINF_4)

# ИКТЗИ ИКТ
Informat_IKT4_button = InlineKeyboardMarkup(row_width=1)

IKTINF_4 = InlineKeyboardButton(text="Робототехника и цифровая экономика", callback_data="Robot_4")

Informat_IKT4_button.insert(IKTINF_4)

# Хендлер "Назад"

back_button232IKT = InlineKeyboardMarkup(row_width=1)

b_1232IKT = InlineKeyboardButton(text="Назад", callback_data="back_232")

back_button232IKT.insert(b_1232IKT)

# 245
# Платка не платка в МИР
IKit_la2 = InlineKeyboardMarkup(row_width=1)

Kito_11 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_2")

IKit_la2.insert(Kito_11)

# IRET(245)
UIR_button2 = InlineKeyboardMarkup(row_width=1)

first_Iret2 = InlineKeyboardButton(text="⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret2")

UIR_button2.insert(first_Iret2)

first_IKTZI2 = InlineKeyboardButton(text="ИКТЗИ", callback_data="this_is_iktzi2")

UIR_button2.insert(first_IKTZI2)

# ИРЭТ ИКТ(245)
Informat_IRET2_button = InlineKeyboardMarkup(row_width=1)

IRINF_2 = InlineKeyboardMarkup(text="Информационные сети, мобильная и оптическая связь, квантовые коммуникации",
                               callback_data="IRINF_infoseti2")

Informat_IRET2_button.insert(IRINF_2)

# ИКТЗИ ИКТ 245
Informat_IKT2_button = InlineKeyboardMarkup(row_width=1)

IKTINF_12 = InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BigData",
                                 callback_data="BigData_2")

Informat_IKT2_button.insert(IKTINF_12)

IKTINF_22 = InlineKeyboardButton(text="Робототехника и цифровая экономика", callback_data="Robot_2")

Informat_IKT2_button.insert(IKTINF_22)

# Хендлер "Назад"

back_button245IKT = InlineKeyboardMarkup(row_width=1)

b_1245IKT = InlineKeyboardButton(text="Назад", callback_data="back_245")

back_button245IKT.insert(b_1245IKT)

# 247
# Платка не платка в МИР(247)
IKit_la3 = InlineKeyboardMarkup(row_width=1)

Kito_13 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_3")

IKit_la3.insert(Kito_13)

# IRET и ИКТЗИ(247)
UIR_button3 = InlineKeyboardMarkup(row_width=1)

first_Iret3 = InlineKeyboardButton(text="⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret3")

UIR_button3.insert(first_Iret3)

first_IKTZI3 = InlineKeyboardButton(text="ИКТЗИ", callback_data="this_is_iktzi3")

UIR_button3.insert(first_IKTZI3)

# ИРЭТ ИКТ(247)
Informat_IRET3_button = InlineKeyboardMarkup(row_width=1)

IRINF_13 = InlineKeyboardMarkup(text="Информационные сети, мобильная и оптическая связь, квантовые коммуникации",
                                callback_data="IRINF_infoseti3")

Informat_IRET3_button.insert(IRINF_13)

# ИКТЗИ ИКТ 247
Informat_IKT3_button = InlineKeyboardMarkup(row_width=1)

IKTINF_13 = InlineKeyboardButton(text="Прикладная математика и информатика. Модели управления BigData",
                                 callback_data="BigData_3")

Informat_IKT3_button.insert(IKTINF_13)

IKTINF_23 = InlineKeyboardButton(text="Интеллектуальные информационные системы", callback_data="intelectyal_3")

Informat_IKT3_button.insert(IKTINF_23)

IKTINF_33 = InlineKeyboardButton(text="Робототехника и цифровая экономика", callback_data="Robot_3")

Informat_IKT3_button.insert(IKTINF_33)

# Хендлер "Назад"

back_button247IKT = InlineKeyboardMarkup(row_width=1)

b_1247IKT = InlineKeyboardButton(text="Назад", callback_data="back_247")

back_button247IKT.insert(b_1247IKT)

determined_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🔷 Поступление☑️"),
        KeyboardButton(text="👉 Без баллов ЕГЭ 👈")
    ],
    [
        KeyboardButton(text="❓Часто задаваемые вопросы❓")
    ],
    [
        KeyboardButton(text="❗Все важные ссылки❗"),
        KeyboardButton(text="☎️Контакты☎️")
    ],
    [
        KeyboardButton(text='🚀Платное обучение🚀')
    ],
    [
        KeyboardButton(text="⚡️Оставить отзыв🖍")
    ]
],
    resize_keyboard=True
)

# Бюджет от 3-4
colledge_button = InlineKeyboardMarkup(row_width=1)

tk_solo_1 = InlineKeyboardButton(text="ТК", callback_data="tk_solo_1")
colledge_button.insert(tk_solo_1)

# ТК
tk_slo_button = InlineKeyboardMarkup(row_width=1)

dl_solo_1 = InlineKeyboardButton(text="Экономика и бухгалтерский учет (по отраслям)", callback_data="economy_1")
tk_slo_button.insert(dl_solo_1)

# Бюджет выше 4(menu)
# Колледжи
kit_button = InlineKeyboardMarkup(row_width=1)

Colledge_1 = InlineKeyboardButton(text="КИТ", callback_data="kit_1")
kit_button.insert(Colledge_1)

Colledge_2 = InlineKeyboardButton(text="ТК", callback_data="tk_1")
kit_button.insert(Colledge_2)

# Образовательные программы
programm_spo4_button = InlineKeyboardMarkup(row_width=1)

programm_spo_1 = InlineKeyboardButton(text="Сетевое и системное администрирование", callback_data="sis_admin_spo")
programm_spo4_button.insert(programm_spo_1)

programm_spo_2 = InlineKeyboardButton(text="Информационные системы и программирование", callback_data="ifo_sis_spo")
programm_spo4_button.insert(programm_spo_2)

programm_spo_3 = InlineKeyboardButton(text="Обеспечение информационной безопасности автоматизированных систем",
                                      callback_data="info_spo")
programm_spo4_button.insert(programm_spo_3)

# назад
back_spo_kit = InlineKeyboardMarkup(row_width=1)

back_kit_1 = InlineKeyboardButton(text="Назад", callback_data="back_kit_1")
back_spo_kit.insert(back_kit_1)

# Образовательная программа
programm_spo4tk_button = InlineKeyboardMarkup(row_width=1)

programm_tk_1 = InlineKeyboardButton(
    text="Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей", callback_data="technical_1")
programm_spo4tk_button.insert(programm_tk_1)

programm_tk_2 = InlineKeyboardButton(text="Технология металлообрабатывающего производства", callback_data="metal_1")
programm_spo4tk_button.insert(programm_tk_2)

programm_tk_3 = InlineKeyboardButton(text="Управление качеством продукции, процессов и услуг (по отраслям)",
                                     callback_data="quality_management_1")
programm_spo4tk_button.insert(programm_tk_3)
# Назад
back_spo_tk = InlineKeyboardMarkup(row_width=1)

back_tk_1 = InlineKeyboardButton(text="Назад", callback_data="back_tk_1")
back_spo_tk.insert(back_tk_1)

# Высшее
vibor_button = InlineKeyboardMarkup(row_width=1)

vibor_1 = InlineKeyboardButton(text="⭐️ Мат Рус Физ или ИКТ", callback_data="Mat")

vibor_button.insert(vibor_1)

vibor_3 = InlineKeyboardButton(text="⭐️ Мат Рус Хим", callback_data="Khemical")

vibor_button.insert(vibor_3)

# Мага
vibor_button_maga = InlineKeyboardMarkup(row_width=1)

vibor_maga_1 = InlineKeyboardButton(text="🔸 Очное", callback_data="Free_maga")

vibor_button_maga.insert(vibor_maga_1)

vibor_maga_2 = InlineKeyboardButton(text="🔸 Заочное", callback_data="night_maga")

vibor_button_maga.insert(vibor_maga_2)

vibor_maga_3 = InlineKeyboardButton(text="🔸 Целевое", callback_data="high_maga")

vibor_button_maga.insert(vibor_maga_3)

# Выбор мага или бак
menu_univer_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🔹 Бакалавриат"),
        KeyboardButton(text="🔹 Магистратура")
    ],
    [
        KeyboardButton(text="🔹 Среднее профессиональное образование")
    ],
    [
        KeyboardButton(text="🏛Главное меню🏛")
    ]
],
    resize_keyboard=True
)

# Выбор форму обучения
menu_Form_of_training_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔺 Очное", callback_data="full_time_training"),
        InlineKeyboardButton(text="🔺 Заочное", callback_data="Distance_learning"),
        InlineKeyboardButton(text="🔺 Целевое", callback_data="Targeted_training")
    ]
])

# Не было в прошлом году набора
menu_theend = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ВШПИТ", callback_data="VSHIP_end")
    ],
    [
        InlineKeyboardButton(text="ИАНТЭ", callback_data="IANT_end")
    ],
    [
        InlineKeyboardButton(text="ИАЭП", callback_data="IAAP_end")
    ],
    [
        InlineKeyboardButton(text="ИИЭиП", callback_data="IIAIP_end")
    ],
    [
        InlineKeyboardButton(text="🏛Главное меню🏛", callback_data="bb_yra")
    ]
])

# 300р в год
menu_one_300 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Посмотреть", callback_data="wie")
    ]
])
