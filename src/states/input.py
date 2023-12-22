from aiogram.fsm.state import StatesGroup, State


class Input(StatesGroup):
    choosing_subject = State()
    choosing_task = State()
    input_extrem = State()
    input_double_integral = State()
    input_linear_combination = State()
