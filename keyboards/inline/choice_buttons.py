from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

#Платное информация
#ИАЭП
baaip_platka = InlineKeyboardMarkup(row_widht=1)

pl_iiaap1 = InlineKeyboardButton(text = "Природообустройство и водопользование (заочное)", callback_data = "zao_1")

baaip_platka.insert(pl_iiaap1)

pl_iiaap2 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data = "zao_2")

baaip_platka.insert(pl_iiaap2)


#ИКТЗИ
platka_iktziii = InlineKeyboardMarkup(row_width=1)

pl_iktzi1 = InlineKeyboardButton(text = "Прикладная математика и информатика. Модели управления BigData", callback_data = "Big Data_iktzi")

platka_iktziii.insert(pl_iktzi1)


#Ирэт
platka_iret1 = InlineKeyboardMarkup(row_width=1)

iretpla_1 = InlineKeyboardButton(text = "Информационные сети, мобильная и оптическая связь, квантовые коммуникации", callback_data = "inforeti")

platka_iret1.insert(iretpla_1)
#хенд назад
back_buttonplatkair = InlineKeyboardMarkup(row_width=1)

pl_ir_112 = InlineKeyboardButton(text = "Назад", callback_data="pl_ir_11123")

back_buttonplatkair.insert(pl_ir_112)

#Темы вопросов
temi_1 = InlineKeyboardMarkup(row_width=1)

question_1 = InlineKeyboardButton(text = "Всё о документах при поступлении в КНИТУ-КАИ🗂", callback_data="doki_postupati")
temi_1.insert(question_1)

question_2 = InlineKeyboardButton(text = "Всё об поступлении📆", callback_data="postupat_vopros")
temi_1.insert(question_2)

question_3 = InlineKeyboardButton(text = "Всё об общежитии🏠", callback_data="obsgiaga_vopros")
temi_1.insert(question_3)

question_4 = InlineKeyboardButton(text = "Для иностранных граждан👥🇺🇸", callback_data="inostraci_vopros")
temi_1.insert(question_4)

question_5 = InlineKeyboardButton(text = "Всё о военной кафедре💂‍♀️", callback_data="war")
temi_1.insert(question_5)

#Клава Гумы
#2
#Выбор баллов
ViborOBS_button_angl = InlineKeyboardMarkup(row_width=1)

Obsnnivibor_1_angl = InlineKeyboardButton(text=">=140", callback_data="Obsiiaga_140_angl")

ViborOBS_button_angl.insert(Obsnnivibor_1_angl)


#Платка Обществознание
Obsagha_button1_angl = InlineKeyboardMarkup(row_width=1)

Obsehtvo_2_angl = InlineKeyboardButton(text="💰Платное обучение💰", callback_data="platka_obsix_1_angl")

Obsagha_button1_angl.insert(Obsehtvo_2_angl)

#Факультеты
IIaiP_button1_angl = InlineKeyboardMarkup(row_width=1)

