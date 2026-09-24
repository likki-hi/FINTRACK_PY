# FINTRACK_PY
Personal Expense Intelligence and Budget Management System using Python
# FINTRACK PY — Personal Expense Intelligence & Budget Management System

## Project Overview

**FINTRACK PY** is a Python-based personal finance management system developed to help users record and manage their income and expenses.

The application allows users to add transactions, categorize spending, search transactions, view financial summaries, set monthly budgets, and generate financial reports.

The project demonstrates practical Python programming concepts including **OOP, functions, exception handling, JSON file handling, list comprehensions, data validation, and unit testing**.

---

## Problem Statement

Managing personal expenses manually can make it difficult to understand spending patterns, monitor budgets, and track financial balances.

FINTRACK PY provides a simple command-line solution for recording financial transactions and generating useful summaries.

---

## Objectives

* Record income and expense transactions.
* Categorize financial transactions.
* Store transaction data using JSON.
* Search transactions using keywords.
* Calculate total income and expenses.
* Calculate the current balance.
* Identify the largest expense.
* Analyze spending by category.
* Set and monitor a monthly budget.
* Generate financial reports.
* Validate user input.
* Handle errors using exception handling.
* Test important financial functions automatically.

---

## Features

### 1. Add Transaction

Users can add:

* Income or expense
* Amount
* Category
* Date
* Description
* Payment method

### 2. View Transactions

Displays all saved financial transactions.

### 3. Search Transactions

Users can search transactions using:

* Category
* Transaction type
* Payment method
* Description

### 4. Financial Summary

Displays:

* Total income
* Total expenses
* Current balance
* Largest expense

### 5. Category Spending

Calculates total spending for each expense category.

### 6. Monthly Budget

Users can enter a monthly budget and check whether expenses are within the budget.

### 7. Financial Report

Generates a consolidated report containing income, expenses, balance, largest expense, category spending, and budget information.

### 8. JSON Data Storage

Transaction data is saved in `data.json` so that it can be loaded when the application starts.

### 9. Input Validation

The application validates important inputs such as:

* Transaction type
* Amount
* Category
* Budget

### 10. Unit Testing

The project includes automated tests using Python's built-in `unittest` framework.

---

## Technologies Used

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| Python       | Application development                |
| JSON         | Data storage                           |
| OOP          | Transaction class                      |
| unittest     | Automated testing                      |
| VS Code      | Development environment                |
| Git & GitHub | Version control and project submission |

---

## Project Structure

```text
FINTRACK_PY/
│
├── main.py
├── transaction.py
├── finance.py
├── storage.py
├── report.py
├── data.json
├── README.md
│
├── screenshots/
│
└── tests/
    └── test_fintrack.py
```

---

## Application Architecture

```text
                 FINTRACK PY
                      │
                      ▼
                 main.py
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 transaction.py   finance.py    report.py
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                  storage.py
                      │
                      ▼
                  data.json
```

### Module Description

**main.py**
Controls the application menu and user interaction.

**transaction.py**
Contains the `Transaction` class and transaction input logic.

**finance.py**
Contains financial calculation functions.

**storage.py**
Handles saving and loading transaction data using JSON.

**report.py**
Handles budget management and financial report generation.

**tests/test_fintrack.py**
Contains automated unit tests for financial calculations.

---

## Python Concepts Demonstrated

### Object-Oriented Programming

The `Transaction` class is used to represent financial transactions.

### Functions

Reusable functions are used for calculations, storage, reporting, and validation.

### List Comprehensions

List comprehensions are used to filter expense transactions.

### Exception Handling

`try-except` blocks handle invalid numeric input and file-related errors.

### JSON File Handling

Transactions are stored and retrieved using JSON.

### Lambda Functions

Lambda expressions are used to identify the largest expense.

### Unit Testing

The `unittest` framework is used to verify financial calculations.

---

## Testing

Automated testing was performed using:

```text
python -m unittest tests/test_fintrack.py -v
```

### Test Result

```text
Ran 5 tests in 0.001s

OK
```

### Tests Performed

* Total income calculation
* Total expense calculation
* Balance calculation
* Largest expense identification
* Category spending calculation

All **5 tests passed successfully**.

---

## Sample Financial Report

```text
========================================
          FINTRACK PY REPORT
========================================

Total Income   : ₹2000.00
Total Expenses : ₹3000.00
Balance        : ₹-1000.00
Largest Expense: ₹3000.00
Category       : food

---------- CATEGORY SPENDING ----------
food: ₹3000.00

========================================
```

---

## Screenshots

The following screenshots demonstrate the main features of the application:

1. Main Menu
2. Adding a Transaction
3. Transaction List
4. Financial Summary
5. Budget Status / Financial Report

Screenshots are stored in the `screenshots/` folder.

---

## Challenges Faced

* Implementing reliable user input validation.
* Handling invalid numeric input.
* Designing reusable financial calculation functions.
* Saving and loading transaction data using JSON.
* Organizing the project into multiple Python modules.
* Creating automated unit tests for financial calculations.

---

## Future Improvements

* Add a graphical user interface.
* Add monthly and yearly expense analysis.
* Add charts and visual dashboards.
* Add transaction editing and deletion.
* Add date-based filtering.
* Persist monthly budget information in JSON.
* Add CSV export functionality.
* Add authentication and multiple user profiles.

---

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd FINTRACK_PY
```

### 3. Run the application

```bash
python main.py
```

### 4. Run tests

```bash
python -m unittest tests/test_fintrack.py -v
```

---

## Project Status

**Completed**

FINTRACK PY successfully implements core personal expense management, financial analysis, budgeting, JSON storage, reporting, and automated testing features.

---

## Author

**Likitha Kalal**

Python programming
