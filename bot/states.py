from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    register = State()
    debt = State()