takoi1fuck_1_angl = InlineKeyboardButton(text="Экономика и управление цифровым предприятием", callback_data="Akanomi_obsix_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_1_angl)

takoi1fuck_2_angl = InlineKeyboardButton(text = "Цифровые технологии в мировой экономике", callback_data="cifri_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_2_angl)

takoi1fuck_3_angl = InlineKeyboardButton(text = "Промышленная коммерция", callback_data="korporation_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_3_angl)

takoi1fuck_4_angl = InlineKeyboardButton(text = "Производственный менеджмент", callback_data="menedgment_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_4_angl)

takoi1fuck_5_angl = InlineKeyboardButton(text = "Управление проектами", callback_data="proekti_1_angl")

IIaiP_button1_angl.insert(takoi1fuck_5_angl)


#Хендлер "Назад"
back_button140OBS_angl = InlineKeyboardMarkup(row_width=1)

OBS_140_angl = InlineKeyboardButton(text = "Назад", callback_data="back_140_angl")

back_button140OBS_angl.insert(OBS_140_angl)


#1
#Выбор баллов
ViborOBS_button = InlineKeyboardMarkup(row_width=1)

Obsnnivibor_1 = InlineKeyboardButton(text=">=140", callback_data="Obsiiaga_140")

ViborOBS_button.insert(Obsnnivibor_1)


#Платка Обществознание
Obsagha_button1 = InlineKeyboardMarkup(row_width=1)

Obsehtvo_2 = InlineKeyboardButton(text="💰Платное обучение💰", callback_data="platka_obsix_1")

Obsagha_button1.insert(Obsehtvo_2)

#Факультеты
IIaiP_button1 = InlineKeyboardMarkup(row_width=1)

takoi1fuck_1 = InlineKeyboardButton(text="Экономика и управление цифровым предприятием", callback_data="Akanomi_obsix_1")

IIaiP_button1.insert(takoi1fuck_1)

takoi1fuck_2 = InlineKeyboardButton(text = "Цифровые технологии в мировой экономике", callback_data="cifri_1")

IIaiP_button1.insert(takoi1fuck_2)

takoi1fuck_3 = InlineKeyboardButton(text = "Промышленная коммерция", callback_data="korporation_1")

IIaiP_button1.insert(takoi1fuck_3)

takoi1fuck_4 = InlineKeyboardButton(text = "Производственный менеджмент", callback_data="menedgment_1")

IIaiP_button1.insert(takoi1fuck_4)

takoi1fuck_5 = InlineKeyboardButton(text = "Управление проектами", callback_data="proekti_1")

IIaiP_button1.insert(takoi1fuck_5)

takoi1fuck_6 = InlineKeyboardButton(text = "Управление человеческими ресурсами", callback_data="ludi_1")

IIaiP_button1.insert(takoi1fuck_6)

#Хендлер "Назад"
back_button140OBS = InlineKeyboardMarkup(row_width=1)

OBS_140 = InlineKeyboardButton(text = "Назад", callback_data="back_140")

back_button140OBS.insert(OBS_140)



#Клавиатура для МИР
ViborIKT_button = InlineKeyboardMarkup(row_width=1)

IKvibor_1 = InlineKeyboardButton(text="209", callback_data="IKKT_209")

ViborIKT_button.insert(IKvibor_1)

IKvibor_2 = InlineKeyboardButton(text="<=232", callback_data="IKKT_232")

ViborIKT_button.insert(IKvibor_2)

IKvibor_3 = InlineKeyboardButton(text="<=245", callback_data="IKKT_245")

ViborIKT_button.insert(IKvibor_3)

IKvibor_4 = InlineKeyboardButton(text="<>=247", callback_data="IKKT_247")

ViborIKT_button.insert(IKvibor_4)

#209
#Платка не платка в МИР
IKit_la = InlineKeyboardMarkup(row_width=1)

Kito_1 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_1")

IKit_la.insert(Kito_1)


#IRET
UIR_button = InlineKeyboardMarkup(row_width=1)

first_Iret = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret1")

UIR_button.insert(first_Iret)

#ИРЭТ ИКТ
Informat_IRET1_button = InlineKeyboardMarkup(row_width=1)

IRINF_1 = InlineKeyboardMarkup(text = "Информационные сети, мобильная и оптическая связь, квантовые коммуникации", callback_data = "IRINF_infoseti")

Informat_IRET1_button.insert(IRINF_1)

#232
#Платка не платка в МИР
IKit_la4 = InlineKeyboardMarkup(row_width=1)

Kito_14 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_4")

IKit_la4.insert(Kito_14)


#IRET и ИКТЗИ
boom_kar = InlineKeyboardMarkup(row_width=1)

first_Iret4 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret4")

boom_kar.insert(first_Iret4)

first_IKTZI4 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="this_is_iktzi4")

boom_kar.insert(first_IKTZI4)

#ИРЭТ ИКТ
Informat_IRET4_button = InlineKeyboardMarkup(row_width=1)

IRINF_4 = InlineKeyboardMarkup(text = "Информационные сети, мобильная и оптическая связь, квантовые коммуникации", callback_data = "IRINF_infoseti4")

Informat_IRET4_button.insert(IRINF_4)

#ИКТЗИ ИКТ
Informat_IKT4_button = InlineKeyboardMarkup(row_width=1)

IKTINF_4 = InlineKeyboardButton(text = "Робототехника и цифровая экономика", callback_data= "Robot_4")

Informat_IKT4_button.insert(IKTINF_4)

#Хендлер "Назад"

back_button232IKT = InlineKeyboardMarkup(row_width=1)

b_1232IKT = InlineKeyboardButton(text = "Назад", callback_data="back_232")

back_button232IKT.insert(b_1232IKT)


#245
#Платка не платка в МИР
IKit_la2 = InlineKeyboardMarkup(row_width=1)

Kito_11 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_2")

IKit_la2.insert(Kito_11)


#IRET(245)
UIR_button2 = InlineKeyboardMarkup(row_width=1)

first_Iret2 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret2")

UIR_button2.insert(first_Iret2)

first_IKTZI2 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="this_is_iktzi2")

UIR_button2.insert(first_IKTZI2)

#ИРЭТ ИКТ(245)
Informat_IRET2_button = InlineKeyboardMarkup(row_width=1)

IRINF_2 = InlineKeyboardMarkup(text = "Информационные сети, мобильная и оптическая связь, квантовые коммуникации", callback_data = "IRINF_infoseti2")

Informat_IRET2_button.insert(IRINF_2)

#ИКТЗИ ИКТ 245
Informat_IKT2_button = InlineKeyboardMarkup(row_width=1)

IKTINF_12 = InlineKeyboardButton(text = "Прикладная математика и информатика. Модели управления BigData", callback_data= "BigData_2")

Informat_IKT2_button.insert(IKTINF_12)

IKTINF_22 = InlineKeyboardButton(text = "Робототехника и цифровая экономика", callback_data= "Robot_2")

Informat_IKT2_button.insert(IKTINF_22)

#Хендлер "Назад"

back_button245IKT = InlineKeyboardMarkup(row_width=1)

b_1245IKT = InlineKeyboardButton(text = "Назад", callback_data="back_245")

back_button245IKT.insert(b_1245IKT)

#247
#Платка не платка в МИР(247)
IKit_la3 = InlineKeyboardMarkup(row_width=1)

Kito_13 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="informat_3")

IKit_la3.insert(Kito_13)


#IRET и ИКТЗИ(247)
UIR_button3 = InlineKeyboardMarkup(row_width=1)

first_Iret3 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="this_is_iret3")

UIR_button3.insert(first_Iret3)

first_IKTZI3 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="this_is_iktzi3")

UIR_button3.insert(first_IKTZI3)

#ИРЭТ ИКТ(247)
Informat_IRET3_button = InlineKeyboardMarkup(row_width=1)

IRINF_13 = InlineKeyboardMarkup(text = "Информационные сети, мобильная и оптическая связь, квантовые коммуникации", callback_data = "IRINF_infoseti3")

Informat_IRET3_button.insert(IRINF_13)

#ИКТЗИ ИКТ 247
Informat_IKT3_button = InlineKeyboardMarkup(row_width=1)

IKTINF_13 = InlineKeyboardButton(text = "Прикладная математика и информатика. Модели управления BigData", callback_data= "BigData_3")

Informat_IKT3_button.insert(IKTINF_13)

IKTINF_23 = InlineKeyboardButton(text = "Интеллектуальные информационные системы", callback_data= "intelectyal_3")

Informat_IKT3_button.insert(IKTINF_23)

IKTINF_33 = InlineKeyboardButton(text = "Робототехника и цифровая экономика", callback_data= "Robot_3")

Informat_IKT3_button.insert(IKTINF_33)

#Хендлер "Назад"

back_button247IKT = InlineKeyboardMarkup(row_width=1)

b_1247IKT = InlineKeyboardButton(text = "Назад", callback_data="back_247")

back_button247IKT.insert(b_1247IKT)


determined_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Высшее💼"),
        KeyboardButton(text="Среднее🎒")
    ],
    [
        KeyboardButton(text="❓Часто задаваемые вопросы❓")
    ],
    [
        KeyboardButton(text="❗Все важные ссылки❗")
    ],
    [
        KeyboardButton(text="☎️Контакты☎️"),
        KeyboardButton(text = '🚀Платное обучение🚀')
    ]
],
    resize_keyboard=True
)


#Среднее
vibor_sr_1 = InlineKeyboardMarkup(row_width=1)

