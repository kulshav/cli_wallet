from enum import Enum
from datetime import datetime
from typing import Type

from pydantic import BaseModel, field_validator

from promts.promts import user_promt


class CategoryEnum(Enum):
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

    @field_validator("date")
    def validate_date_format(cls, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(user_promt.wrong_date_input_format())
        return date_str

    @field_validator("category")
    def validate_category(cls, category_str):
        if category_str not in CategoryEnum:
            raise ValueError(
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                )
            )
        return category_str
