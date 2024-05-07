import pytest

from storage.core import StorageManager, StorageDataEnum


class TestStorageManager:
    def test_storage_data_enum(self):
        assert StorageDataEnum.date.value == "Date"
        assert isinstance(StorageDataEnum.date.value, str)

        assert StorageDataEnum.category.value == "Category"
        assert isinstance(StorageDataEnum.category.value, str)

        assert StorageDataEnum.amount.value == "Amount"
        assert isinstance(StorageDataEnum.amount.value, str)

        assert StorageDataEnum.desc.value == "Description"
        assert isinstance(StorageDataEnum.desc.value, str)

    def test_storage_manager(self, storage_instance, restart_storage):
        headers = [
            StorageDataEnum.date.value,
            StorageDataEnum.category.value,
            StorageDataEnum.amount.value,
            StorageDataEnum.desc.value
        ]
        expense_record = ["2024-05-07", "Expense", "500.0", "Groceries"]
        income_record = ["2024-05-07", "Income", "1000.0", "Scholarship"]

        assert storage_instance._get_data_dict() == []
        assert storage_instance._get_data_list() == [headers]

        storage_instance._insert_many_rows([expense_record, income_record])
        assert storage_instance._get_data_list() == [headers, expense_record, income_record]
        assert storage_instance._get_data_dict() == [
            {
                StorageDataEnum.amount.value: expense_record[2],
                StorageDataEnum.category.value: expense_record[1],
                StorageDataEnum.date.value: expense_record[0],
                StorageDataEnum.desc.value: expense_record[3],
            },
            {
                StorageDataEnum.amount.value: income_record[2],
                StorageDataEnum.category.value: income_record[1],
                StorageDataEnum.date.value: income_record[0],
                StorageDataEnum.desc.value: income_record[3],
            },
        ]