vibor_sr_r_1 = InlineKeyboardButton(text = "⭐️ от 3 до 4", callback_data="var 3-4")
vibor_sr_1.insert(vibor_sr_r_1)

vibor_sr_r_2 = InlineKeyboardButton(text = "⭐️ от 4 и выше", callback_data="var 4+")
vibor_sr_1.insert(vibor_sr_r_2)

#Платка не платка от 3-4
platka_sr_1 = InlineKeyboardMarkup(row_width=1)

pl_sr_1 = InlineKeyboardButton(text = "Платное", callback_data="pl_sr_01")
platka_sr_1.insert(pl_sr_1)


#Образовательные программы
obr_platka_1 = InlineKeyboardMarkup(row_width=1)

obrazovka_1 = InlineKeyboardButton(text = "Экономика и бухгалтерский учёт(по отраслям)", callback_data="accountant")
obr_platka_1.insert(obrazovka_1)

obrazovka_2 = InlineKeyboardButton(text = "Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей(на базе 9кл.)", callback_data="auto_door")
obr_platka_1.insert(obrazovka_2)

obrazovka_3 = InlineKeyboardButton(text = "Управление качеством продукции, процессов и услуг(по отрослям) (на базе 9кл.)", callback_data="quality_management")
obr_platka_1.insert(obrazovka_3)

obrazovka_4 = InlineKeyboardButton(text = "Технология металлообрабатывающего производства (на базе 9кл.)", callback_data="Recycling+")
obr_platka_1.insert(obrazovka_4)

obrazovka_5 = InlineKeyboardButton(text = "Управление качеством продукции, процессов и услуг(по отраслям)(на базе 11кл.)", callback_data="management+")
obr_platka_1.insert(obrazovka_5)

obrazovka_6 = InlineKeyboardButton(text = "Обеспечение информационной безопасности автоматизированных систем", callback_data="autosistems")
obr_platka_1.insert(obrazovka_6)

#Назад
back_button_sr = InlineKeyboardMarkup(row_width=1)

bsr_1 = InlineKeyboardButton(text = "Назад", callback_data="bsr_11")

back_button_sr.insert(bsr_1)


#Высшее
vibor_button = InlineKeyboardMarkup(row_width=1)

vibor_1 = InlineKeyboardButton(text="⭐️ Математика Русский Физика", callback_data="Mat")

vibor_button.insert(vibor_1)

vibor_2 = InlineKeyboardButton(text = "⭐️ Математика Русский Информатика", callback_data="IkT")

vibor_button.insert(vibor_2)

vibor_3 = InlineKeyboardButton(text = "⭐️ Математика Русский Обществознание", callback_data="Obshaga")

vibor_button.insert(vibor_3)

vibor_4 = InlineKeyboardButton(text = "⭐️ Математика Русский Английский", callback_data="English")

vibor_button.insert(vibor_4)

# Клавиатура при вводе баллов

# 168
fiziks_168 = InlineKeyboardMarkup(row_width=1)

nizko_lari = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="Ruki_truki")

fiziks_168.insert(nizko_lari)


IAAAP_button = InlineKeyboardMarkup(row_width=1)

zao_iiap = InlineKeyboardButton(text="ИАЭП", callback_data="zaokha")

IAAAP_button.insert(zao_iiap)

freenizko_button = InlineKeyboardMarkup(row_width=1)

fiznizko_lir = InlineKeyboardButton(text="Стандартизация, сертификация и метрология (заочное)",
                                    callback_data="nemo")

freenizko_button.insert(fiznizko_lir)

# 202
fiziks_202 = InlineKeyboardMarkup(row_width=1)

fiz_202 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="loliiiii")

fiziks_202.insert(fiz_202)


#Факультеты
free_button = InlineKeyboardMarkup(row_width=1)

iaap_202 = InlineKeyboardButton(text = "ИАЭП", callback_data="iaps_202")

free_button.insert(iaap_202)

iretii_202 = InlineKeyboardButton(text="⚡💚ИРЭФ-ЦТ💚⚡", callback_data="iret_free")

free_button.insert(iretii_202)

#Хендлер ИРЭТ
ireti_button = InlineKeyboardMarkup(row_width=1)

lol_iret = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol_kek")

ireti_button.insert(lol_iret)

#Хендлер ИАЭП
iaap_button202 = InlineKeyboardMarkup(row_width=1)

i_1 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_202")

iaap_button202.insert(i_1)

#Хендлер "Назад"

back_button202 = InlineKeyboardMarkup(row_width=1)

b_1202 = InlineKeyboardButton(text = "Назад", callback_data="b_202")

back_button202.insert(b_1202)


#205
fiziks_205 = InlineKeyboardMarkup(row_width=1)

fiz_205 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_205")

fiziks_205.insert(fiz_205)


#Факультеты
free_button205 = InlineKeyboardMarkup(row_width=1)

f_1205 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1205")

free_button205.insert(f_1205)

f_2205 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1205")

free_button205.insert(f_2205)

#Хендлер ИАЭП
iaap_button205 = InlineKeyboardMarkup(row_width=1)

i_1205 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_205")

iaap_button205.insert(i_1205)

i_2205 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2205")

iaap_button205.insert(i_2205)

#Хендлер ИРЭТ
ireti_button205 = InlineKeyboardMarkup(row_width=1)

lol_iret1205 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_205")

ireti_button205.insert(lol_iret1205)

#Хендлер "Назад"
back_button205 = InlineKeyboardMarkup(row_width=1)

b_1205 = InlineKeyboardButton(text = "Назад", callback_data="b_205")

back_button205.insert(b_1205)



#206
fiziks_206 = InlineKeyboardMarkup(row_width=1)

fiz_206 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_206")

fiziks_206.insert(fiz_206)


#Факультеты
free_button206 = InlineKeyboardMarkup(row_width=1)

f_1206 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1206")

free_button206.insert(f_1206)

f_2206 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1206")

free_button206.insert(f_2206)

#ИАЭП Направления
iaap_button206 = InlineKeyboardMarkup(row_width=1)

i_1206 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_206")

iaap_button206.insert(i_1206)

i_2206 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2206")

iaap_button206.insert(i_2206)

i_3206 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3206")

iaap_button206.insert(i_3206)

#ИРЭТ Направления
ireti_button206 = InlineKeyboardMarkup(row_width=1)

