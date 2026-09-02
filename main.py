from src.file_readers import read_csv_file, read_excel_file
from src.processing import (
    filter_by_state,
    process_bank_search,
    sort_by_date,
)
from src.utils import load_transactions


def print_transaction(transaction: dict) -> None:
    """Выводит информацию о банковской операции."""
    date = transaction.get("date", "")
    description = transaction.get("description", "")
    amount = transaction.get("amount", "")
    currency = transaction.get("currency_name", "")

    print(f"{date[:10]} {description}")
    print(f"Сумма: {amount} {currency}")
    print()


def main() -> None:
    """Запускает основную логику программы."""
    print(
        "Программа: Привет! Добро пожаловать в программу работы "
        "с банковскими транзакциями."
    )
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input("Пользователь: ")

    if file_type == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = load_transactions("operations.json")
    elif file_type == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_csv_file("transactions.csv")
    elif file_type == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_excel_file("transactions_excel.xlsx")
    else:
        print("Программа: Неверный пункт меню.")
        return

    if not transactions:
        print("Программа: Не удалось загрузить транзакции.")
        return

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            "Программа: Введите статус, по которому необходимо "
            "выполнить фильтрацию."
        )
        print(
            "Доступные для фильтровки статусы: "
            "EXECUTED, CANCELED, PENDING"
        )

        status = input("Пользователь: ").upper()

        if status in available_statuses:
            break

        print(f'Программа: Статус операции "{status}" недоступен.')

    transactions = filter_by_state(transactions, status)

    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    sort_answer = input(
        "Программа: Отсортировать операции по дате? Да/Нет\n"
        "Пользователь: "
    ).lower()

    if sort_answer == "да":
        sort_order = input(
            "Программа: Отсортировать по возрастанию "
            "или по убыванию?\n"
            "Пользователь: "
        ).lower()

        transactions = sort_by_date(
            transactions,
            ascending=sort_order == "по возрастанию",
        )

    ruble_answer = input(
        "Программа: Выводить только рублевые транзакции? Да/Нет\n"
        "Пользователь: "
    ).lower()

    if ruble_answer == "да":
        transactions = [
            transaction
            for transaction in transactions
            if transaction.get("currency_code") == "RUB"
        ]

    search_answer = input(
        "Программа: Отфильтровать список транзакций "
        "по определенному слову в описании? Да/Нет\n"
        "Пользователь: "
    ).lower()

    if search_answer == "да":
        search = input(
            "Программа: Введите слово для поиска:\n"
            "Пользователь: "
        )
        transactions = process_bank_search(transactions, search)

    if not transactions:
        print(
            "Программа: Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
        return

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}")
    print()

    for transaction in transactions:
        print_transaction(transaction)


if __name__ == "__main__":
    main()
