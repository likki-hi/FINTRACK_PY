from transaction import get_transaction
from storage import load_data, save_data
from finance import (
    total_income,
    total_expenses,
    balance,
    largest_expense,
    category_spending
)
from report import set_budget, budget_status, generate_report


def view_transactions(transactions):
    print("\n========== ALL TRANSACTIONS ==========")

    if not transactions:
        print("No transactions found.")
        return

    for i, t in enumerate(transactions, start=1):
        print(f"\nTransaction {i}")
        print(f"Type           : {t['type']}")
        print(f"Amount         : ₹{t['amount']:.2f}")
        print(f"Category       : {t['category']}")
        print(f"Date           : {t['date']}")
        print(f"Description    : {t['description']}")
        print(f"Payment Method : {t['payment_method']}")


def search_transactions(transactions):
    print("\n========== SEARCH TRANSACTIONS ==========")

    keyword = input("Enter search keyword: ").strip().lower()

    results = []

    for t in transactions:
        if (
            keyword in t["category"].lower()
            or keyword in t["type"].lower()
            or keyword in t["payment_method"].lower()
            or keyword in t["description"].lower()
        ):
            results.append(t)

    if not results:
        print("No matching transactions found.")
        return

    print(f"\nFound {len(results)} transaction(s):")

    for i, t in enumerate(results, start=1):
        print(f"\nTransaction {i}")
        print(f"Type           : {t['type']}")
        print(f"Amount         : ₹{t['amount']:.2f}")
        print(f"Category       : {t['category']}")
        print(f"Date           : {t['date']}")
        print(f"Description    : {t['description']}")
        print(f"Payment Method : {t['payment_method']}")


def financial_summary(transactions):
    print("\n========== FINANCIAL SUMMARY ==========")

    income = total_income(transactions)
    expenses = total_expenses(transactions)
    current_balance = balance(transactions)

    print(f"Total Income   : ₹{income:.2f}")
    print(f"Total Expenses : ₹{expenses:.2f}")
    print(f"Balance        : ₹{current_balance:.2f}")

    largest = largest_expense(transactions)

    if largest:
        print(f"Largest Expense: ₹{largest['amount']:.2f}")
        print(f"Category       : {largest['category']}")
    else:
        print("Largest Expense: No expenses yet")


def category_summary(transactions):
    print("\n========== CATEGORY SPENDING ==========")

    categories = category_spending(transactions)

    if not categories:
        print("No expenses recorded.")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def main():

    transactions = load_data()
    budget = None

    while True:

        print("\n========================================")
        print("             FINTRACK PY")
        print("     Personal Expense Management")
        print("========================================")

        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Search Transactions")
        print("4. Financial Summary")
        print("5. Category Spending")
        print("6. Set Monthly Budget")
        print("7. Budget Status")
        print("8. Generate Report")
        print("9. Save Data")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            transaction = get_transaction()
            transactions.append(transaction)
            save_data(transactions)

        elif choice == "2":

            view_transactions(transactions)

        elif choice == "3":

            search_transactions(transactions)

        elif choice == "4":

            financial_summary(transactions)

        elif choice == "5":

            category_summary(transactions)

        elif choice == "6":

            budget = set_budget()
            print(f"✅ Monthly budget set to ₹{budget:.2f}")

        elif choice == "7":

            if budget is None:
                print("\n❌ Please set your monthly budget first.")
            else:
                budget_status(transactions, budget)

        elif choice == "8":

            generate_report(transactions, budget)

        elif choice == "9":

            save_data(transactions)

        elif choice == "10":

            save_data(transactions)
            print("\nThank you for using FINTRACK PY!")
            break

        else:

            print("❌ Invalid choice. Please select 1-10.")


if __name__ == "__main__":
    main()