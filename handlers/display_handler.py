from datetime import datetime
import typer
from promts.promts import user_promt
from storage.crud import query
from utils.validator import InputValidator
from handlers.interactive_mode import interactive_handler


class DisplayApp(typer.Typer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_balance():
        current_balance = query.get_current_balance()
        useful_financial_tip = (
            user_promt.ok_balance()
            if current_balance >= 0
            else user_promt.negative_balance()
        )
        return typer.echo(f"Balance: {current_balance}\n\n{useful_financial_tip}")

    @staticmethod
    def display_records(
        category: str,
        year: int,
        month: int,
        day: int,
        i: bool,
    ) -> str | ValueError:
        if i:
            year, month, day = interactive_handler.input_date_handler()

        InputValidator.validate_date_as_number([year, month, day])

        period_description = ""
        if year is not None:
            period_description += f"{year} "
        if month is not None:
            period_description += (
                f"{datetime.strptime(str(month), '%m').strftime('%B')} "
            )
        if day is not None:
            period_description += f"{day} "

        total_records = query.get_categorized_filtered_data_by_period(
            category, year, month, day
        )

        all_time_total = query.get_all_time_total_amount(category)

        echo_msg = (
            f"Total {category.lower()} {period_description}: {total_records}\n\n"
            if period_description
            else ""
        )

        return (
            f"{echo_msg}" f"All time {category.lower()}: {all_time_total}\n"
        )
