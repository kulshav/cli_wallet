import csv
import os

from enum import Enum

from configs.config import settings
from logs.logger import logger


class StorageDataEnum(str, Enum):
    date: str = "Date"
    category: str = "Category"
    amount: str = "Amount"
    desc: str = "Description"

    record_id: str = "ID"


class StorageManager:
    """
    Provides useful basic CRUD methods
    """

    def __init__(self):
        self.path_to_storage = settings.PATH_TO_STORAGE
        self._create_storage()

    def _create_storage(self):
        if not os.path.exists(self.path_to_storage):
            with open(self.path_to_storage, "w") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        StorageDataEnum.date,
                        StorageDataEnum.category,
                        StorageDataEnum.amount,
                        StorageDataEnum.desc,
                    ]
                )
            logger.debug("Storage created!")
        else:
            logger.debug("Storage exists")

    def _drop_storage(self):
        if os.path.exists(self.path_to_storage):
            os.remove(self.path_to_storage)
            logger.debug("Storage has been deleted!")
        else:
            logger.debug("Storage doesnt exists")

    def _insert_row(self, input_data: list | tuple):
        try:
            with open(self.path_to_storage, "a") as file:
                writer = csv.writer(file)
                writer.writerow(input_data)
        except (IOError, csv.Error) as error:
            logger.error(f"Error when trying to insert in storage: {error}")
            return error

    def _insert_many_rows(self, input_data: list[list]):
        try:
            for row in input_data:
                with open(self.path_to_storage, "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(row)
        except (IOError, csv.Error) as error:
            logger.error(f"Error when trying to insert in storage: {error}")
            return error

    def _get_data_dict(self) -> list[dict]:
        with open(self.path_to_storage, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def _get_data_list(self) -> list[list]:
        with open(self.path_to_storage, "r") as file:
            reader = csv.reader(file)
            return list(reader)

    def _update_row(self, row_number: int, updated_data: dict):
        rows = self._get_data_dict()
        header = (
            StorageDataEnum.date,
            StorageDataEnum.category,
            StorageDataEnum.amount,
            StorageDataEnum.desc,
        )
        with open(self.path_to_storage, "w") as file:
            writer = csv.DictWriter(
                f=file,
                fieldnames=header,
            )
            writer.writeheader()
            for index, row in enumerate(rows, start=1):
                if index == row_number:
                    row[StorageDataEnum.date] = updated_data[StorageDataEnum.date]
                    row[StorageDataEnum.category] = updated_data[StorageDataEnum.category]
                    row[StorageDataEnum.amount] = updated_data[StorageDataEnum.amount]
                    row[StorageDataEnum.desc] = updated_data[StorageDataEnum.desc]
                writer.writerow(row)
