from datetime import datetime
from typing import Annotated

import typer

from typer import Exit

from utils.validator import CategoryEnum
from handlers.display_handler import DisplayApp


display_app = DisplayApp(
    no_args_is_help=True,
    add_completion=False,
    short_help="Shows wallet data: Balance, Income, Expense",
)


@display_app.command(name="balance")
def balance_command():
    """
    Shows current balance
    """
    return display_app.get_balance()


@display_app.command(name="income")
def income_command(
    year: Annotated[int, None] = datetime.now().year,
    month: Annotated[int, None] = None,
    day: Annotated[int, None] = None,
    i: bool = False,  # Interactive mode shortened to --i for simple usage purposes
) -> None | Exit:
    """
    Shows total income with optional filters by year, month, and day.

    Whole year --year=2024\n
    Whole month of current year --month=12\n
    Whole day of current month&year --day=5\n\n

    --i for interactive mode
    """
    try:
        message_result = display_app.display_records(
            CategoryEnum.income, year, month, day, i
        )
        return typer.echo(message_result)
    except ValueError as error:
        typer.echo(error)
        typer.Exit()


@display_app.command(name="expense")
def expense_command(
    year: Annotated[int, None] = datetime.now().year,
    month: Annotated[int, None] = None,
    day: Annotated[int, None] = None,
    i: bool = False,  # Interactive mode shortened to --i for simple usage purposes
) -> None | Exit:
    """
    Shows total expenses with optional filters by year, month, and day.

    Whole year --year=2024\n
    Whole month of current year --month=12\n
    Whole day of current month&year --day=5\n

    --i for interactive mode
    """
    try:
        message_result = display_app.display_records(
            CategoryEnum.expense, year, month, day, i
        )
        return typer.echo(message_result)
    except ValueError as error:
        typer.echo(error)
        typer.Exit()
