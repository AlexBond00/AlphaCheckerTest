from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.search_channel import search_channel
from models.inspector_models import UpdateInspector, User
from models.postback_models import Postback, Category
from states import UpdateUserState

router = Router(name="update_command")


@router.message(Command("update"))
async def update_command(message: Message, state: FSMContext, bot: Bot, *args, **kwargs):
    await state.clear()
    await message.answer(
        "Send it to me user_id, tg_id, channel_name separated by a space.\n"
        "Example: 5555 6666 F3"
    )
    await state.set_state(UpdateUserState.wait_data)


@router.message(UpdateUserState.wait_data)
async def get_info_by_client(message: Message, state: FSMContext):
    data_list: list[str] = message.text.split(" ")
    checker: bool = False
    inspector = await User.get(uid=message.from_user.id)

    if len(data_list) >= 2:
        if not (data_list[0].isdigit() and data_list[1].isdigit()):
            await message.answer(
                "You have entered an invalid value,\n"
                "the client's user id and tg id must contain only digits."
            )
            await state.clear()
            return

        user_id: int = int(data_list[0])
        tg_id: int = int(data_list[1])

        postback_list: list[Postback] = await Postback.filter(
            user_id=user_id,
            category__not=Category.REVENUE
        ).all()

        if postback_list:
            non_null_sub1: list[Postback] = await Postback.filter(
                user_id=user_id,
                sub1__not_isnull=True,
                category__not=Category.REVENUE
            ).all()

            if non_null_sub1:
                for postback in non_null_sub1:
                    if postback.sub1 != str(tg_id):
                        await message.answer(
                            "This user already has records with a filled-in sub1 "
                            "that does not match the tg_id that you sent."
                        )
                        await message.answer("Start over please!")
                        await state.clear()
                        return

            for postback in postback_list:
                if postback.sub1 is None:
                    await postback.update_from_dict(
                        {"sub1": tg_id}
                    )
                    await postback.save()
                    checker = True
                else:
                    pass

            if checker:
                await UpdateInspector.create(user=inspector)
                await search_channel(user_id)
                await message.answer("Updates are saved.")
            else:
                await message.answer("The data has already been filled in.")
        else:
            await message.answer("The user was not found by this user id.")
    else:
        await message.answer(
            "You have entered an invalid value, "
            "the client's user id must contain only digits.")
    await state.clear()
