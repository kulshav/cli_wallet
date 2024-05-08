import pytest

from storage.core import StorageManager, StorageDataEnum
from utils.validator import CategoryEnum


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

    def test_storage_manager(self, storage_instance, restart_storage, get_headers):

        assert storage_instance._get_data_dict() == []
        assert storage_instance._get_data_list() == [get_headers]

    def test_storage_manager_insert(
        self, storage_instance, restart_storage, get_headers
    ):
        expense_record = ["2024-05-07", "Expense", "500.0", "Groceries"]
        income_record = ["2024-05-07", "Income", "1000.0", "Scholarship"]

        storage_instance._insert_many_rows([expense_record, income_record])
        assert storage_instance._get_data_list() == [
            get_headers,
            expense_record,
            income_record,
        ]
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

        assert len(storage_instance._get_data_list()) == 3  # list includes Headers
        assert len(storage_instance._get_data_dict()) == 2

    @pytest.mark.parametrize(
        ("record_id", "updated_data", "expected_result"),
        [
            (
                1,
                {
                    StorageDataEnum.date.value: "2024-12-12",
                    StorageDataEnum.category.value: CategoryEnum.expense.value,
                    StorageDataEnum.amount.value: 1000,
                    StorageDataEnum.desc.value: "Test Update",
                },
                {
                    StorageDataEnum.date.value: "2024-12-12",
                    StorageDataEnum.category.value: CategoryEnum.expense.value,
                    StorageDataEnum.amount.value: "1000",
                    StorageDataEnum.desc.value: "Test Update",
                },
            ),
            (
                10,
                {
                    StorageDataEnum.date.value: "2024-12-12",
                    StorageDataEnum.category.value: CategoryEnum.expense.value,
                    StorageDataEnum.amount.value: "1000",
                    StorageDataEnum.desc.value: "Test Update",
                },
                {
                    StorageDataEnum.date.value: "2024-12-12",
                    StorageDataEnum.category.value: CategoryEnum.expense.value,
                    StorageDataEnum.amount.value: "1000",
                    StorageDataEnum.desc.value: "Test Update",
                },
            )
        ],
    )
    def test_storage_manager_update_row(
        self,
        storage_instance,
        restart_storage,
        get_headers,
        populate_storage,
        record_id,
        updated_data,
        expected_result,
    ):
        rows_before = storage_instance._get_data_dict()
        total_records_before = len(rows_before)

        storage_instance._update_row(
            row_number=record_id,
            updated_data=updated_data
        )

        rows_after = storage_instance._get_data_dict()
        total_records_after = len(rows_after)

        row_data_after_update = {}

        for index, row in enumerate(rows_after, start=1):
            if index == record_id:
                row_data_after_update = row

        assert row_data_after_update == expected_result
        assert total_records_after == total_records_before