lol_iret1206 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_206")

ireti_button206.insert(lol_iret1206)

#Хендлер "Назад"
back_button206 = InlineKeyboardMarkup(row_width=1)

b_1206 = InlineKeyboardButton(text = "Назад", callback_data="b_206")

back_button206.insert(b_1206)



#207

fiziks_207 = InlineKeyboardMarkup(row_width=1)

fiz_207 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_207")

fiziks_207.insert(fiz_207)


#Факультеты
free_button207 = InlineKeyboardMarkup(row_width=1)

f_1207 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1207")

free_button207.insert(f_1207)

f_2207 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1207")

free_button207.insert(f_2207)

#ИАЭП Направления
iaap_button207 = InlineKeyboardMarkup(row_width=1)

i_1207 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_207")

iaap_button207.insert(i_1207)

i_2207 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2207")

iaap_button207.insert(i_2207)

i_3207 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3207")

iaap_button207.insert(i_3207)

#ИРЭТ Направления
ireti_button207 = InlineKeyboardMarkup(row_width=1)

lol_iret1207 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_207")

ireti_button207.insert(lol_iret1207)

lol_iret2207 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_207")

ireti_button207.insert(lol_iret2207)

#Хендлер Назад
back_button207 = InlineKeyboardMarkup(row_width=1)

b_1207 = InlineKeyboardButton(text = "Назад", callback_data="b_207")

back_button207.insert(b_1207)



#208
fiziks_208 = InlineKeyboardMarkup(row_width=1)

fiz_208 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_208")

fiziks_208.insert(fiz_208)


#Факультеты
free_button208 = InlineKeyboardMarkup(row_width=1)

f_1208 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1208")

free_button208.insert(f_1208)

f_2208 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1208")

free_button208.insert(f_2208)

#ИАЭП Направления
iaap_button208 = InlineKeyboardMarkup(row_width=1)

i_1208 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_208")

iaap_button208.insert(i_1208)

i_2208 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2208")

iaap_button208.insert(i_2208)

i_3208 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3208")

iaap_button208.insert(i_3208)

i_4208 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4208")

iaap_button208.insert(i_4208)

#ИРЭТ Направления
ireti_button208 = InlineKeyboardMarkup(row_width=1)

lol_iret1208 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_208")

ireti_button208.insert(lol_iret1208)

lol_iret2208 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_208")

ireti_button208.insert(lol_iret2208)

#Хендлер Назад
back_button208 = InlineKeyboardMarkup(row_width=1)

b_1208 = InlineKeyboardButton(text = "Назад", callback_data="b_208")

back_button208.insert(b_1208)


#209
fiziks_209 = InlineKeyboardMarkup(row_width=1)

fiz_209 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_209")

fiziks_209.insert(fiz_209)


#Факультеты
free_button209 = InlineKeyboardMarkup(row_width=1)

f_1209 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1209")

free_button209.insert(f_1209)

f_2209 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1209")

free_button209.insert(f_2209)

#ИАЭП Направления
iaap_button209 = InlineKeyboardMarkup(row_width=1)

i_1209 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_209")

iaap_button209.insert(i_1209)

i_2209 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2209")

iaap_button209.insert(i_2209)

i_3209 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3209")

iaap_button209.insert(i_3209)

i_4209 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4209")

iaap_button209.insert(i_4209)

#ИРЭТ Направления
ireti_button209 = InlineKeyboardMarkup(row_width=1)

lol_iret1209 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_209")

ireti_button209.insert(lol_iret1209)

lol_iret2209 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_209")

ireti_button209.insert(lol_iret2209)

lol_button209 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_209")

ireti_button209.insert(lol_button209)

#Хендлер Назад
back_button209 = InlineKeyboardMarkup(row_width=1)

b_1209 = InlineKeyboardButton(text = "Назад", callback_data="b_209")

back_button209.insert(b_1209)


#210
fiziks_210 = InlineKeyboardMarkup(row_width=1)

fiz_210 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_210")

fiziks_210.insert(fiz_210)


#Факультеты
free_button210 = InlineKeyboardMarkup(row_width=1)

f_1210 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1210")

free_button210.insert(f_1210)

f_2210 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1210")

free_button210.insert(f_2210)

f_3210 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1210")

free_button210.insert(f_3210)

#ИАЭП Направления
iaap_button210 = InlineKeyboardMarkup(row_width=1)

i_1210 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_210")

iaap_button210.insert(i_1210)

i_2210 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2210")

iaap_button210.insert(i_2210)

i_3210 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3210")

iaap_button210.insert(i_3210)

i_4210 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4210")

iaap_button210.insert(i_4210)

i_5210 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5210")

iaap_button210.insert(i_5210)

#ИРЭТ Направления
ireti_button210 = InlineKeyboardMarkup(row_width=1)

lol_iret1210 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_210")

ireti_button210.insert(lol_iret1210)

lol_iret2210 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_210")

ireti_button210.insert(lol_iret2210)

lol_button210 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_210")

ireti_button210.insert(lol_button210)

#ИАНТЭ Направления
IANte_button210 = InlineKeyboardMarkup(row_width=1)

in_1210 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_210")

IANte_button210.insert(in_1210)

#Хендлер Назад
back_button210 = InlineKeyboardMarkup(row_width=1)

b_1210 = InlineKeyboardButton(text = "Назад", callback_data="b_210")

back_button210.insert(b_1210)

#211
fiziks_211 = InlineKeyboardMarkup(row_width=1)

fiz_211 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_211")

fiziks_211.insert(fiz_211)


#Факультеты
free_button211 = InlineKeyboardMarkup(row_width=1)

f_1211 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1211")

free_button211.insert(f_1211)

f_2211 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1211")

free_button211.insert(f_2211)

f_3211 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1211")

free_button211.insert(f_3211)

#ИАЭП Направления
iaap_button211 = InlineKeyboardMarkup(row_width=1)

i_1211 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_211")

iaap_button211.insert(i_1211)

i_2211 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2211")

iaap_button211.insert(i_2211)

i_3211 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3211")

iaap_button211.insert(i_3211)

i_4211 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4211")

iaap_button211.insert(i_4211)

i_5211 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5211")

iaap_button211.insert(i_5211)

I_6211 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6211")

