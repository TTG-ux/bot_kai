from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    Text = State()


class Careitems(StatesGroup):
    item1 = State()


class Careitems_1(StatesGroup):
    itemi1 = State()


class text_one(StatesGroup):
    texit = State()
    texup = State()
    text_1 = State()
    text_2 = State()
    complite = State()


class khemical_1(StatesGroup):
    u_1 = State()


class test(StatesGroup):
    t_1 = State()
    t_2 = State()
    t_3 = State()
    t_4 = State()
