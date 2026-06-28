import json
from typing import Any


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
                return data

            return []

    except (
        FileNotFoundError,
        json.JSONDecodeError,
    ):
        return []
