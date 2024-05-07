import typer

from cli.records import records_app
from cli.display import display_app


app = typer.Typer(no_args_is_help=True, add_completion=False)

# Register cli commands
app.add_typer(records_app, name="record")
app.add_typer(display_app, name="display")


# Description of an app
@app.callback()
def cli_application_description():
    """
    Simple budget tracker CLI application.
    """


if __name__ == '__main__':
    # start cli application
    app()
