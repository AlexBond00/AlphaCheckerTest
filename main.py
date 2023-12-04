import asyncio
import json
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, Router
from tortoise import Tortoise
from config.json_parser import parse_json
from config.config import DB_CONFIG_FILE_PATH, BOT_TOKEN
from handlers import forwarding_message
from handlers.commands import start_command, get_info_command, update_command, \
    help_command

#  logger conf
path_file = os.path.dirname(os.path.abspath(__file__))
name_log: str = "/".join(
    [path_file, "logs", f"{str(datetime.now().date())}.log"])
logging.basicConfig(
    level=logging.INFO,
    filename=name_log,
    format="%(asctime)s %(levelname)s %(message)s"
)


async def init_tortoise():
    with open(DB_CONFIG_FILE_PATH) as f:
        json_data = json.load(f)
    parsed_json = parse_json(json_data)
    await Tortoise.init(config=parsed_json, use_tz=True)
    await Tortoise.generate_schemas(safe=True)


async def main():
    await init_tortoise()

    bots: list[Bot] = [Bot(token=BOT_TOKEN, parse_mode="HTML")]

    dp = Dispatcher()

    router = Router()

    router.include_router(help_command.router)
    router.include_router(start_command.router)
    router.include_router(get_info_command.router)
    router.include_router(update_command.router)
    router.include_router(forwarding_message.router)

    dp.include_router(router)

    await dp.start_polling(
        *bots, allowed_updates=[
            "message", "callback_query", "chat_member", "chat_join_request"])


if __name__ == "__main__":
    print("hello")
    asyncio.run(main())