iaap_button211.insert(I_6211)

#ИРЭТ Направления
ireti_button211 = InlineKeyboardMarkup(row_width=1)

lol_iret1211 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_211")

ireti_button211.insert(lol_iret1211)

lol_iret2211 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_211")

ireti_button211.insert(lol_iret2211)

lol_button211 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_211")

ireti_button211.insert(lol_button211)

#ИАНТЭ Направления
IANte_button211 = InlineKeyboardMarkup(row_width=1)

in_1211 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_211")

IANte_button211.insert(in_1211)

#Хендлер Назад
back_button211 = InlineKeyboardMarkup(row_width=1)

b_1211 = InlineKeyboardButton(text = "Назад", callback_data="b_211")

back_button211.insert(b_1211)


#220
fiziks_220 = InlineKeyboardMarkup(row_width=1)

fiz_220 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_220")

fiziks_220.insert(fiz_220)


#Факультеты
free_button220 = InlineKeyboardMarkup(row_width=1)

f_1220 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1220")

free_button220.insert(f_1220)

f_2220= InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1220")

free_button220.insert(f_2220)

f_3220 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1220")

free_button220.insert(f_3220)

#ИАЭП Направления
iaap_button220 = InlineKeyboardMarkup(row_width=1)

i_1220 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_220")

iaap_button220.insert(i_1220)

i_2220 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2220")

iaap_button220.insert(i_2220)

i_3220= InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3220")

iaap_button220.insert(i_3220)

i_4220 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4220")

iaap_button220.insert(i_4220)

i_5220 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5220")

iaap_button220.insert(i_5220)

I_6220 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6220")

iaap_button220.insert(I_6220)

#ИРЭТ Направления
ireti_button220 = InlineKeyboardMarkup(row_width=1)

lol_iret1220 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_220")

ireti_button220.insert(lol_iret1220)

lol_iret2220 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_220")

ireti_button220.insert(lol_iret2220)

lol_iret3220 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_220")

ireti_button220.insert(lol_iret3220)

lol_iret4220 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_220")

ireti_button220.insert(lol_iret4220)

lol_iret5220 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_220")

ireti_button220.insert(lol_iret5220)

#ИАНТЭ Направления
IANte_button220 = InlineKeyboardMarkup(row_width=1)

in_1220 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_220")

IANte_button220.insert(in_1220)

#Хендлер Назад
back_button220 = InlineKeyboardMarkup(row_width=1)

b_1220 = InlineKeyboardButton(text = "Назад", callback_data="b_220")

back_button220.insert(b_1220)


#226
fiziks_226 = InlineKeyboardMarkup(row_width=1)

fiz_226 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_226")

fiziks_226.insert(fiz_226)


#Факультеты
free_button226 = InlineKeyboardMarkup(row_width=1)

f_1226 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1226")

free_button226.insert(f_1226)

f_2226= InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1226")

free_button226.insert(f_2226)

f_3226 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1226")

free_button226.insert(f_3226)

#ИАЭП Направления
iaap_button226 = InlineKeyboardMarkup(row_width=1)

i_1226 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_226")

iaap_button226.insert(i_1226)

i_2226 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2226")

iaap_button226.insert(i_2226)

i_3226= InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3226")

iaap_button226.insert(i_3226)

i_4226 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4226")

iaap_button226.insert(i_4226)

i_5226 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5226")

iaap_button226.insert(i_5226)

I_6226 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6226")

iaap_button226.insert(I_6226)

I_7226 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7226")

iaap_button226.insert(I_7226)

#ИРЭТ Направления
ireti_button226 = InlineKeyboardMarkup(row_width=1)

lol_iret1226 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_226")

ireti_button226.insert(lol_iret1226)

lol_iret2226= InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_226")

ireti_button226.insert(lol_iret2226)

lol_iret3226 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_226")

ireti_button226.insert(lol_iret3226)

lol_iret4226 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_226")

ireti_button226.insert(lol_iret4226)

lol_iret5226 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_226")

ireti_button226.insert(lol_iret5226)

#ИАНТЭ Направления
IANte_button226 = InlineKeyboardMarkup(row_width=1)

in_1226 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_226")

IANte_button226.insert(in_1226)

#Хендлер Назад
back_button226 = InlineKeyboardMarkup(row_width=1)

b_1226 = InlineKeyboardButton(text = "Назад", callback_data="b_226")

back_button226.insert(b_1226)



#228
fiziks_228 = InlineKeyboardMarkup(row_width=1)

fiz_228 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_228")

fiziks_228.insert(fiz_228)


#Факультеты
free_button228 = InlineKeyboardMarkup(row_width=1)

f_4228 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1228")

free_button228.insert(f_4228)

f_1228 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1228")

free_button228.insert(f_1228)

f_2228 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1228")

free_button228.insert(f_2228)

f_3228 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1228")

free_button228.insert(f_3228)

#ФМФ Направления
FMF_button228 = InlineKeyboardMarkup(row_width=1)

fmf_1228 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1228")

FMF_button228.insert(fmf_1228)

#ИАЭП Направления
iaap_button228 = InlineKeyboardMarkup(row_width=1)

i_1228 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_228")

iaap_button228.insert(i_1228)

i_2228 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2228")

iaap_button228.insert(i_2228)

i_3228 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3228")

iaap_button228.insert(i_3228)

i_4228 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4228")

iaap_button228.insert(i_4228)

i_5228 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5228")

iaap_button228.insert(i_5228)

I_6228 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6228")

iaap_button228.insert(I_6228)

I_7228 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7228")

iaap_button228.insert(I_7228)

#ИРЭТ Направления
ireti_button228 = InlineKeyboardMarkup(row_width=1)

lol_iret1228 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_228")

ireti_button228.insert(lol_iret1228)

lol_iret2228 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_228")

ireti_button228.insert(lol_iret2228)

lol_iret3228 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_228")

ireti_button228.insert(lol_iret3228)

lol_iret4228 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_228")

ireti_button228.insert(lol_iret4228)

lol_iret5228 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_228")

ireti_button228.insert(lol_iret5228)

#ИАНТЭ Направления
IANte_button228 = InlineKeyboardMarkup(row_width=1)

in_1228 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_228")

IANte_button228.insert(in_1228)

