from finance import (
    total_income,
    total_expenses,
    balance,
    largest_expense,
    category_spending
)


def set_budget():
    while True:
        try:
            budget = float(input("Enter monthly budget (₹): "))

            if budget <= 0:
                print("Budget must be greater than 0.")
                continue

            return budget

        except ValueError:
            print("Please enter a valid amount.")


def budget_status(transactions, budget):
    expenses = total_expenses(transactions)
    remaining = budget - expenses

    print("\n========== BUDGET STATUS ==========")
    print(f"Monthly Budget : ₹{budget:.2f}")
    print(f"Total Expenses : ₹{expenses:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")

    if remaining >= 0:
        print("Status         : Within Budget")
    else:
        print("Status         : Budget Exceeded")


def generate_report(transactions, budget=None):
    print("\n========================================")
    print("          FINTRACK PY REPORT")
    print("========================================")

    income = total_income(transactions)
    expenses = total_expenses(transactions)
    current_balance = balance(transactions)

    print(f"\nTotal Income   : ₹{income:.2f}")
    print(f"Total Expenses : ₹{expenses:.2f}")
    print(f"Balance        : ₹{current_balance:.2f}")

    largest = largest_expense(transactions)

    if largest:
        print(f"Largest Expense: ₹{largest['amount']:.2f}")
        print(f"Category       : {largest['category']}")
    else:
        print("Largest Expense: No expenses yet")

    print("\n---------- CATEGORY SPENDING ----------")

    categories = category_spending(transactions)

    if categories:
        for category, amount in categories.items():
            print(f"{category}: ₹{amount:.2f}")
    else:
        print("No expenses recorded.")

    if budget is not None:
        remaining = budget - expenses

        print("\n---------- BUDGET ----------")
        print(f"Monthly Budget : ₹{budget:.2f}")
        print(f"Remaining      : ₹{remaining:.2f}")

        if remaining >= 0:
            print("Status         : Within Budget")
        else:
            print("Status         : Budget Exceeded")

    print("\n========================================")