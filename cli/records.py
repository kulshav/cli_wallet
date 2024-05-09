from datetime import datetime

from click.exceptions import Exit
from typing_extensions import Annotated

import typer

from handlers.records_handler import RecordApp
from utils.validator import CategoryEnum
from promts.promts import user_promt


records_app = RecordApp(
    no_args_is_help=True,
    add_completion=False,
    short_help="Use to create, search or edit income/expense records",
)


@records_app.command(
    name="add",
    no_args_is_help=True,
    short_help="Use to insert new income or expense record",
)
def insert_record(
    date: Annotated[str, None] = datetime.now().strftime("%Y-%m-%d"),
    category: Annotated[str, None] = CategoryEnum.expense.value,
    amount: float = 0.0,
    desc: Annotated[str, None] = "",
    i: bool = False,  # Interactive mode shortened to --i for simple usages purposes
):
    """
    Example usages:\n\n
    Today Expense: record add --amount=500.00 --description="Groceries"\n
    Your date Income: record add --date=2024-05-06 --category=Income --amount=500.00 --desc="scholarship"\n\n

    record add --i for interactive mode
    """
    try:
        validated_record = records_app.insert_record(date, category, amount, desc, i)
        return typer.echo(
            user_promt.successful_record_input(
                date=validated_record[0],
                category=validated_record[1],
                amount=validated_record[2],
                desc=validated_record[3],
            )
        )
    except (ValueError, TypeError) as error:
        typer.echo(error)
        typer.Exit()


@records_app.command(
    name="search",
    no_args_is_help=True,
    short_help="Use to search by date | category | amount",
)
def find_records(
    date: Annotated[str, None] = None,
    category: Annotated[str, None] = None,
    amount: float = None,
    desc: str = None,
) -> None | Exit:
    """
    Searching for specific records

    search --date=2024-02-02 --category=Expense --amount=500.00 --desc="Groceries"

    --i interactive search (Recommended)
    """
    try:
        echo_msg = records_app.search_records(date, category, amount, desc)
        return typer.echo(echo_msg)
    except ValueError as error:
        typer.echo(error)
        return typer.Exit()


@records_app.command(
    name="edit",
    no_args_is_help=True,
    short_help="Use to edit any record, requires record_id",
)
def edit_records(
    record_id: Annotated[int, None] = None,
    date: Annotated[str, None] = None,
    category: Annotated[str, None] = None,
    amount: float = None,
    desc: str = None,
    i: bool = False,  # Interactive mode shortened to --i for simple usages purposes
):
    """
    Edits any record by its ID\n
    If you need to know record_id -> use 'record search'\n\n

    Edit without checking record (Not recommended)\n
    edit --record-id=1 --date=2024-02-02 --category=Expense --amount=500.00 --desc="Groceries"\n\n

    --i for interactive mode (Recommended)
    """
    try:
        echo_msg = records_app.edit_record(record_id, date, category, amount, desc, i)
        return typer.echo(f"Record successfully updated!\n\n{echo_msg}")
    except (ValueError, TypeError) as error:
        typer.echo(error)
        return typer.Exit()
