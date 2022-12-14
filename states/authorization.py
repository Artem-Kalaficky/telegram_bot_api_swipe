from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    language = State()
    login_or_register = State()


class Register(StatesGroup):
    email = State()
    password1 = State()
    password2 = State()
    first_name = State()
    last_name = State()
    complete = State()


class Login(StatesGroup):
    email = State()
    password = State()
    complete = State()


