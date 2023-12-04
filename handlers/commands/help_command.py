from aiogram import Router
from aiogram.filters import Command

from aiogram.types import Message

router = Router(name="help_command")


@router.message(Command("help"))
async def help_command(message: Message):
    """Help handler."""
    await message.answer(
        "/getinfo command to get all user records,\n"
        "/update to update user data in the database."
    )
