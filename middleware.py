from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from models.inspector_models import User


class ExceptionsMiddleware(BaseMiddleware):
    """Custom middleware to save messages in db."""
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        uid_list: list[int] = [user.uid for user in await User.all()]
        if event.from_user.id in uid_list:
            await handler(event, data)
