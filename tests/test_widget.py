import pytest

from src.widget import get_date, mask_account_card


def test_get_date():
    assert get_date("2024-03-11T02:26:18Z") == "11.03.2024"


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(input_value, expected):
    assert mask_account_card(input_value) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-01-01T00:00:00Z", "01.01.2024"),
        ("2023-12-31T23:59:59Z", "31.12.2023"),
    ],
)
def test_get_date_param(input_date, expected):
    assert get_date(input_date) == expected


def test_mask_account_card_invalid_input():
    with pytest.raises(ValueError):
        mask_account_card("1234567890")
