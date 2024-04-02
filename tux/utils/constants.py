import json
import os
from pathlib import Path
from typing import Final

from dotenv import load_dotenv

load_dotenv()
config_file = Path("config/settings.json")
config = json.loads(config_file.read_text())


# defining json stuff so it can be pulled later down the file
class Constants:
    # Bot-related constants
    BOT_VERSION = "1.0.0"
    BOT_NAME = "Tux"
    BOT_SOURCE = "https://github.com/allthingslinux/tux"

    # Production constants
    PROD_TOKEN: Final[str] = os.getenv("PROD_TOKEN", "")
    PROD_PREFIX: Final[str] = os.getenv("PROD_PREFIX", "$")
    PROD_COG_IGNORE_LIST: Final[set[str]] = set(os.getenv("PROD_COG_IGNORE_LIST", "").split(","))

    # Staging constants
    STAGING = os.getenv("STAGING")
    STAGING_TOKEN: Final[str] = os.getenv("STAGING_TOKEN", "")
    STAGING_PREFIX: Final[str] = os.getenv("STAGING_PREFIX", ">")
    STAGING_COG_IGNORE_LIST: Final[set[str]] = set(
        os.getenv("STAGING_COG_IGNORE_LIST", "").split(",")
    )

    # Sentry-related constants
    SENTRY_URL: Final[str] = os.getenv("SENTRY_URL", "")

    # Channel constants
    CHANNELS: Final[dict[str, int]] = {
        "AUDIT": 1191472088695980083,
        "MOD": 1234567890,
        "GENERAL": 1234567890,
        "BOT": 1234567890,
    }

    # Color constants
    EMBED_STATE_COLORS: Final[dict[str, int]] = {
        "DEFAULT": 0xF2B033,
        "INFO": 0x00BFFF,
        "WARNING": 0xF67402,
        "ERROR": 0xFF0000,
        "SUCCESS": 0x55DD33,
        "DEBUG": 0x800080,
        "BLACK": 0x000000,
        "WHITE": 0xFFFFFF,
    }

    EMBED_STATE_ICONS: Final[dict[str, str]] = {
        "INFO": "https://cdn3.emoji.gg/emojis/3228-info.png",
        "WARNING": "https://cdn3.emoji.gg/emojis/3228-info.png",
        "ERROR": "https://cdn3.emoji.gg/emojis/3228-info.png",
        "SUCCESS": "https://cdn3.emoji.gg/emojis/3228-info.png",
    }

    # User ID Constants
    USER_IDS: Final[dict[str, int]] = {
        "ADMIN": config["Permissions"]["Admin"],
        "MOD": config["Permissions"]["Mod"],
        "JR MOD": config["Permissions"]["Jr_Mod"],
        "OWNER": config["Permissions"]["Owner"],
        "TESTING": config["Permissions"]["Testing"],
    }
    # Temp VC constants
    TEMPVC_CATEGORY_ID = os.getenv("TEMPVC_CATEGORY_ID")
    TEMPVC_CHANNEL_ID = os.getenv("TEMPVC_CHANNEL_ID")

    # Discord constants
    ACTION_ROW_MAX_ITEMS = 5
    SELECTS_MAX_OPTIONS = 25
    SELECT_MAX_NAME_LENGTH = 100
    CONTEXT_MENU_NAME_LENGTH = 32
    SLASH_CMD_NAME_LENGTH = 32
    SLASH_CMD_MAX_DESC_LENGTH = 100
    SLASH_CMD_MAX_OPTIONS = 25
    SLASH_OPTION_NAME_LENGTH = 100
    EMBED_MAX_NAME_LENGTH = 256
    EMBED_MAX_DESC_LENGTH = 4096
    EMBED_MAX_FIELDS = 25
    EMBED_TOTAL_MAX = 6000
    EMBED_FIELD_VALUE_LENGTH = 1024


"""
Constants for the bot.

Example:

from tux.utils.constants import Constants as CONST
print(CONST.BOT_NAME)
print(CONST.COLORS.INFO)
print(CONST.CHANNELS.AUDIT)
"""

CONST = Constants()
