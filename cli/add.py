from datetime import datetime

import typer
from typing_extensions import Annotated

from utils.validator import CategoryEnum

add_record_app = typer.Typer(no_args_is_help=True, add_completion=False)


# Creates new record in storage -> Income | Expense
@add_record_app.command(name="add", no_args_is_help=True)
def insert_new_record(
    date: Annotated[str, None] = datetime.now().strftime("%Y-%m-%d"),
    category: Annotated[str, None] = CategoryEnum.expense.value,
    amount: float = 0.0,
    desc: Annotated[str, None] = "",
    i: bool = False,  # Interactive mode shortened to --i for simplified usages purposes
):
    """
    Example usages:\n\n
    Today Expense: records add --amount=500.00 --description="Groceries"\n
    X date Income: records add --date=2024-05-06 --category=Income --amount=500.00 --desc="scholarship"\n\n

    records add --i for interactive mode
    """
    raise NotImplemented
