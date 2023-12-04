from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    """States during registration."""
    username = State()


class UpdateUserState(StatesGroup):
    wait_data = State()


class GetInfoClient(StatesGroup):
    wait_user_id = State()
