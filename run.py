import typer

from cli.add import add_record_app


app = typer.Typer(no_args_is_help=True, add_completion=False)

# Register cli commands
app.add_typer(add_record_app, name="add")


# Description of an app
@app.callback()
def cli_application_description():
    """
    Simple budget tracker CLI application.
    """


if __name__ == '__main__':
    # start cli application
    app()
