import asyncio
import os
import time
from datetime import datetime, timedelta
from typing import Union

import sys
from sys import version as pyver

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls

import config
from Professor.core.clientbot import clientbot
from Professor.core.dir import dirr
from Professor.utils.logger import LOGGER
from Professor.utils.database import database
from Professor.utils.decorators import language
from Professor.utils.inline import start_panel

# Initialize directories
dirr()

# Initialize clients
app = Client(
    "ProfessorBot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

# Initialize PyTgCalls client
pytgcalls = PyTgCalls(clientbot)

# Print startup message
print(f"""
⊰᯽⊱┈──╌❊╌──┈⊰᯽⊱
PROFESSOR MUSIC BOT STARTED SUCCESSFULLY
Python Version: {pyver.split()[0]}
Pyrogram Version: {pyrogram.__version__}
PyTgCalls Version: {pytgcalls.__version__}
⊰᯽⊱┈──╌❊╌──┈⊰᯽⊱
""")

# Bot command to check if it's running
@app.on_message(filters.command("start") & filters.private)
@language
async def start_command(client, message: Message, _):
    await message.reply_text(
        _["start_1"].format(message.from_user.mention, config.MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["S_B_1"],
                        url=f"https://t.me/{app.username}?startgroup=true",
                    ),
                    InlineKeyboardButton(
                        text=_["S_B_2"], url=config.SUPPORT_GROUP
                    ),
                ],
            ]
        ),
    )

# Bot command to show ping/latency
@app.on_message(filters.command("ping") & filters.group)
@language
async def ping_command(client, message: Message, _):
    start = time.time()
    response = await message.reply_text(_["ping_1"])
    end = time.time()
    resp = (end - start) * 1000
    await response.edit_text(_["ping_2"].format(resp))

# Start the bot
async def start_bot():
    # Initialize database
    await database.connect()

    try:
        # Start the bot client
        await app.start()

        # Start user client (for playing music in calls)
        await clientbot.start()

        # Start PyTgCalls
        await pytgcalls.start()

        # Load plugins
        from Professor.plugins import load_plugins
        await load_plugins()

        # Log startup message
        LOGGER.info("Professor Music Bot Started Successfully")
        LOGGER.info("Visit @SANATANI_TECH for updates")
    except Exception as e:
        LOGGER.error(f"Error starting bot: {e}")

# Run the bot
if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(start_bot())
