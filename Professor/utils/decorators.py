import asyncio
from functools import wraps
from typing import Callable, Union

from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, CallbackQuery

import config
from Professor.utils.database import database
from Professor.utils.logger import LOGGER
from Professor.lang import get_string

# Load strings in memory for faster access
strings = {}

def language(func: Callable) -> Callable:
    """
    Decorator to load the language for the command
    and pass it to the function as the third argument
    """
    @wraps(func)
    async def wrapper(client, message: Union[Message, CallbackQuery], *args, **kwargs):
        try:
            # Check if the message is a callback query or a regular message
            chat_id = message.chat.id if isinstance(message, Message) else message.message.chat.id

            # Load language for this chat
            language = await database.get_lang(chat_id)

            # Get language strings dictionary
            if language not in strings:
                strings[language] = get_string(language)

            # Call the function with language strings
            return await func(client, message, strings[language], *args, **kwargs)
        except Exception as e:
            LOGGER.error(f"Error in language decorator: {e}")
            # Fallback to English if any error occurs
            if "en" not in strings:
                strings["en"] = get_string("en")
            return await func(client, message, strings["en"], *args, **kwargs)
    return wrapper

def check_blacklist(func: Callable) -> Callable:
    """
    Decorator to check if a user is blacklisted
    and prevent them from using the bot
    """
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        # Skip this check for sudo users
        if message.from_user.id in config.SUDO_USERS:
            return await func(client, message, *args, **kwargs)

        # Check if user is blacklisted
        is_blacklisted = await database.is_blacklisted(message.from_user.id)
        if is_blacklisted:
            return  # Silently ignore blacklisted users

        return await func(client, message, *args, **kwargs)
    return wrapper

def sudo_users_only(func: Callable) -> Callable:
    """
    Decorator to allow only sudo users to use
    certain commands
    """
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        user_id = message.from_user.id

        # Allow admin users from config and database
        if user_id in config.SUDO_USERS or await database.is_sudo(user_id):
            return await func(client, message, *args, **kwargs)

        # Send a message if unauthorized
        await message.reply_text("⚠️ You are not authorized to use this command!")
        return
    return wrapper

def errors(func: Callable) -> Callable:
    """
    Error handling decorator for command handlers
    """
    @wraps(func)
    async def wrapper(client, message: Union[Message, CallbackQuery], *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except FloodWait as e:
            # Wait in case of flood wait and retry
            await asyncio.sleep(e.x + 5)
            return await func(client, message, *args, **kwargs)
        except MessageNotModified:
            # Ignore this error as it's harmless
            pass
        except Exception as e:
            LOGGER.error(f"Error in {func.__name__}: {e}")
            # Notify the user of the error
            chat_id = message.chat.id if isinstance(message, Message) else message.message.chat.id
            err_msg = f"Error: {type(e).__name__}: {e}"

            try:
                if isinstance(message, Message):
                    await message.reply_text(err_msg)
                else:  # CallbackQuery
                    await message.message.reply_text(err_msg)
            except:
                pass
    return wrapper
