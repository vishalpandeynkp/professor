from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import config
from Professor.utils.decorators import language, check_blacklist
from Professor.utils.inline import start_panel
from Professor.utils.database import database

__module_name__ = "Start"

# Start command for private chats
@Client.on_message(filters.command(["start"]) & filters.private)
@language
@check_blacklist
async def start_private(client, message: Message, _):
    """
    Handle the /start command in private chats
    """
    await message.reply_text(
        _["start_1"].format(message.from_user.mention, config.MUSIC_BOT_NAME),
        reply_markup=start_panel(_),
    )

    # Add user to database
    await database.add_user(message.from_user.id)

# Start command for groups
@Client.on_message(filters.command(["start"]) & filters.group)
@language
@check_blacklist
async def start_group(client, message: Message, _):
    """
    Handle the /start command in group chats
    """
    await message.reply_text(
        _["start_1"].format(message.from_user.mention, config.MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["S_B_5"],
                        callback_data="help_command",
                    ),
                ],
            ]
        ),
    )

    # Add chat to database
    await database.add_chat(message.chat.id)

# Ping command to check bot's latency
@Client.on_message(filters.command(["ping"]))
@language
async def ping_command(client, message: Message, _):
    """
    Handle the /ping command to check bot response time
    """
    start = datetime.now()

    # Send the initial message
    response = await message.reply_text(_["ping_1"])

    # Calculate response time
    end = datetime.now()
    latency = (end - start).microseconds / 1000

    # Get uptime information
    uptime_seconds = int((datetime.now() - client.start_time).total_seconds())
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime = f"{days}d, {hours}h, {minutes}m, {seconds}s"

    # Reply with the ping result
    await response.edit_text(
        _["ping_2"].format(
            round(latency, 2),
            uptime,
            # System uptime (not implemented in this example)
            "N/A"
        )
    )
