from datetime import datetime

from storage.core import StorageManager


class QueryManager(StorageManager):
    def __init__(self):
        super().__init__()

    def insert_new_record(
        self, date: datetime, category: str, amount: float, desc: str
    ):
        self._insert_row([date, category, amount, desc])


query = QueryManager()

