import os
from typing import Final

import pytz

BOT_TOKEN: Final[str] = "6489796599:AAGyUnbepH9PN_aE7VYcutmxtCw7Wwmhoek"

DEFAULT_TIMEZONE: Final = pytz.timezone("Europe/Moscow")

DB_CONFIG_FILE_PATH: Final[str] = os.path.join(
    os.path.dirname(__file__), "db_config.json")
