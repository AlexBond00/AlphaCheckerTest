from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BufferedInputFile

from handlers.search_channel import search_channel
from models.inspector_models import GetInfoInspector, User
from models.postback_models import Postback, Category
from states import GetInfoClient

router = Router(name="getinfo_command")


@router.message(Command("getinfo"))
async def start_command(message: Message, state: FSMContext, bot: Bot, *args, **kwargs):
    await state.clear()
    await message.answer("Enter the client's user id.")
    await state.set_state(GetInfoClient.wait_user_id)


@router.message(GetInfoClient.wait_user_id)
async def get_telegram_id(message: Message, state: FSMContext, bot: Bot):
    print('Start handler')
    __tg_str_symbols_limit = 4096  # tg constant limit to send messages
    state_str: str = str()
    inspector: User = await User.get(uid=message.from_user.id)
    if message.text.isdigit():
        user_id = message.text
        postback_list: list[Postback] = await Postback.filter(
            user_id=user_id,
            category__not=Category.REVENUE,
        ).all()
        print(postback_list)
        await GetInfoInspector.create(user=inspector)
        if postback_list:
            for postback in postback_list:
                state_str += f"| {postback.partner} | " \
                             f"{postback.category} | " \
                             f"{postback.created_at} | " \
                             f"{postback.user_id} | " \
                             f"{postback.amount} | " \
                             f"{postback.sub1} | " \
                             f"{postback.sub5} |\n"
            if len(state_str) >= __tg_str_symbols_limit:
                bytes_str = bytes(state_str, "utf-8")
                document = BufferedInputFile(
                    file=bytes_str, filename='statistics.txt')
                await message.answer(
                    "Requested data is too large to be represented in one "
                    "message because of telegram policy.\n\n"
                    "Here is the file with requested statistics: \n"
                )
                await bot.send_document(
                    chat_id=message.from_user.id, document=document)
            else:
                await message.answer(
                    "Here are all postbacks about the user:\n\n"
                    "| partner | category | created_at | user_id "
                    "| amount | sub1 | sub5 |"
                )
                await message.answer(state_str)
                await search_channel(user_id)
        else:
            await message.answer("The user was not found by this user id.")
    else:
        await message.answer(
            "You have entered an invalid value, "
            "the client's user id must contain only digits.")
    await state.clear()
