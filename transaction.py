from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount, category, date, description, payment_method):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.payment_method = payment_method

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
            "payment_method": self.payment_method
        }


def get_transaction():
    print("\n========== ADD TRANSACTION ==========")

    while True:
        transaction_type = input("Type (income/expense): ").strip().lower()

        if transaction_type in ["income", "expense"]:
            break

        print("Please enter income or expense.")

    while True:
        try:
            amount = float(input("Amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    date = input("Date (YYYY-MM-DD): ").strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    description = input("Description: ").strip()

    payment_method = input(
        "Payment Method (Cash/UPI/Card/Bank): "
    ).strip()

    transaction = Transaction(
        transaction_type,
        amount,
        category,
        date,
        description,
        payment_method
    )

    print("\n✅ Transaction added successfully!")

    return transaction.to_dict()