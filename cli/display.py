import typer

from storage.crud import query
from promts.promts import user_promt

display_app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    short_help="Shows wallet data: Balance, Income, Expense"
)


@display_app.command(name="balance")
def display_current_balance():
    """
    Shows current balance
    """
    current_balance = query.get_current_balance()

    echo_msg = user_promt.ok_balance()

    # Just for giggles
    if current_balance < 0:
        echo_msg = user_promt.negative_balance()

    return typer.echo(
        f"Balance: {current_balance}\n\n"
        f"{echo_msg}"
    )

