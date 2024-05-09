import typer
from click.exceptions import Exit

from handlers.interactive_mode import interactive_handler
from promts.promts import user_promt
from storage.crud import query, StorageDataEnum
from utils.validator import InputValidator


class RecordApp(typer.Typer):
    """
    Record app business-logic handler for all 'record' subcommands

    'record COMMAND --SUBCOMMAND'
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def insert_record(
        date: str = None,
        category: str = None,
        amount: float = None,
        desc: str = None,
        i: bool = False,
    ):
        if not i:
            InputValidator.validate_date_format(date)
            InputValidator.validate_category(category)
            InputValidator.validate_amount(amount)
        else:
            # User have chosen interactive mode
            date, category, amount, desc = interactive_handler.record_insert_handler()

        query.insert_new_record(date=date, category=category, amount=amount, desc=desc)

        return date, category, amount, desc

    @staticmethod
    def search_records(
        date: str,
        category: str,
        amount: float,
        desc: str,
    ) -> str:
        search_result_data = query.get_record_filtered(date, category, amount, desc)
        InputValidator.validate_search_data(search_result_data)

        search_result_message = "Search result:"
        for record in search_result_data:
            search_result_message += (
                f"\n\n"
                f"{user_promt.record_output_with_id(
                    record_id=record[StorageDataEnum.record_id],
                    date=record[StorageDataEnum.date],
                    category=record[StorageDataEnum.category],
                    amount=record[StorageDataEnum.amount],
                    desc=record[StorageDataEnum.desc]
                )}"
            )
        return search_result_message

    @staticmethod
    def edit_record(
        record_id: int,
        date: str,
        category: str,
        amount: float,
        desc: str,
        i: bool,
    ) -> str | Exit | ValueError:

        if not i:
            record_to_edit = query.get_record_data_by_id(record_id)
            # InputValidator.validate_record_id(record_id)
            # InputValidator.validate_date_format(date)
            # InputValidator.validate_category(category)
            # InputValidator.validate_amount(amount)
            InputValidator.validate_record_data(record_to_edit)

            typer.echo(
                f"--BEFORE EDITING--\n"
                f"{user_promt.record_output_with_id(
                    record_id=record_id,
                    date=record_to_edit[StorageDataEnum.date],
                    category=record_to_edit[StorageDataEnum.category],
                    amount=record_to_edit[StorageDataEnum.amount],
                    desc=record_to_edit[StorageDataEnum.desc],
                )}\n\n"
                f"--AFTER EDITING--\n"
                f"{user_promt.record_output_with_id(
                    record_id=record_id,
                    date=date,
                    category=category,
                    amount=amount,
                    desc=desc)}",
            )

            # Editing process confirmation from user, default = Exit app
            if not typer.prompt(
                user_promt.check_record_to_edit(), default="n", type=bool
            ):
                return Exit()
        else:
            record_id, date, category, amount, desc = (
                interactive_handler.input_edit_record_handler()
            )

        query.edit_record_by_id(
            record_id=record_id,
            updated_data={
                StorageDataEnum.date: date,
                StorageDataEnum.category: category,
                StorageDataEnum.amount: amount,
                StorageDataEnum.desc: desc,
            },
        )

        return user_promt.record_output_with_id(
            record_id=record_id,
            date=date,
            category=category,
            amount=amount,
            desc=desc,
        )
