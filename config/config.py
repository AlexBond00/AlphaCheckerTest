import os
from typing import Final

import pytz

BOT_TOKEN: Final[str] = "6644748119:AAEgxgWHQjRSM8Bm513KLvwTJZ2XhPCI-7s"

DEFAULT_TIMEZONE: Final = pytz.timezone("Europe/Moscow")

DB_CONFIG_FILE_PATH: Final[str] = os.path.join(
    os.path.dirname(__file__), "db_config.json")
