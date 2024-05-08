import pytest

from storage.core import StorageManager, StorageDataEnum


class TestStorageManager:
    def test_storage_data_enum(self):
        assert StorageDataEnum.date == "Date"
        assert isinstance(StorageDataEnum.date, str)

        assert StorageDataEnum.category == "Category"
        assert isinstance(StorageDataEnum.category, str)

        assert StorageDataEnum.amount == "Amount"
        assert isinstance(StorageDataEnum.amount, str)

        assert StorageDataEnum.desc == "Description"
        assert isinstance(StorageDataEnum.desc, str)

    def test_storage_manager(self, storage_instance, restart_storage):
        headers = [
            StorageDataEnum.date,
            StorageDataEnum.category,
            StorageDataEnum.amount,
            StorageDataEnum.desc
        ]
        expense_record = ["2024-05-07", "Expense", "500.0", "Groceries"]
        income_record = ["2024-05-07", "Income", "1000.0", "Scholarship"]

        assert storage_instance._get_data_dict() == []
        assert storage_instance._get_data_list() == [headers]

        storage_instance._insert_many_rows([expense_record, income_record])
        assert storage_instance._get_data_list() == [headers, expense_record, income_record]
        assert storage_instance._get_data_dict() == [
            {
                StorageDataEnum.amount: expense_record[2],
                StorageDataEnum.category: expense_record[1],
                StorageDataEnum.date: expense_record[0],
                StorageDataEnum.desc: expense_record[3],
            },
            {
                StorageDataEnum.amount: income_record[2],
                StorageDataEnum.category: income_record[1],
                StorageDataEnum.date: income_record[0],
                StorageDataEnum.desc: income_record[3],
            },
        ]




