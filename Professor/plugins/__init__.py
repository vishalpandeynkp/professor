import glob
import importlib
import os
from os.path import dirname, basename, isfile, join

from Professor.utils.logger import LOGGER

# Get all Python files in the plugins directory
plugin_files = glob.glob(join(dirname(__file__), "*.py"))
plugin_modules = [
    basename(f)[:-3]
    for f in plugin_files
    if isfile(f) and not f.endswith("__init__.py")
]

# List to store all imported plugin modules
all_modules = []

async def load_plugins():
    """
    Load all plugin modules
    """
    for module in plugin_modules:
        try:
            imported_module = importlib.import_module(f"Professor.plugins.{module}")
            if hasattr(imported_module, "__module_name__"):
                module_name = imported_module.__module_name__
            else:
                module_name = module.replace("_", " ").title()

            all_modules.append(imported_module)
            LOGGER.info(f"Successfully imported: {module_name}")
        except Exception as e:
            LOGGER.error(f"Error importing {module}: {e}")

    LOGGER.info(f"Successfully imported {len(all_modules)} plugins")
    return all_modules
