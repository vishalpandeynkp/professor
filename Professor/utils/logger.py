import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

from colorama import Fore, Style

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Get current date and time for log filename
now = datetime.now()
log_filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".log"
log_filepath = os.path.join("logs", log_filename)

# Configure main logger with file and console output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            log_filepath,
            maxBytes=5000000,  # ~5MB per file
            backupCount=10     # Keep up to 10 log files
        ),
        logging.StreamHandler()
    ]
)

# Get the logger instance
LOGGER = logging.getLogger("ProfessorMusicBot")

# Custom handler for terminal output with colors
class ColorizedHandler(logging.StreamHandler):
    COLORS = {
        'DEBUG': Fore.BLUE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
    }

    def emit(self, record):
        try:
            msg = self.format(record)
            color = self.COLORS.get(record.levelname, '')
            reset = Style.RESET_ALL
            stream = self.stream
            stream.write(f"{color}{msg}{reset}\n")
            self.flush()
        except Exception:
            self.handleError(record)

# Replace the default stream handler with our colorized one
for handler in LOGGER.handlers:
    if isinstance(handler, logging.StreamHandler) and not isinstance(handler, RotatingFileHandler):
        LOGGER.removeHandler(handler)
        LOGGER.addHandler(ColorizedHandler())

# Log startup message
LOGGER.info("Logger initialized. Bot starting...")

# Print logo in terminal
def log_startup():
    """Print ASCII logo at startup"""
    print(f"{Fore.MAGENTA}")
    print("╔═════════════════════════════════════════════════╗")
    print("║                                                 ║")
    print("║             PROFESSOR MUSIC BOT                 ║")
    print("║                                                 ║")
    print("║          The Powerful Telegram Bot              ║")
    print("║                                                 ║")
    print("╚═════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    LOGGER.info("PROFESSOR MUSIC BOT IS STARTING...")
