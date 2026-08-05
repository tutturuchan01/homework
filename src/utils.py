import json
from typing import Any

from src.logger import get_logger

logger = get_logger(__name__)


def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: путь к JSON-файлу
    :return: список транзакций или пустой список
    """

    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(
                    "Файл %s успешно загружен",
                    file_path,
                )
                return data

            logger.error(
                "Файл %s содержит не список",
                file_path,
            )
            return []

    except FileNotFoundError:
        logger.error(
            f"Файл {file_path} не найден"
        )
        return []

    except json.JSONDecodeError:
        logger.error(
            f"Файл {file_path} содержит некорректный JSON"
        )
        return []
