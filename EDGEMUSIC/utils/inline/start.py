from pyrogram.types import InlineKeyboardButton

import config
from TGNMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍs", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="ᴇᴅɢᴇ ʙᴏᴛs", url=f"https://t.me/edgebots"),
        ]
    ]
    return buttons