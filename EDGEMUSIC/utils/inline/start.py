from pyrogram.types import InlineKeyboardButton

import config
from EDGEMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="Add Me", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="Help", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="Developer", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="Edge Bots", url=f"https://t.me/edgebots"),
        ]
    ]
    return buttons