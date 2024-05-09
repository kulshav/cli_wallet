import pytest

from storage.crud import query
from utils.validator import CategoryEnum


@pytest.fixture
def get_all_time_income() -> float:
    return query.get_all_time_total_amount(CategoryEnum.income.value)


@pytest.fixture
def get_all_time_expense() -> float:
    return query.get_all_time_total_amount(CategoryEnum.expense.value)
