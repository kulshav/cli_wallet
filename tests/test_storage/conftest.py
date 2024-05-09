import pytest

from storage.core import StorageManager, StorageDataEnum
from storage.crud import QueryManager


@pytest.fixture
def storage_instance():
    storage_instance = StorageManager()

    yield storage_instance


@pytest.fixture
def query_instance():
    query_instance = QueryManager()

    yield query_instance


@pytest.fixture
def restart_storage(storage_instance):
    storage_instance._drop_storage()
    storage_instance._create_storage()


@pytest.fixture
def get_headers():
    return [
        StorageDataEnum.date,
        StorageDataEnum.category,
        StorageDataEnum.amount,
        StorageDataEnum.desc,
    ]


@pytest.fixture
def populate_storage(storage_instance):
    expense_records = [
        ["2024-05-07", "Expense", "500.0", "Groceries"],
        ["2024-05-07", "Expense", "100.0", "Groceries"],
        ["2024-05-07", "Expense", "100.0", "Groceries"],
        ["2024-05-07", "Expense", "500.0", "Groceries"],
        ["2024-05-07", "Expense", "100.0", "Groceries"],
        ["2024-05-07", "Expense", "500.0", "Groceries"],
        ["2024-05-07", "Expense", "100.0", "Groceries"],
        ["2024-05-07", "Expense", "1000.0", "Groceries"],
        ["2024-05-07", "Expense", "1000.0", "Groceries"],
    ]

    income_records = [
        ["2024-05-07", "Income", "1000.0", "Scholarship"],
        ["2024-05-07", "Income", "30000.0", "Salary"],
    ]
    storage_instance._insert_many_rows(income_records)
    storage_instance._insert_many_rows(expense_records)
