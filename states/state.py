from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    Text = State()
    LVL1 = State()


class Careitems(StatesGroup):
    item1 = State()


class Careitems_1(StatesGroup):
    itemi1 = State()


class text_one(StatesGroup):
    texit = State()
    texup = State()