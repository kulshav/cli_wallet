import pytest

from utils.validator import CategoryEnum, InputValidator
from promts.promts import user_promt


class TestValidator:
    def test_category_enum(self):
        assert CategoryEnum.expense == "Expense"
        assert CategoryEnum.income == "Income"

        assert isinstance(CategoryEnum.expense, str)
        assert isinstance(CategoryEnum.income, str)

    @pytest.mark.parametrize(
        ("date", "expected_result"),
        [
            ("20-05-05", user_promt.wrong_date_input_format()),
            ("asd", user_promt.wrong_date_input_format()),
            ("123", user_promt.wrong_date_input_format()),
            ("2024-2024-2024", user_promt.wrong_date_input_format()),
            ("2024-13-123", user_promt.wrong_date_input_format()),
        ],
    )
    def test_input_wrong_date_validator(self, date, expected_result):
        with pytest.raises(ValueError) as error:
            InputValidator.validate_date_format(date)
        assert str(error.value) == expected_result

    @pytest.mark.parametrize(
        ("category", "expected_result"),
        [
            (
                "20-05-05",
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                ),
            ),
            (
                "asd",
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                ),
            ),
            (
                "123",
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                ),
            ),
            (
                "2024-2024-2024",
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                ),
            ),
            (
                "2024-13-123",
                user_promt.wrong_category_format(
                    CategoryEnum.income.value, CategoryEnum.expense.value
                ),
            ),
        ],
    )
    def test_input_wrong_category_validator(self, category, expected_result):
        with pytest.raises(ValueError) as error:
            InputValidator.validate_category(category)
        assert str(error.value) == expected_result

    def test_validate_date_category_success(self):
        assert InputValidator.validate_date_format("2024-01-01") == "2024-01-01"
        assert (
            InputValidator.validate_category(CategoryEnum.income) == CategoryEnum.income
        )
        assert (
            InputValidator.validate_category(CategoryEnum.expense)
            == CategoryEnum.expense
        )
