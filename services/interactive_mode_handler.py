from typing_extensions import Annotated
from datetime import datetime

import typer

from utils.validator import CategoryEnum, InputValidator
from promts.promts import user_promt


class InteractiveModeHandler:

    @staticmethod
    def record_insert() -> tuple[str, str, str | float, str] | None:
        """Simple handler for new records in interactive mode"""

        # 1st step: enter date
        date = typer.prompt(
            user_promt.ask_to_enter_date(), default=datetime.now().strftime("%Y-%m-%d")
        )
        try:
            InputValidator.validate_date_format(date_str=date)
        except ValueError as error:
            typer.echo(error)
            typer.Exit()
            return

        # 2nd step: enter category
        category = typer.prompt(
            text=user_promt.ask_to_enter_category(),
            type=Annotated[str, CategoryEnum.income.value, CategoryEnum.expense.value],
            default=CategoryEnum.expense.value,
        )
        try:
            InputValidator.validate_category(category_str=category)
        except ValueError as error:
            typer.echo(error)
            typer.Exit()
            return

        # 3rd step: Enter amount
        amount = typer.prompt(user_promt.ask_to_enter_amount(), type=float)

        # 4th step: Enter description
        desc = typer.prompt(user_promt.ask_to_enter_desc(), default="")

        return date, category, amount, desc


interactive_handler = InteractiveModeHandler()
