from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    fullname = State()
    phone = State()
    confirm = State()