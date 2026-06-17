import pytest


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
        },
    ]
