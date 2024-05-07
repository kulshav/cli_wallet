import pytest

from storage.core import StorageManager, StorageData


class TestStorageManager:
    def test_storage_data_enum(self):
        assert StorageData.date.value == "Date"
        assert isinstance(StorageData.date.value, str)

        assert StorageData.category.value == "Category"
        assert isinstance(StorageData.category.value, str)

        assert StorageData.amount.value == "Amount"
        assert isinstance(StorageData.amount.value, str)

        assert StorageData.desc.value == "Description"
        assert isinstance(StorageData.desc.value, str)

    def test_storage_manager(self, storage_instance, restart_storage):
        headers = [
            StorageData.date.value,
            StorageData.category.value,
            StorageData.amount.value,
            StorageData.desc.value
        ]
        expense_record = ["2024-05-07", "Expense", "500.0", "Groceries"]
        income_record = ["2024-05-07", "Income", "1000.0", "Scholarship"]

        assert storage_instance._get_data_dict() == []
        assert storage_instance._get_data_list() == [headers]

        storage_instance._insert_many_rows([expense_record, income_record])
        assert storage_instance._get_data_list() == [headers, expense_record, income_record]
        assert storage_instance._get_data_dict() == [
            {
                StorageData.amount.value: expense_record[2],
                StorageData.category.value: expense_record[1],
                StorageData.date.value: expense_record[0],
                StorageData.desc.value: expense_record[3],
            },
            {
                StorageData.amount.value: income_record[2],
                StorageData.category.value: income_record[1],
                StorageData.date.value: income_record[0],
                StorageData.desc.value: income_record[3],
            },
        ]




