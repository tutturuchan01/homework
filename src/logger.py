import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        log_file = LOG_DIR / f"{name.split('.')[-1]}.log"

        file_handler = logging.FileHandler(
            log_file,
            mode="w",
            encoding="utf-8",
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