#Хендлер Назад
back_button228 = InlineKeyboardMarkup(row_width=1)

b_1228 = InlineKeyboardButton(text = "Назад", callback_data="b_228")

back_button228.insert(b_1228)



#232
fiziks_232 = InlineKeyboardMarkup(row_width=1)

fiz_232 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_232")

fiziks_232.insert(fiz_232)


#Факультеты
free_button232 = InlineKeyboardMarkup(row_width=1)

f_5232 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1232")

free_button232.insert(f_5232)

f_4232 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1232")

free_button232.insert(f_4232)

f_1232= InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1232")

free_button232.insert(f_1232)

f_2232 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1232")

free_button232.insert(f_2232)

f_3232 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1232")

free_button232.insert(f_3232)

#ИКЗИ Направления
IKZI_button232 = InlineKeyboardMarkup(row_width=1)

Iktzi_1232 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1232")

IKZI_button232.insert(Iktzi_1232)

#ФМФ Направления
FMF_button232 = InlineKeyboardMarkup(row_width=1)

fmf_1232 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1232")

FMF_button232.insert(fmf_1232)

#ИАЭП Направления
iaap_button232 = InlineKeyboardMarkup(row_width=1)

i_1232 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_232")

iaap_button232.insert(i_1232)

i_2232 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2232")

iaap_button232.insert(i_2232)

i_3232= InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3232")

iaap_button232.insert(i_3232)

i_4232 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4232")

iaap_button232.insert(i_4232)

i_5232= InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5232")

iaap_button232.insert(i_5232)

I_6232 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6232")

iaap_button232.insert(I_6232)

I_7232 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7232")

iaap_button232.insert(I_7232)

#ИРЭТ Направления
ireti_button232 = InlineKeyboardMarkup(row_width=1)

lol_iret1232= InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_232")

ireti_button232.insert(lol_iret1232)

lol_iret2232 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_232")

ireti_button232.insert(lol_iret2232)

lol_iret3232 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_232")

ireti_button232.insert(lol_iret3232)

lol_iret4232 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_232")

ireti_button232.insert(lol_iret4232)

lol_iret5232 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_232")

ireti_button232.insert(lol_iret5232)

#ИАНТЭ Направления
IANte_button232 = InlineKeyboardMarkup(row_width=1)

in_1232 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_232")

IANte_button232.insert(in_1232)

#Хендлер Назад
back_button232 = InlineKeyboardMarkup(row_width=1)

b_1232 = InlineKeyboardButton(text = "Назад", callback_data="b_232")

back_button232.insert(b_1232)



#233
fiziks_233 = InlineKeyboardMarkup(row_width=1)

fiz_233 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_233")

fiziks_233.insert(fiz_233)


#Факультеты
free_button233 = InlineKeyboardMarkup(row_width=1)

f_5233 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1233")

free_button233.insert(f_5233)

f_4233 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1233")

free_button233.insert(f_4233)

f_1233 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1233")

free_button233.insert(f_1233)

f_2233 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1233")

free_button233.insert(f_2233)

f_3233 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1233")

free_button233.insert(f_3233)

#ИКЗИ Направления
IKZI_button233 = InlineKeyboardMarkup(row_width=1)

Iktzi_1233 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1233")

IKZI_button233.insert(Iktzi_1233)

Iktzi_2233 = InlineKeyboardButton(text = "Программирование и администратирование компьютерных систем", callback_data="proga_1233")

IKZI_button233.insert(Iktzi_2233)

#ФМФ Направления
FMF_button233 = InlineKeyboardMarkup(row_width=1)

fmf_1233 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1233")

FMF_button233.insert(fmf_1233)

#ИАЭП Направления
iaap_button233 = InlineKeyboardMarkup(row_width=1)

i_1233 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_233")

iaap_button233.insert(i_1233)

i_2233 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2233")

iaap_button233.insert(i_2233)

i_3233 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3233")

iaap_button233.insert(i_3233)

i_4233 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4233")

iaap_button233.insert(i_4233)

i_5233= InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5233")

iaap_button233.insert(i_5233)

I_6233 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6233")

iaap_button233.insert(I_6233)

I_7233 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7233")

iaap_button233.insert(I_7233)

#ИРЭТ Направления
ireti_button233 = InlineKeyboardMarkup(row_width=1)

lol_iret1233= InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_233")

ireti_button233.insert(lol_iret1233)

lol_iret2233 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_233")

ireti_button233.insert(lol_iret2233)

lol_iret3233 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_233")

ireti_button233.insert(lol_iret3233)

lol_iret4233 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_233")

ireti_button233.insert(lol_iret4233)

lol_iret5233 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_233")

ireti_button233.insert(lol_iret5233)

#ИАНТЭ Направления
IANte_button233 = InlineKeyboardMarkup(row_width=1)

in_1233 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_233")

IANte_button233.insert(in_1233)

#Хендлер Назад
back_button233 = InlineKeyboardMarkup(row_width=1)

b_1233 = InlineKeyboardButton(text = "Назад", callback_data="b_233")

back_button233.insert(b_1233)



#235
fiziks_235 = InlineKeyboardMarkup(row_width=1)

fiz_235 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_235")

fiziks_235.insert(fiz_235)


#Факультеты
free_button235 = InlineKeyboardMarkup(row_width=1)

f_5235 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1235")

free_button235.insert(f_5235)

f_4235 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1235")

free_button235.insert(f_4235)

f_1235 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1235")

free_button235.insert(f_1235)

f_2235 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1235")

free_button235.insert(f_2235)

f_3235 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1235")

free_button235.insert(f_3235)

#ИКЗИ Направления
IKZI_button235 = InlineKeyboardMarkup(row_width=1)

Iktzi_1235 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1235")

IKZI_button235.insert(Iktzi_1235)

Iktzi_2235 = InlineKeyboardButton(text = "Программирование и администратирование компьютерных систем", callback_data="proga_1235")

IKZI_button235.insert(Iktzi_2235)

Iktzi_3235 = InlineKeyboardButton(text = "Информационная безопасность", callback_data="infobez_1235")

IKZI_button235.insert(Iktzi_3235)

#ФМФ Направления
FMF_button235 = InlineKeyboardMarkup(row_width=1)

fmf_1235 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1235")

FMF_button235.insert(fmf_1235)

