import sys

from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from Professor.utils.logger import LOGGER

# Initialize assistant (user client for voice calls)
assistant = Client(
    "ProfessorMusicAssistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_name=str(config.STRING_SESSION),
)

# Init PyTgCalls with the assistant client
pytgcalls = PyTgCalls(assistant)

# Export the client for use in other modules
clientbot = assistant

async def start():
    """
    Start the assistant client for voice calls
    """
    LOGGER.info("Starting Assistant Client")
    try:
        await assistant.start()
        await pytgcalls.start()
        LOGGER.info("Assistant Started Successfully")
    except Exception as e:
        LOGGER.error(f"Error starting assistant: {e}")
        sys.exit()

    # Get the assistant client info
    get_me = await assistant.get_me()
    LOGGER.info(f"Assistant Started as {get_me.first_name}")

    # Add the assistant client to the config clients list
    config.clients.append(assistant)

    return assistant, pytgcalls
