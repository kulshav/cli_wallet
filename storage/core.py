import csv
import os

from enum import Enum

from loguru import logger

from configs.config import settings


class StorageDataEnum(Enum):
    date: str = "Date"
    category: str = "Category"
    amount: str = "Amount"
    desc: str = "Description"


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
                # Write headers to the CSV file
                writer = csv.writer(file)
                writer.writerow(
                    [
                        StorageDataEnum.date.value,
                        StorageDataEnum.category.value,
                        StorageDataEnum.amount.value,
                        StorageDataEnum.desc.value,
                    ]
                )
            logger.success("Storage created!")
        else:
            logger.info("Storage exists")

    def _drop_storage(self):
        if os.path.exists(self.path_to_storage):
            os.remove(self.path_to_storage)
            logger.success("Storage has been deleted!")
        else:
            logger.warning("Storage doesnt exists")

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
                with open(f"{self.path_to_storage}", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(row)
        except (IOError, csv.Error) as error:
            logger.error(f"Error when trying to insert in storage: {error}")
            return error

    def _get_data_dict(self) -> list:
        query_data = []
        with open(f"{self.path_to_storage}", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                query_data.append(row)

        return query_data

    def _get_data_list(self) -> list:
        query_data = []
        with open(f"{self.path_to_storage}", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                query_data.append(row)

        return query_data

