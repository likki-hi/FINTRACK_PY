def total_income(transactions):
    return sum(
        t["amount"]
        for t in transactions
        if t["type"] == "income"
    )


def total_expenses(transactions):
    return sum(
        t["amount"]
        for t in transactions
        if t["type"] == "expense"
    )


def balance(transactions):
    return total_income(transactions) - total_expenses(transactions)


def largest_expense(transactions):
    expenses = [
        t for t in transactions
        if t["type"] == "expense"
    ]

    if not expenses:
        return None

    return max(expenses, key=lambda t: t["amount"])


def category_spending(transactions):
    categories = {}

    for t in transactions:
        if t["type"] == "expense":
            category = t["category"]

            categories[category] = categories.get(category, 0) + t["amount"]

    return categories