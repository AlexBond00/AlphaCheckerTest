from aiogram import Bot, Router
from aiogram.types import Message


router = Router(name="forward_message")


@router.message()
async def forward_message(message: Message, bot: Bot, *args, **kwargs):
    if message.forward_from:
        tg_id: int | None = message.forward_from.id
        await message.answer(f"Tg client id: {tg_id}")
    else:
        await message.answer(
            "In order to find out the client's tg id, "
            "you need to forward his message to this chat.")