#ИАЭП Направления
iaap_button235 = InlineKeyboardMarkup(row_width=1)

i_1235 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_235")

iaap_button235.insert(i_1235)

i_2235 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2235")

iaap_button235.insert(i_2235)

i_3235 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3235")

iaap_button235.insert(i_3235)

i_4235 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4235")

iaap_button235.insert(i_4235)

i_5235 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5235")

iaap_button235.insert(i_5235)

I_6235 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6235")

iaap_button235.insert(I_6235)

I_7235 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7235")

iaap_button235.insert(I_7235)

#ИРЭТ Направления
ireti_button235 = InlineKeyboardMarkup(row_width=1)

lol_iret1235 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_235")

ireti_button235.insert(lol_iret1235)

lol_iret2235 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_235")

ireti_button235.insert(lol_iret2235)

lol_iret3235 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_235")

ireti_button235.insert(lol_iret3235)

lol_iret4235 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_235")

ireti_button235.insert(lol_iret4235)

lol_iret5235 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_235")

ireti_button235.insert(lol_iret5235)

#ИАНТЭ Направления
IANte_button235 = InlineKeyboardMarkup(row_width=1)

in_1235 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_235")

IANte_button235.insert(in_1235)

#Хендлер Назад
back_button235 = InlineKeyboardMarkup(row_width=1)

b_1235 = InlineKeyboardButton(text = "Назад", callback_data="b_235")

back_button235.insert(b_1235)



#240
fiziks_240 = InlineKeyboardMarkup(row_width=1)

fiz_240 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_240")

fiziks_240.insert(fiz_240)


#Факультеты
free_button240 = InlineKeyboardMarkup(row_width=1)

f_5240 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1240")

free_button240.insert(f_5240)

f_4240 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1240")

free_button240.insert(f_4240)

f_1240 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1240")

free_button240.insert(f_1240)

f_2240 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1240")

free_button240.insert(f_2240)

f_3240 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1240")

free_button240.insert(f_3240)

#ИКЗИ Направления
IKZI_button240 = InlineKeyboardMarkup(row_width=1)

Iktzi_1240 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1240")

IKZI_button240.insert(Iktzi_1240)

Iktzi_2240 = InlineKeyboardButton(text = "Программирование и администратирование компьютерных систем", callback_data="proga_1240")

IKZI_button240.insert(Iktzi_2240)

Iktzi_3240 = InlineKeyboardButton(text = "Информационная безопасность", callback_data="infobez_1240")

IKZI_button240.insert(Iktzi_3240)

#ФМФ Направления
FMF_button240 = InlineKeyboardMarkup(row_width=1)

fmf_1240 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1240")

FMF_button240.insert(fmf_1240)

fmf_2240 = InlineKeyboardButton(text = "Наноинженерия", callback_data= "nano_1240")

FMF_button240.insert(fmf_2240)

#ИАЭП Направления
iaap_button240 = InlineKeyboardMarkup(row_width=1)

i_1240 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_240")

iaap_button240.insert(i_1240)

i_2240 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2240")

iaap_button240.insert(i_2240)

i_3240 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3240")

iaap_button240.insert(i_3240)

i_4240 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4240")

iaap_button240.insert(i_4240)

i_5240 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5240")

iaap_button240.insert(i_5240)

I_6240 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6240")

iaap_button240.insert(I_6240)

I_7240 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7240")

iaap_button240.insert(I_7240)

#ИРЭТ Направления
ireti_button240 = InlineKeyboardMarkup(row_width=1)

lol_iret1240 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_240")

ireti_button240.insert(lol_iret1240)

lol_iret2240 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_240")

ireti_button240.insert(lol_iret2240)

lol_iret3240 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_240")

ireti_button240.insert(lol_iret3240)

lol_iret4240 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_240")

ireti_button240.insert(lol_iret4240)

lol_iret5240 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_240")

ireti_button240.insert(lol_iret5240)

#ИАНТЭ Направления
IANte_button240 = InlineKeyboardMarkup(row_width=1)

in_1240 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_240")

IANte_button240.insert(in_1240)

#Хендлер Назад
back_button240 = InlineKeyboardMarkup(row_width=1)

b_1240 = InlineKeyboardButton(text = "Назад", callback_data="b_240")

back_button240.insert(b_1240)



#241
fiziks_241 = InlineKeyboardMarkup(row_width=1)

fiz_241 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_241")

fiziks_241.insert(fiz_241)


#Факультеты
free_button241 = InlineKeyboardMarkup(row_width=1)

f_5241 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1241")

free_button241.insert(f_5241)

f_4241 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1241")

free_button241.insert(f_4241)

f_1241 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1241")

free_button241.insert(f_1241)

f_2241 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1241")

free_button241.insert(f_2241)

f_3241 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1241")

free_button241.insert(f_3241)

#ИКЗИ Направления
IKZI_button241 = InlineKeyboardMarkup(row_width=1)

Iktzi_1241 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1241")

IKZI_button241.insert(Iktzi_1241)

Iktzi_2241 = InlineKeyboardButton(text = "Программирование и администратирование компьютерных систем", callback_data="proga_1241")

IKZI_button241.insert(Iktzi_2241)

Iktzi_3241 = InlineKeyboardButton(text = "Информационная безопасность", callback_data="infobez_1241")

IKZI_button241.insert(Iktzi_3241)

#ФМФ Направления
FMF_button241 = InlineKeyboardMarkup(row_width=1)

fmf_1241 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1241")

FMF_button241.insert(fmf_1241)

fmf_2241 = InlineKeyboardButton(text = "Наноинженерия", callback_data= "nano_1241")

FMF_button241.insert(fmf_2241)

fmf_3241 = InlineKeyboardButton(text = "Лазерные технологии и 3D-прототипирование", callback_data= "lazer_1241")

FMF_button241.insert(fmf_3241)

#ИАЭП Направления
iaap_button241 = InlineKeyboardMarkup(row_width=1)

i_1241 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_241")

iaap_button241.insert(i_1241)

i_2241 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2241")

iaap_button241.insert(i_2241)

i_3241 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3241")

iaap_button241.insert(i_3241)

i_4241 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4241")

iaap_button241.insert(i_4241)

i_5241 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5241")

iaap_button241.insert(i_5241)

I_6241 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6241")

