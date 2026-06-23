from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Callable[..., Any]:
    """Декоратор для логирования работы функции."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                return result

            except Exception as error:
                message = (
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise

        return wrapper

    return decorator
