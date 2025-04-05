import asyncio
import time
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

import config
from Professor.utils.logger import LOGGER


class Database:
    """MongoDB Database class for storing user preferences, chat settings, etc."""

    def __init__(self):
        self.client = None
        self.db = None
        self.connected = False
        self.connection_retry_count = 0
        self.max_retries = 5

    async def connect(self):
        """Connect to MongoDB database"""
        if not config.MONGO_DB_URI:
            LOGGER.error("No MongoDB URI provided. Skipping database connection.")
            return

        try:
            LOGGER.info("Connecting to MongoDB...")
            self.client = AsyncIOMotorClient(config.MONGO_DB_URI)
            await self.client.admin.command('ping')  # Test connection

            self.db = self.client.professor_music
            self.connected = True
            LOGGER.info("Connected to MongoDB successfully")

            # Initialize collections
            self.chats = self.db.chats
            self.users = self.db.users
            self.playlists = self.db.playlists
            self.blacklist = self.db.blacklisted
            self.language = self.db.language
            self.sudoers = self.db.sudoers

            # Ensure indexes for faster queries
            await self.users.create_index("user_id")
            await self.chats.create_index("chat_id")
            await self.playlists.create_index("user_id")
            await self.blacklist.create_index("user_id")
            await self.language.create_index("chat_id")

        except ServerSelectionTimeoutError:
            if self.connection_retry_count < self.max_retries:
                self.connection_retry_count += 1
                LOGGER.warning(f"Failed to connect to MongoDB. Retrying... ({self.connection_retry_count}/{self.max_retries})")
                await asyncio.sleep(5)
                await self.connect()
            else:
                LOGGER.error("Failed to connect to MongoDB after multiple attempts.")
        except Exception as e:
            LOGGER.error(f"Error connecting to MongoDB: {e}")

    async def add_chat(self, chat_id: int):
        """Add a chat to the database"""
        if not self.connected:
            return

        is_chat = await self.chats.find_one({"chat_id": chat_id})
        if not is_chat:
            await self.chats.insert_one({"chat_id": chat_id, "is_active": True})
            return True
        return False

    async def remove_chat(self, chat_id: int):
        """Remove a chat from the database"""
        if not self.connected:
            return

        is_chat = await self.chats.find_one({"chat_id": chat_id})
        if is_chat:
            await self.chats.delete_one({"chat_id": chat_id})
            return True
        return False

    async def add_user(self, user_id: int):
        """Add a user to the database"""
        if not self.connected:
            return

        is_user = await self.users.find_one({"user_id": user_id})
        if not is_user:
            # Current timestamp for last seen
            now = int(time.time())
            await self.users.insert_one({
                "user_id": user_id,
                "last_seen": now,
                "is_blacklisted": False,
                "language": "en",
            })
            return True
        return False

    async def get_lang(self, chat_id: int) -> str:
        """Get language setting for a chat"""
        if not self.connected:
            return "en"

        chat = await self.language.find_one({"chat_id": chat_id})
        if not chat:
            await self.language.insert_one({"chat_id": chat_id, "language": "en"})
            return "en"
        return chat["language"]

    async def set_lang(self, chat_id: int, language: str):
        """Set language for a chat"""
        if not self.connected:
            return

        await self.language.update_one(
            {"chat_id": chat_id},
            {"$set": {"language": language}},
            upsert=True
        )

    async def blacklist_user(self, user_id: int):
        """Blacklist a user"""
        if not self.connected:
            return

        is_blacklisted = await self.blacklist.find_one({"user_id": user_id})
        if not is_blacklisted:
            await self.blacklist.insert_one({"user_id": user_id})
            return True
        return False

    async def whitelist_user(self, user_id: int):
        """Remove a user from blacklist"""
        if not self.connected:
            return

        is_blacklisted = await self.blacklist.find_one({"user_id": user_id})
        if is_blacklisted:
            await self.blacklist.delete_one({"user_id": user_id})
            return True
        return False

    async def is_blacklisted(self, user_id: int) -> bool:
        """Check if a user is blacklisted"""
        if not self.connected:
            return False

        is_blacklisted = await self.blacklist.find_one({"user_id": user_id})
        return bool(is_blacklisted)

    async def is_sudo(self, user_id: int) -> bool:
        """Check if a user is in sudo users list"""
        if not self.connected:
            return user_id in config.SUDO_USERS

        user = await self.sudoers.find_one({"user_id": user_id})
        if user:
            return True
        return user_id in config.SUDO_USERS

    async def add_sudo(self, user_id: int):
        """Add a user to sudo users list"""
        if not self.connected:
            return

        is_sudo = await self.sudoers.find_one({"user_id": user_id})
        if not is_sudo:
            await self.sudoers.insert_one({"user_id": user_id})
            return True
        return False

    async def remove_sudo(self, user_id: int):
        """Remove a user from sudo users list"""
        if not self.connected:
            return

        is_sudo = await self.sudoers.find_one({"user_id": user_id})
        if is_sudo:
            await self.sudoers.delete_one({"user_id": user_id})
            return True
        return False

    async def get_all_chats(self):
        """Get list of all saved chats"""
        if not self.connected:
            return []

        return await self.chats.find().to_list(None)

# Initialize database
database = Database()
