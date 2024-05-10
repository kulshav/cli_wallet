<h1 align="center"> CLI Wallet</h1>

[![Automated tests](https://github.com/kulshav/cli_wallet/actions/workflows/run_tests.yml/badge.svg?branch=master)](https://github.com/kulshav/cli_wallet/actions/workflows/run_tests.yml)

<p align="center">
<i>Simple cli wallet powered by <a href="https://github.com/tiangolo/typer">Typer</a> that helps you to track budget. 
Uses csv file as storage for all your expense/income records</i>
</p>

## Table of contents

- [Features](#features)
- [Installation](#installation)
- [Example of Usages](#example-usages)


# **Features**
- Creating income or expense
- Searching or editing your income or expense record
- Analytics: current balance, income, expense
- Providing direct input or interactive mode with step-by-step input


# **Installation**

**1. Clone the repository**
```bash
git clone https://github.com/kulshav/cli_wallet
```

**2. Create .env file from .env.dist as example**
```bash
# Default path to storage. Set own if you want
PATH_TO_STORAGE=data/records.csv
DEBUG_LOG_PATH=logs/debug.log
```

**3. Create and activate virtual environment**

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

**4. Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
**5. Run app**

By default, it will display --help message
```bash
python3 run.py
```

# Example usages

You can use flag ```--help``` to any available command and subcommand to get an example of command usages.

You can use flag ```--i``` to enter interactive mode aka step-by-step input.

### Basic scenario usage
```bash
python3 run.py COMMAND SUBCOMMAND --ARGS
```

_Simple examples of usages provided below_

### 1. Display command

#### 1.1 Get current balance
```bash
python3 run.py display balance
```
#### 1.2 Get income (same for expense) 

All time income
```bash
python3 run.py display income
```
Income for specific period
```bash
python3 run.py display income --year=2024
> Total income 2024: 31000 
 
python3 run.py display income --month=5
> Total income 2024 May: 31000

python3 run.py display income --day=7
> Total income 2024 May 7: 31000

python3 run.py display income --year=2023 --month=12 --day=31
> Total income 2023 January 31: 0
```

_Tired of typing? Just use interactive mode_
```bash
python3 run.py display income --i

# Interactive mode example. Use enter to choose default option, or just enter whatever you need
> Input any year as a number. Default -> [2024]: Enter
> Input any month as a number. Default -> [5]: Enter
> Input any day as a number. Default -> current [7]: Enter

> Total inc2024 May 9 : 31000
```

### 2. Record command

#### 2.1 Insert new record
```bash
python3 run.py record add --date=2024-05-09 --category=Income --amount=500 --desc="Scolarship"

> You have successfully entered a new record:
Date: 2024-05-09
Category: Income
Amount: 500.0
Description: Scolarship
```

_Tired of typing? Again? Use interactive mode_
```bash
python3 run.py record add --i
> Input date in format (YYYY-MM-DD) Press Enter(today) -> [2024-05-09]: Enter
> Input the category - (Income | Expense) Press Enter -> [Expense]: Enter
> Input the amount: 500
> Input the description (Press Enter to skip) []: "Scolarship"

> You have successfully entered a new record:
Date: 2024-05-09
Category: Expense
Amount: 500.0
Description: Scolarship
```

#### 2.2 Search for existing record
```bash
python3 run.py record search --date=2024-02-02 --category=Expense --amount=500.00 --desc="Groceries"

> Search result:
ID: 3
Date: 2024-05-07
Category: Expense
Amount: 500.0
Description: Groceries
```

You also can search just by any criteria you want
```bash
python3 run.py record search --date=2024-02-02
> Search result:
ID: 3
Date: 2024-05-07
Category: Expense
Amount: 500.0
Description: Groceries
```

#### 2.3 Editing existing record

You can use provided ID in record search to edit this record

_NOTE: interactive mode recommended_

```bash
python3 run.py record edit --i
> Input record ID as number. Enter to -> [Exit]: 3
# You will be promt to check if you want to edit this recordd
>
ID: 3
Date: 2024-05-07
Category: Expense
Amount: 500.0
Description: Groceries

Please check record before editing (y/n to continue) [n]: y

> Input date. Enter to set unchanged -> [2024-05-07]: 2024-05-08
> Input category (Income, Expense). Enter to set unchanged -> [Expense]: Enter  # Wont be changing thios
> Input amount. Enter to set unchanged -> [500.0]: 1000
> Input description. Enter to set unchanged -> [Groceries]: Enter # Wont be changing that

>
Record successfully updated!

ID: 3
Date: 2024-05-08
Category: Expense
Amount: 1000.0
Description: Groceries
```

Or you cant just be a risky guy and go with full args
```bash
python3 run.py record edit --date=2024-05-08 --category=Expense --amount=1000 --desc="Groceries"
```







