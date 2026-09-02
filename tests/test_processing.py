from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)

operations = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "description": "Открытие вклада",
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2020-01-15T10:20:30.123456",
        "description": "Перевод с карты на карту",
    },
]


def test_filter_by_state():
    assert len(filter_by_state(operations)) == 2


def test_sort_by_date():
    result = sort_by_date(operations)
    assert result[0]["date"] < result[1]["date"]


def test_sort_by_date_reverse():
    result = sort_by_date(operations, ascending=False)
    assert result[0]["date"] > result[1]["date"]


def test_process_bank_search():
    result = process_bank_search(operations, "перевод")
    assert len(result) == 2


def test_process_bank_search_case_insensitive():
    result = process_bank_search(operations, "ПЕРЕВОД")
    assert len(result) == 2


def test_process_bank_search_no_results():
    result = process_bank_search(operations, "зарплата")
    assert result == []


def test_process_bank_operations():
    categories = [
        "Перевод с карты на карту",
        "Открытие вклада",
    ]

    result = process_bank_operations(operations, categories)

    assert result == {
        "Перевод с карты на карту": 2,
        "Открытие вклада": 1,
    }


def test_process_bank_operations_category_not_found():
    categories = [
        "Перевод с карты на карту",
        "Оплата телефона",
    ]

    result = process_bank_operations(operations, categories)

    assert result == {
        "Перевод с карты на карту": 2,
        "Оплата телефона": 0,
    }
