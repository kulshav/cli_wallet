from enum import Enum
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator
from pydantic.main import Model

from promts.promts import user_promt


class CategoryEnum(str, Enum):
    income: str = "Income"
    expense: str = "Expense"


class InputValidator(BaseModel):
    """
    Validate types from input data
    """

    date: str
    category: str
    amount: float
    description: str

    record_id: int
    record_data: dict
    search_data: dict

    def __call__(
        self,
        record_id: int | None = None,
        date: str | None = None,
        category: str | None = None,
        amount: int | None = None,
        record_data: dict | None = None,
        search_data: dict | None = None,
    ):
        if record_id:
            self.validate_record_id(record_id)
        if date:
            self.validate_date_format(date)
        if category:
            self.validate_category(category)
        if amount:
            self.validate_amount(amount)
        if record_data:
            self.validate_record_data(record_data)
        if search_data:
            self.validate_search_data(search_data)

    @field_validator("date")
    def validate_date_format(cls, date_input: str) -> str | ValueError:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            raise ValueError(user_promt.wrong_date_input_format())
        return date_input

    @field_validator("category")
    def validate_category(
        cls, category_input: str | CategoryEnum
    ) -> CategoryEnum | ValueError:
        if category_input not in CategoryEnum:
            raise ValueError(
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                )
            )
        return category_input

    @field_validator("amount")
    def validate_amount(cls, amount_input: float) -> float | ValueError:
        if amount_input < 0:
            raise ValueError(user_promt.negative_amount_input())

        return amount_input

    @field_validator("record_id")
    def validate_record_id(cls, record_id_input: int) -> int | ValueError:
        if record_id_input < 0:
            raise ValueError(user_promt.wrong_input_record_id())

        return record_id_input

    @field_validator("record_data")
    def validate_record_data(cls, record_data_input: dict | None) -> dict | ValueError:
        if record_data_input is None:
            raise ValueError(user_promt.user_promt.not_found_any_records())

        return record_data_input

    @field_validator("search_data")
    def validate_search_data(cls, search_data: dict | None) -> dict | ValueError:
        if len(search_data) < 0:
            raise ValueError(user_promt.not_found_any_records())

        return search_data