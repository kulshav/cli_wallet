import pytest

from storage.core import StorageDataEnum
from utils.validator import CategoryEnum


class TestCrud:

    def test_get_records(self, restart_storage, populate_storage, query_instance):
        index = 1
        rows = query_instance.get_records_with_ids()

        total_income = 0
        total_expense = 0

        for index, row in enumerate(rows, start=1):
            assert isinstance(row, dict)
            assert row[StorageDataEnum.record_id] == index
            record = query_instance.get_record_data_by_id(index)

            assert row[StorageDataEnum.date.value] == record[StorageDataEnum.date.value]
            assert (
                row[StorageDataEnum.category.value]
                == record[StorageDataEnum.category.value]
            )
            assert (
                row[StorageDataEnum.amount.value]
                == record[StorageDataEnum.amount.value]
            )
            assert row[StorageDataEnum.desc.value] == record[StorageDataEnum.desc.value]

            if record[StorageDataEnum.category] == CategoryEnum.income:
                total_income += float(row[StorageDataEnum.amount])

            if row[StorageDataEnum.category] == CategoryEnum.expense:
                total_expense += float(row[StorageDataEnum.amount])

        assert index == len(rows)

        current_balance = query_instance.get_current_balance()
        assert (total_income - total_expense) == current_balance

        all_time_total_income = query_instance.get_all_time_total_amount(
            CategoryEnum.income
        )
        all_time_total_expense = query_instance.get_all_time_total_amount(
            CategoryEnum.expense
        )
        assert all_time_total_income == total_income
        assert all_time_total_expense == total_expense
