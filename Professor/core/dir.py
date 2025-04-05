import os
import sys
from os import mkdir
from os.path import exists, isdir

from Professor.utils.logger import LOGGER

def dirr():
    """
    Create necessary directories for the bot to function properly
    """

    # Define all directories that need to be created
    required_dirs = [
        "downloads",
        "cache",
        "logs",
        "assets",
        "raw_files",
        "downloads/audio",
        "downloads/video"
    ]

    for directory in required_dirs:
        if not exists(directory):
            try:
                mkdir(directory)
                LOGGER.info(f"Created directory: {directory}")
            except Exception as e:
                LOGGER.error(f"Error creating directory {directory}: {e}")
                sys.exit()

    # Create temp directories for downloading music/videos
    if not isdir("./downloads/audio"):
        try:
            mkdir("./downloads/audio")
            LOGGER.info("Created directory: downloads/audio")
        except Exception as e:
            LOGGER.error(f"Error creating audio directory: {e}")
            sys.exit()

    if not isdir("./downloads/video"):
        try:
            mkdir("./downloads/video")
            LOGGER.info("Created directory: downloads/video")
        except Exception as e:
            LOGGER.error(f"Error creating video directory: {e}")
            sys.exit()

    # Create empty __init__.py files to make directories importable
    for dirpath, dirnames, filenames in os.walk("./"):
        # Skip directories that shouldn't be packages
        if "/." in dirpath or "/.." in dirpath or "__pycache__" in dirpath:
            continue

        if isdir(dirpath) and "__init__.py" not in filenames:
            try:
                with open(os.path.join(dirpath, "__init__.py"), "w") as f:
                    pass
                LOGGER.info(f"Created __init__.py in {dirpath}")
            except Exception as e:
                LOGGER.error(f"Error creating __init__.py in {dirpath}: {e}")

    LOGGER.info("Directories check completed.")
