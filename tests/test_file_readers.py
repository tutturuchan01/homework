from unittest.mock import patch

from src.file_readers import read_csv_file, read_excel_file


@patch("src.file_readers.pd.read_csv")
def test_read_csv_file(mock_read_csv):
    mock_df = mock_read_csv.return_value
    mock_df.to_dict.return_value = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "amount": 16210,
        }
    ]

    result = read_csv_file("transactions.csv")

    mock_read_csv.assert_called_once_with("transactions.csv", sep=";")
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "amount": 16210,
        }
    ]


@patch("src.file_readers.pd.read_excel")
def test_read_excel_file(mock_read_excel):
    mock_df = mock_read_excel.return_value
    mock_df.to_dict.return_value = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "amount": 16210,
        }
    ]

    result = read_excel_file("transactions_excel.xlsx")

    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "amount": 16210,
        }
    ]
