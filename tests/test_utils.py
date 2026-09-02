import json

from src.utils import load_transactions


def test_load_transactions_success(tmp_path):
    test_file = tmp_path / "test.json"

    data = [{"id": 1}, {"id": 2}]

    test_file.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    assert load_transactions(str(test_file)) == data


def test_load_transactions_file_not_found():
    assert load_transactions("missing.json") == []


def test_load_transactions_invalid_json(tmp_path):
    test_file = tmp_path / "test.json"

    test_file.write_text(
        "invalid json",
        encoding="utf-8",
    )

    assert load_transactions(str(test_file)) == []


def test_load_transactions_not_list(tmp_path):
    test_file = tmp_path / "test.json"

    test_file.write_text(
        json.dumps({"id": 1}),
        encoding="utf-8",
    )

    assert load_transactions(str(test_file)) == []
