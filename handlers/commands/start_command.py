from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from models.inspector_models import User
from states import RegisterState
from logger import alpha_checker_logger


router = Router(name="start_command")


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    """Start command. Registration and greetings."""
    alpha_checker_logger.critical("Test import critical!")
    # Check if user is in db
    user = await User.get_or_none(uid=message.from_user.id)
    if user:
        await message.answer(
            f"Welcome back, {user.username}! "
            "If you want some assistance type '/help'")
        return
    await message.answer(
        "You are not registered yet. Please follow simple steps "
        "to complete registration.\n"
        "Choose username: \n")
    await state.set_state(RegisterState.username)


@router.message(RegisterState.username)
async def registartion_get_username(message: Message, state: FSMContext):
    """Creates user with input data."""
    username_data = message.text
    # username validation
    if not username_data or len(username_data) > 100:
        await message.answer(
            "Please, input your username carefully. 100 symbols availible."
        )
    user = await User.get_or_none(username=username_data)
    if user:
        await message.answer(
            "This username is aready taken, please choose another one."
        )
        return
    name_data = {"username": message.text}
    name_data.update({"uid": message.from_user.id})
    await User.create(**name_data)
    await message.answer(
        "Your profile sucsessfully created!"
    )
    await state.clear()
