import os
import re
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

# Get basic info from environment variables
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", "!").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# Sudo users have full control over the bot
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

# Bot log channel
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

# Music downloader settings
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Professor Music Bot")
OWNER_ID = int(getenv("OWNER_ID", ""))

# Spotify integration
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# Start message
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/image.jpg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SANATANI_TECH")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/SANATANI_SUPPORT")

# Heroku settings (for self-updates)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# Bot behavior and technical settings
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True").lower() == "true"
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True").lower() == "true"
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False").lower() == "true"
YOUTUBE_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Language
LANGUAGE = getenv("LANGUAGE", "en")

# YouTube stream format, video quality
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SANATANI_TECH")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/SANATANI_SUPPORT")

# Duration limit for songs in seconds
DURATION_LIMIT = int(DURATION_LIMIT_MIN) * 60

# Complete server command for system control
BANNED_USERS = getenv("BANNED_USERS", "").split()

# Text for audio/video quality choices
QUALITY = getenv("QUALITY", "Best").lower()

# Command prefixes
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

# Bot owner/sudo user IDs
OWNER_ID.append(OWNER_ID) if OWNER_ID not in SUDO_USERS else None

# For multiple clients handling
clients = []
