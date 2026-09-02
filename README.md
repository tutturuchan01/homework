# Банковские операции

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/status-in%20development-green)

## Описание проекта

Проект предназначен для обработки банковских операций клиента.

Реализованы функции для:

* маскировки номеров банковских карт и счетов;
* преобразования дат;
* фильтрации операций по статусу;
* сортировки операций по дате;
* генерации данных по транзакциям;
* логирования функций;
* загрузки транзакций из JSON-файлов;
* загрузки финансовых операций из CSV- и XLSX-файлов;
* конвертации валют через внешний API.

## Содержание

* Технологии
* Начало работы
* Использование
* Тестирование
* To Do
* Автор

## Технологии

В проекте используются:

* Python 3.13
* Pandas
* Poetry
* Pytest
* Flake8
* Git
* GitHub

## Начало работы

### Установка проекта

Клонируйте репозиторий:

```bash
git clone <ссылка_на_репозиторий>
```

Перейдите в директорию проекта:

```bash
cd homework
```

Установите зависимости:

```bash
poetry install
```

## Использование

### Маскировка номера карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
```

Результат:

```text
7000 79** **** 6361
```

### Маскировка номера счета

```python
from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))
```

Результат:

```text
**4305
```

### Работа с датой

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
```

Результат:

```text
11.03.2024
```

### Фильтрация операций

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"}
]

print(filter_by_state(operations))
```

### Сортировка операций

```python
from src.processing import sort_by_date

operations = [
    {"id": 1, "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "date": "2018-06-30T02:08:58.425572"}
]

print(sort_by_date(operations))
```
## Модуль generators

Добавлен модуль `generators`, содержащий генераторы для работы с транзакциями.

### Фильтрация по валюте

```python
from src.generators import filter_by_currency

for tx in filter_by_currency(transactions, "USD"):
    print(tx)
```

### Описания транзакций
```python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

### Генератор номеров карт
```python
from src.generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
```


## Модуль decorators

Добавлен модуль `decorators`, содержащий декоратор для логирования работы функций.

### Логирование в консоль

```python
from src.decorators import log


@log()
def add(a, b):
    return a + b


add(1, 2)
```

Результат:

```text
add ok
```

### Логирование в файл

```python
from src.decorators import log


@log(filename="mylog.txt")
def add(a, b):
    return a + b


add(1, 2)
```

В файл `mylog.txt` будет записано:

```text
add ok
```


## Модуль utils

### Загрузка транзакций из JSON

```python
from src.utils import load_transactions

transactions = load_transactions("data/operations.json")
print(transactions)
```

## Модуль external_api

### Конвертация валют

```python
from src.external_api import transaction_amount

amount = transaction_amount(transaction)
print(amount)
```


## Тестирование

Для запуска тестов используйте:

```bash
pytest
```

Для проверки кода линтером:

```bash
flake8
```

## To Do

* Добавить новые функции обработки банковских операций.
* Расширить покрытие тестами.
* Добавить автоматическую проверку кода.

## Автор

Varenka
