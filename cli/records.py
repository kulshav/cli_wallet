import csv

from datetime import datetime
from typing_extensions import Annotated

import typer

from pydantic import ValidationError

from utils.validator import InputValidator, CategoryEnum
from handlers.interactive_mode import interactive_handler
from storage.crud import query
from promts.promts import user_promt


records_app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    short_help="Use to create or edit income/expense and search for records"
)


@records_app.command(name="add", no_args_is_help=True, short_help="Use to insert new income or expense record")
def insert_record(
    date: Annotated[str, None] = datetime.now().strftime("%Y-%m-%d"),
    category: Annotated[str, None] = CategoryEnum.expense.value,
    amount: float = 0.0,
    desc: Annotated[str, None] = "",
    i: bool = False,  # Interactive mode shortened to --i for simple usages purposes
):
    """
    Example usages\n\n:
    Today Expense: record add --amount=500.00 --description="Groceries"\n
    Your date Income: record add --date=2024-05-06 --category=Income --amount=500.00 --desc="scholarship"\n\n

    record add --i for interactive mode
    """

    if i:  # User have chosen interactive mode
        try:
            date, category, amount, desc = interactive_handler.record_insert()
        except TypeError:
            return typer.Exit()
    else:
        try:
            InputValidator(date=date, category=category, amount=amount, description=desc)
        except ValidationError as error:
            typer.echo(error)
            typer.Exit()
            return

    try:
        query.insert_new_record(date=date, category=category, amount=amount, desc=desc)
    except (IOError, csv.Error) as error:
        typer.echo(error)
        typer.Exit()
        return

    return typer.echo(
        user_promt.successful_record_input(
            date=date,
            category=category,
            amount=amount,
            desc=desc,
        )
    )


@records_app.command(name="search")
def get_record():
    """Gets full data of the existing record interactively"""
    pass
