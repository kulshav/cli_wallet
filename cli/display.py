import typer

display_app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    short_help="Shows wallet data: Balance, Income, Expense"
)


@display_app.command(name="balance", no_args_is_help=True, short_help="")
def display_current_balance():
    """
    Shows current balance
    """
    pass
