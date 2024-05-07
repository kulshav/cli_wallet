

class UserPromt:
    @staticmethod
    def ask_to_enter_date() -> str:
        return "Input date in format (YYYY-MM-DD) Press Enter(today) ->"

    @staticmethod
    def ask_to_enter_category() -> str:
        return "Input the category - (Income | Expense) Press Enter ->"

    @staticmethod
    def ask_to_enter_amount() -> str:
        return "Input the amount"

    @staticmethod
    def ask_to_enter_desc() -> str:
        return "Input the description (Press Enter to skip)"

    @staticmethod
    def wrong_date_input_format() -> str:
        return "Incorrect date format. The correct format is 'YYYY-MM-DD'\n\nUse the --help flag for assistance"

    @staticmethod
    def wrong_category_format(*args) -> str:
        return f"Invalid category!\nAvailable categories: {args}\n\nUse the --help flag for assistance"

    @staticmethod
    def negative_amount_input() -> str:
        return "You entered a negative amount.\n\nUse the --help flag for assistance"

    @staticmethod
    def input_not_number():
        return "Amount is not a number!\nThe correct format is: 1000, 1000.00\n\nUse the --help flag for assistance"

    @staticmethod
    def successful_record_input(date, category, amount, desc) -> str:
        return (
            "\n\nYou have successfully entered a new record:\n"
            f"Date: {date}\n"
            f"Category: {category}\n"
            f"Amount: {amount}\n"
            f"Description: {desc}"
        )


user_promt = UserPromt()


