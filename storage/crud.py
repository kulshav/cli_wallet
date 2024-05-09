import csv
from datetime import datetime
from typing import Any

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
            if row[StorageDataEnum.category] == CategoryEnum.income:
                total_income += float(row[StorageDataEnum.amount])

            if row[StorageDataEnum.category] == CategoryEnum.expense:
                total_expense += float(row[StorageDataEnum.amount])

        return total_income - total_expense

    def get_all_time_total_amount(self, category: str):
        rows = self._get_data_dict()

        total_income = 0

        for row in rows:
            if row[StorageDataEnum.category] == category:
                total_income += float(row[StorageDataEnum.amount])

        return total_income

    def get_categorized_filtered_data_by_period(
        self, category: str, year: int = None, month: int = None, day: int = None
    ):
        total_amount = 0
        rows = self._get_data_dict()

        for row in rows:
            row_date = datetime.strptime(row[StorageDataEnum.date], "%Y-%m-%d").date()

            # Filter by year
            if year is not None and row_date.year != year:
                continue

            # Filter by month
            if month is not None and row_date.month != month:
                continue

            # Filter by day
            if day is not None and row_date.day != day:
                continue

            if row[StorageDataEnum.category] == category:
                total_amount += float(row[StorageDataEnum.amount])

        return total_amount

    def get_record_filtered(
        self,
        date: str = None,
        category: str = None,
        amount: float = None,
        desc: str = None,
    ) -> list[dict[str, Any]]:

        filtered_records = []
        rows = self._get_data_dict()

        for index, row in enumerate(rows, start=1):
            record_date = row[StorageDataEnum.date]
            record_category = row[StorageDataEnum.category]
            record_amount = float(row[StorageDataEnum.amount])
            record_desc = row[StorageDataEnum.desc]

            # Check if the record matches the search criteria
            if (
                (date is None or date == record_date)
                and (category is None or category == record_category)
                and (amount is None or amount == record_amount)
                and (desc is None or desc in record_desc)
            ):
                filtered_records.append(
                    {
                        StorageDataEnum.record_id: index,
                        StorageDataEnum.date: record_date,
                        StorageDataEnum.category: record_category,
                        StorageDataEnum.amount: record_amount,
                        StorageDataEnum.desc: record_desc,
                    }
                )

        return filtered_records

    def get_records_with_ids(self) -> list[dict[str, Any]]:
        records_with_ids = []
        rows = self._get_data_dict()

        for index, row in enumerate(rows, start=1):
            records_with_ids.append(
                {
                    StorageDataEnum.record_id: index,
                    StorageDataEnum.date: row[StorageDataEnum.date],
                    StorageDataEnum.category: row[StorageDataEnum.category],
                    StorageDataEnum.amount: row[StorageDataEnum.amount],
                    StorageDataEnum.desc: row[StorageDataEnum.desc],
                }
            )

        return records_with_ids

    def get_record_data_by_id(self, record_id: int) -> dict | None:
        rows = self._get_data_dict()

        for index, row in enumerate(rows, start=1):
            if index == record_id:
                return row

    def edit_record_by_id(self, record_id: int, updated_data: dict):
        self._update_row(row_number=record_id, updated_data=updated_data)


query = QueryManager()
