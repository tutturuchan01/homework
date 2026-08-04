import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            LOG_FILE,
            mode="w",
            encoding="utf-8",
        )

        file_formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)

    return logger
