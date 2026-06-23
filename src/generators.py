from collections.abc import Generator


def filter_by_currency(transactions: list, currency_code: str) -> Generator:
    """
    Фильтрует транзакции по коду валюты.
    """

    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code")
            == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """
    Возвращает описания транзакций.
    """

    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.
    """

    for number in range(start, stop + 1):
        card_number = f"{number:016d}"

        yield (
            f"{card_number[:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:]}"
        )
