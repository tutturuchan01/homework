import re
from collections import Counter
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """
    Фильтрует список операций по указанному статусу.

    :param operations: список операций
    :param state: статус операции
    :return: отфильтрованный список операций
    """

    return [
        operation
        for operation in operations
        if operation.get("state") == state
    ]


def sort_by_date(
    operations: list[dict[str, Any]],
    ascending: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.

    :param operations: список операций
    :param ascending: порядок сортировки
    :return: отсортированный список операций
    """

    return sorted(
        operations,
        key=lambda operation: operation["date"],
        reverse=not ascending,
    )


def process_bank_search(
    data: list[dict[str, Any]],
    search: str
) -> list[dict[str, Any]]:
    """
    Ищет банковские операции по строке в описании.

    :param data: список банковских операций
    :param search: строка для поиска
    :return: список подходящих операций
    """

    pattern = re.compile(re.escape(search), re.IGNORECASE)

    return [
        operation
        for operation in data
        if pattern.search(str(operation.get("description", "")))
    ]


def process_bank_operations(
    data: list[dict[str, Any]],
    categories: list[str]
) -> dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    :param data: список банковских операций
    :param categories: список категорий
    :return: словарь с количеством операций по категориям
    """

    descriptions = [
        operation.get("description", "")
        for operation in data
        if operation.get("description") in categories
    ]

    counter = Counter(descriptions)

    return {
        category: counter.get(category, 0)
        for category in categories
    }
