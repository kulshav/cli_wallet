from datetime import datetime

from utils.validator import CategoryEnum
from storage.core import StorageManager, StorageDataEnum


class QueryManager(StorageManager):
    """
    Class for executing crud queries from storage
    """
    def __init__(self):
        super().__init__()

    def insert_new_record(
        self, date: datetime, category: str, amount: float, desc: str
    ):
        self._insert_row([date, category, amount, desc])

    def get_current_balance(self) -> float:
        rows = self._get_data_dict()

        total_income = 0.0
        total_expense = 0.0

        for row in rows:
            if row[StorageDataEnum.category.value] == CategoryEnum.income.value:
                total_income += float(row[StorageDataEnum.amount.value])

            if row[StorageDataEnum.category.value] == CategoryEnum.expense.value:
                total_expense += float(row[StorageDataEnum.amount.value])

        return total_income - total_expense


query = QueryManager()

