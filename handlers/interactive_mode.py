from click.exceptions import Exit
from typing_extensions import Annotated
from datetime import datetime

import typer

from storage.crud import query
from storage.core import StorageDataEnum
from utils.validator import CategoryEnum, InputValidator
from promts.promts import user_promt


class InteractiveModeHandler:
    """
    CLI app business-logic handler for interactive mode

    'record COMMAND --i'
    """

    @staticmethod
    def record_insert_handler() -> tuple[str, str, str | float, str] | ValueError:
        """
        Handler for creating new records in interactive mode.
        Uses step-by-step validation.

        :returns tuple[date, category, amount, desc] -> on success\n
        :raises ValueError -> if validation failed\n
        """

        # 1st step: get date from input and validate
        date = typer.prompt(
            user_promt.ask_to_enter_date(), default=datetime.now().strftime("%Y-%m-%d")
        )
        InputValidator.validate_date_format(date)

        # 2nd step: get category from input and validate
        category = typer.prompt(
            text=user_promt.ask_to_enter_category(),
            type=Annotated[str, CategoryEnum.income, CategoryEnum.expense],
            default=str(CategoryEnum.expense.value),
        )
        InputValidator.validate_category(category)

        # 3rd step: get amount from input and validate
        amount = typer.prompt(user_promt.ask_to_enter_amount(), type=float)
        InputValidator.validate_amount(amount)

        # 4th step: get description from input
        desc = typer.prompt(user_promt.ask_to_enter_desc(), default="")

        return date, category, amount, desc

    @staticmethod
    def input_date_handler() -> tuple[int, int, int]:
        """
        Handler for interactive date input: Year, Month, Day

        Included validation on CLI level
        :returns tuple[year, month, day]
        """

        year = typer.prompt(
            user_promt.ask_to_enter_year(),
            default=datetime.now().year,
        )

        month = typer.prompt(
            user_promt.ask_to_enter_month(),
            default=datetime.now().month,
        )

        day = typer.prompt(
            user_promt.ask_to_enter_day(),
            default=datetime.now().day,
        )

        return year, month, day

    @staticmethod
    def input_edit_record_handler() -> Exit | ValueError | tuple:
        """
        Handler for interactive editing existing record.\n
        Uses step-by-step validation.

        :returns tuple[record_id, date, category, amount, desc] -> on success\n
        :raises ValueError -> if validation failed\n
        :raises Exit -> If user declined editing process
        """

        # 1st step: Enter record_id and validate input
        record_id = typer.prompt(
            user_promt.ask_to_enter_record_id(), type=int, default=0
        )
        InputValidator.validate_record_id(record_id)

        # Get data from provided record_id, validate if exists, then continue
        record_to_edit = query.get_record_data_by_id(record_id)
        InputValidator.validate_record_data(record_to_edit)

        typer.echo(
            user_promt.record_output_with_id(
                record_id=record_id,
                date=record_to_edit[StorageDataEnum.date],
                category=record_to_edit[StorageDataEnum.category],
                amount=record_to_edit[StorageDataEnum.amount],
                desc=record_to_edit[StorageDataEnum.desc],
            )
        )

        # Asking to confirm editing, default - stop!
        confirmation = typer.prompt(user_promt.check_record_to_edit(), default="n", type=bool)
        if not confirmation:
            return Exit()

        # 3rd step: get date from input and validate
        date = typer.prompt(
            user_promt.ask_to_enter_date_options(),
            default=record_to_edit[StorageDataEnum.date],
        )
        InputValidator.validate_date_format(date)

        # 4th step: get category from input and validate
        category = typer.prompt(
            text=user_promt.ask_to_enter_category_options(),
            type=Annotated[str, CategoryEnum.income, CategoryEnum.expense],
            default=record_to_edit[StorageDataEnum.category],
        )
        InputValidator.validate_category(category)

        # 5th step: get amount from input and validate
        amount = typer.prompt(
            user_promt.ask_to_enter_amount_options(),
            type=float,
            default=record_to_edit[StorageDataEnum.amount],
        )
        InputValidator.validate_amount(amount)

        # 6th step: get description from input
        desc = typer.prompt(
            user_promt.ask_to_enter_desc_options(),
            default=record_to_edit[StorageDataEnum.desc],
        )

        return record_id, date, category, amount, desc


interactive_handler = InteractiveModeHandler()
