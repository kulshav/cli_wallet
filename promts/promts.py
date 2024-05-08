import random


class UserPromt:
    """
    Promts messages to user
    """

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

    @staticmethod
    def negative_balance() -> str:
        return (
            "Your balance is negative!\n"
            "Maybe just spend less and earn more? It`s that simple"
        )

    @staticmethod
    def ok_balance() -> str:
        informative_tip = [
            "Just spend less and earn more!",
            "Save money -> dont buy a coffee. Ok, this time it`s just a joke chill...",
            "Max out your credit cards for that instant gratification. Who needs financial stability anyway?",
            "You dont need any retirement savings. You'll definitely want to work until you're 95.",
            "Impulsive buying is the only way to spend money. Source: Trust me bro.",
            "Don't bother with paying out loans. "
            "Ignorance is bliss, especially when creditors come knocking for your TV",
            "Why worry about compound interest when you can just compound your debt instead?",
        ]

        return f"Very very informative financial tip: {random.choice(informative_tip)}"

    @staticmethod
    def not_found_any_records() -> str:
        return "Not found any records. Maybe try harder? 😇"

    @staticmethod
    def ask_to_enter_year() -> str:
        return "Input any year as a number. Default -> current"

    @staticmethod
    def ask_to_enter_month() -> str:
        return "Input any month as a number. Default -> current"

    @staticmethod
    def ask_to_enter_day() -> str:
        return "Input any day as a number. Default -> current"

    @staticmethod
    def negative_or_zero_date() -> str:
        return "You entered a negative or zero date.\n\nUse the --help flag for assistance"

    @staticmethod
    def month_not_exists() -> str:
        return "You entered month that doesn`t exists"

    @staticmethod
    def day_not_exists() -> str:
        return "You entered day that doesn`t exists"

    @staticmethod
    def ask_to_enter_record_id() -> str:
        return "Input record ID as number. Enter to ->"

    @staticmethod
    def wrong_input_record_id() -> str:
        return "Record with entered ID doesn`t exists"

    @staticmethod
    def check_record_to_edit() -> str:
        return "Please check record before editing (y/n to continue)"

    @staticmethod
    def ask_to_enter_date_options() -> str:
        return "Input date. Enter to set unchanged ->"

    @staticmethod
    def ask_to_enter_category_options() -> str:
        return "Input category (Income, Expense). Enter to set unchanged ->"

    @staticmethod
    def ask_to_enter_amount_options() -> str:
        return "Input amount. Enter to set unchanged ->"

    @staticmethod
    def ask_to_enter_desc_options() -> str:
        return "Input description. Enter to set unchanged ->"

    @staticmethod
    def record_output_with_id(
        record_id: int,
        date: str,
        category: str,
        amount: str,
        desc: str,
    ):
        return (
            f"\nID: {record_id}\n\n"
            f"Date: {date}\n"
            f"Category: {category}\n"
            f"Amount: {amount}\n"
            f"Description: {desc}\n"
        )


user_promt = UserPromt()
