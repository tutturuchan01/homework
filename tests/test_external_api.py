from unittest.mock import Mock, patch

from src.external_api import transaction_amount


def test_transaction_amount_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {
                "code": "RUB"
            }
        }
    }

    assert transaction_amount(transaction) == 100.50


@patch("src.external_api.requests.get")
def test_transaction_amount_usd(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "result": 9500.0
    }

    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD"
            }
        }
    }

    assert transaction_amount(transaction) == 9500.0
