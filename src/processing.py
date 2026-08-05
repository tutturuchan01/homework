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