iaap_button241.insert(I_6241)

I_7241 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7241")

iaap_button241.insert(I_7241)

#ИРЭТ Направления
ireti_button241 = InlineKeyboardMarkup(row_width=1)

lol_iret1241 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_241")

ireti_button241.insert(lol_iret1241)

lol_iret2241 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_241")

ireti_button241.insert(lol_iret2241)

lol_iret3241 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_241")

ireti_button241.insert(lol_iret3241)

lol_iret4241 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_241")

ireti_button241.insert(lol_iret4241)

lol_iret5241 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_241")

ireti_button241.insert(lol_iret5241)

#ИАНТЭ Направления
IANte_button241 = InlineKeyboardMarkup(row_width=1)

in_1241 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_241")

IANte_button241.insert(in_1241)

#Хендлер Назад
back_button241 = InlineKeyboardMarkup(row_width=1)

b_1241 = InlineKeyboardButton(text = "Назад", callback_data="b_241")

back_button241.insert(b_1241)



#250
fiziks_250 = InlineKeyboardMarkup(row_width=1)

fiz_250 = InlineKeyboardButton(text="🆓бюджет🆓", callback_data="lol1_250")

fiziks_250.insert(fiz_250)


#Факультеты
free_button250 = InlineKeyboardMarkup(row_width=1)

f_5250 = InlineKeyboardButton(text = "ИКТЗИ", callback_data="IKTZI_1250")

free_button250.insert(f_5250)

f_4250 = InlineKeyboardButton(text = "ФМФ", callback_data="FMF_1250")

free_button250.insert(f_4250)

f_1250 = InlineKeyboardButton(text = "ИАЭП", callback_data="Ia_1250")

free_button250.insert(f_1250)

f_2250 = InlineKeyboardButton(text = "⚡💚ИРЭФ-ЦТ💚⚡", callback_data="Ir_1250")

free_button250.insert(f_2250)

f_3250 = InlineKeyboardButton(text = "ИАНТЭ", callback_data="IAN_1250")

free_button250.insert(f_3250)

#ИКЗИ Направления
IKZI_button250 = InlineKeyboardMarkup(row_width=1)

Iktzi_1250 = InlineKeyboardButton(text = "Защита информации в компьютерных сетях", callback_data="secr_1250")

IKZI_button250.insert(Iktzi_1250)

Iktzi_2250 = InlineKeyboardButton(text = "Программирование и администратирование компьютерных систем", callback_data="proga_1250")

IKZI_button250.insert(Iktzi_2250)

Iktzi_3250 = InlineKeyboardButton(text = "Информационная безопасность", callback_data="infobez_1250")

IKZI_button250.insert(Iktzi_3250)

Iktzi_4250 = InlineKeyboardButton(text = "Программная инженерия", callback_data= "progas_1250")

IKZI_button250.insert(Iktzi_4250)

#ФМФ Направления
FMF_button250 = InlineKeyboardMarkup(row_width=1)

fmf_1250 = InlineKeyboardButton(text = "Современные плазменные технологии", callback_data="plazma_1250")

FMF_button250.insert(fmf_1250)

fmf_2250 = InlineKeyboardButton(text = "Наноинженерия", callback_data= "nano_1250")

FMF_button250.insert(fmf_2250)

fmf_3250 = InlineKeyboardButton(text = "Лазерные технологии и 3D-прототипирование", callback_data= "lazer_1250")

FMF_button250.insert(fmf_3250)

#ИАЭП Направления
iaap_button250 = InlineKeyboardMarkup(row_width=1)

i_1250 = InlineKeyboardButton(text = "Стандартизация, сертификация и метрология (заочное)", callback_data="Ia_250")

iaap_button250.insert(i_1250)

i_2250 = InlineKeyboardButton(text = "Оптико-электронные системы", callback_data="ia_2250")

iaap_button250.insert(i_2250)

i_3250 = InlineKeyboardButton(text = "Управление беспилотными летательными аппаратами. Интеллектульные технические системы. Робототехника", callback_data="ia_3250")

iaap_button250.insert(i_3250)

i_4250 = InlineKeyboardButton(text = "Информационно-измерительные системы", callback_data="ia_4250")

iaap_button250.insert(i_4250)

i_5250 = InlineKeyboardButton(text = "Инженерная экология. Защита в чрезвычайных ситуациях", callback_data="ia_5250")

iaap_button250.insert(i_5250)

I_6250 = InlineKeyboardButton(text = "Электрооборудование предприятий, летательных аппаратов и автомобилей", callback_data="ia_6250")

iaap_button250.insert(I_6250)

I_7250 = InlineKeyboardButton(text = "Управление качеством", callback_data="ia_7250")

iaap_button250.insert(I_7250)

#ИРЭТ Направления
ireti_button250 = InlineKeyboardMarkup(row_width=1)

lol_iret1250 = InlineKeyboardButton(text="Инфокоммуникационные системы и их информационная защита", callback_data="lol11_250")

ireti_button250.insert(lol_iret1250)

lol_iret2250 = InlineKeyboardButton(text = "Электроника, микросистемная техника", callback_data="lol[1]_250")

ireti_button250.insert(lol_iret2250)

lol_iret3250 = InlineKeyboardButton(text = "Интеллектуальная радиоэлектроника и фотоника, встроенные системы, интернет вещей", callback_data="lol[2]_250")

ireti_button250.insert(lol_iret3250)

lol_iret4250 = InlineKeyboardButton(text = "Конструирование и технология электронных средств", callback_data="lol[3]_250")

ireti_button250.insert(lol_iret4250)

lol_iret5250 = InlineKeyboardButton(text = "Системы передачи и обработки информации, управления, навигации и радиоэлектронной борьбы", callback_data="lol[4]_250")

ireti_button250.insert(lol_iret5250)

#ИАНТЭ Направления
IANte_button250 = InlineKeyboardMarkup(row_width=1)

in_1250 = InlineKeyboardButton(text = "Энерго-и ресурсоэффективные технологии", callback_data="ener_250")

IANte_button250.insert(in_1250)

#Хендлер Назад
back_button250 = InlineKeyboardMarkup(row_width=1)

b_1250 = InlineKeyboardButton(text = "Назад", callback_data="b_250")

back_button250.insert(b_1250)


