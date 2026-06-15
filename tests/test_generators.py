import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2


def test_filter_by_currency_empty(transactions):
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert "Перевод организации" in result


def test_card_number_generator():
    result = list(card_number_generator(1, 3))

    assert result[0] == "0000 0000 0000 0001"
    assert result[-1] == "0000 0000 0000 0003"
