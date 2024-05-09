import pytest

from enum import Enum

from typer.testing import CliRunner

from promts.promts import user_promt
from storage.crud import query
from run import app
from utils.validator import CategoryEnum


class ExitCodesEnum(str, Enum):
    OK: int = 0
    ERROR: int = 2


runner = CliRunner()


def test_app_no_args():
    result = runner.invoke(app, [])
    # Exit without an error
    assert result.exit_code == int(ExitCodesEnum.OK)
    assert "Simple budget tracker CLI application" in result.stdout
    assert "--help" in result.stdout


@pytest.mark.parametrize("arg", ["add", "hello", "asd"])
def test_app_wrong_args(arg):
    result = runner.invoke(app, args=[arg])
    assert result.exit_code == int(ExitCodesEnum.ERROR)


@pytest.mark.parametrize(
    ("command", "expected_result"),
    [
        ("display", "--help, balance, expense, income"),
        ("record", "--help, add, search, edit"),
    ],
)
def test_app_display_record_commands(command, expected_result):
    result = runner.invoke(app, args=[command])
    assert result.exit_code == int(ExitCodesEnum.OK)

    for option in expected_result.split(","):
        assert option in result.stdout


def test_app_display_balance():
    result = runner.invoke(app, args=["display", "balance"])
    assert result.exit_code == int(ExitCodesEnum.OK)
    assert "Balance" in result.stdout
    result_str = result.stdout.split()
    current_balance = float(result_str[1])
    assert current_balance == query.get_current_balance()


@pytest.mark.parametrize(
    ("category", "year", "month", "day"),
    [
        [CategoryEnum.income.value, None, None, None],
        [CategoryEnum.income.value, 2024, None, None],
        [CategoryEnum.income.value, 2024, 5, None],
        [CategoryEnum.income.value, 2024, 5, 8],
        [CategoryEnum.expense.value, None, None, None],
        [CategoryEnum.expense.value, 2024, None, None],
        [CategoryEnum.expense.value, 2024, 5, None],
        [CategoryEnum.expense.value, 2024, 5, 8],
    ],
)
def test_app_display_args(
    category, year, month, day, get_all_time_income, get_all_time_expense
):
    """
    Tests for app display income | expense --args
    """
    args = ["display", str(category).lower()]

    # creating indexes for stdout parsing
    parsed_result_index = 4
    all_time_parsed_result_index = 8

    if year:
        args.append(f"--year={year}")
    if month:
        parsed_result_index = 5
        all_time_parsed_result_index = 9
        args.append(f"--month={month}")
    if day:
        parsed_result_index = 6
        all_time_parsed_result_index = 10
        args.append(f"--day={day}")

    result = runner.invoke(app, args=args)

    result_str = result.stdout.split()
    parsed_result = result_str[parsed_result_index]
    parsed_all_time_result = result_str[all_time_parsed_result_index]

    total_amount = query.get_categorized_filtered_data_by_period(
        category=category,
        year=year,
        month=month,
        day=day,
    )
    assert float(parsed_result) == total_amount
    assert (
        float(parsed_all_time_result) == get_all_time_income
        if category == CategoryEnum.income.value
        else get_all_time_expense
    )

    assert result.exit_code == int(ExitCodesEnum.OK)
    assert (
        "Total income"
        if category == CategoryEnum.income.value
        else "Total expense" in result.stdout
    )
    assert (
        "All time income"
        if category == CategoryEnum.income.value
        else "All time expense" in result.stdout
    )


@pytest.mark.parametrize(
    ("date", "category", "amount", "desc"),
    [
        ["2024-05-08", CategoryEnum.income.value, 30000, "Salary"],
        ["2024-05-08", CategoryEnum.expense.value, 500, "Groceries"],
        ["2024-05-08", None, None, None],
        ["2024-05-08", CategoryEnum.income.value, None, None],
        ["2024-05-08", CategoryEnum.income.value, 500.0, None],
        ["2024-05-08", CategoryEnum.income.value, 500.0, "Salary"],
    ],
)
def test_app_record_add(date, category, amount, desc):
    result = runner.invoke(
        app=app,
        args=[
            "record",
            "add",
            f"--date={date}",
            f"--category={category}",
            f"--amount={amount}",
            f"--desc={desc}",
        ],
    )

    if (date is None) or (category is None) or (amount is None):
        assert result.exit_code == int(ExitCodesEnum.ERROR)
    else:
        assert result.exit_code == int(ExitCodesEnum.OK)
        assert "You have successfully entered a new record" in result.stdout


def test_app_record_search():
    items = {
        "--date=": "2024-05-07",
        "--category=": CategoryEnum.income.value,
        "--amount=": 500,
    }

    for key, value in items.items():
        result = runner.invoke(
            app=app,
            args=["record", "search", f"{key}{value}"],
        )
        assert "Search result" in result.stdout


def test_app_record_edit():
    items = {
        "--date=": "2024-05-07",
        "--category=": CategoryEnum.income.value,
        "--amount=": 500,
    }

    for key, value in items.items():
        result = runner.invoke(
            app=app,
            args=["record", "edit", "--record-id=1", f"{key}{value}"],
        )
        assert "BEFORE EDITING" in result.stdout
        assert "AFTER EDITING" in result.stdout
