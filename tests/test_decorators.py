import pytest

from src.decorators import log


@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b


def test_log_success_console(capsys):
    result = add(2, 3)

    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error" in captured.out


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(2, 3)

    assert result == 6

    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content


def test_log_error_to_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def divide_error(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_error(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "divide_error error" in content
