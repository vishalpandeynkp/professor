import os
import glob
import json
from os.path import dirname, basename, isfile, join

from Professor.utils.logger import LOGGER

lang_folder = dirname(__file__)

# Get language files
langfiles = glob.glob(join(lang_folder, "*.json"))
langfiles = [basename(file)[:-5] for file in langfiles if isfile(file) and not file.endswith("__init__.py")]

# Dictionary to store loaded language strings
languages = {}

# Load all language files into memory
for language in langfiles:
    try:
        with open(f"{lang_folder}/{language}.json", "r", encoding="utf-8") as f:
            languages[language] = json.load(f)
        LOGGER.info(f"Loaded language: {language}")
    except Exception as e:
        LOGGER.error(f"Error loading language {language}: {e}")

def get_string(language: str) -> dict:
    """
    Get language strings dictionary for a language.
    Falls back to English if the specified language is
    not available.
    """
    if language not in languages:
        LOGGER.warning(f"Language {language} not found, falling back to English")
        return languages["en"]

    return languages[language]
