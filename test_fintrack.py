import unittest

from finance import (
    total_income,
    total_expenses,
    balance,
    largest_expense,
    category_spending
)


class TestFinanceFunctions(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {
                "type": "income",
                "amount": 5000,
                "category": "Salary",
                "date": "2026-09-01",
                "description": "Monthly salary",
                "payment_method": "Bank"
            },
            {
                "type": "expense",
                "amount": 1500,
                "category": "Food",
                "date": "2026-09-05",
                "description": "Lunch",
                "payment_method": "UPI"
            },
            {
                "type": "expense",
                "amount": 1000,
                "category": "Travel",
                "date": "2026-09-10",
                "description": "Bus",
                "payment_method": "Cash"
            },
            {
                "type": "expense",
                "amount": 500,
                "category": "Food",
                "date": "2026-09-15",
                "description": "Dinner",
                "payment_method": "Card"
            }
        ]

    def test_total_income(self):
        self.assertEqual(total_income(self.transactions), 5000)

    def test_total_expenses(self):
        self.assertEqual(total_expenses(self.transactions), 3000)

    def test_balance(self):
        self.assertEqual(balance(self.transactions), 2000)

    def test_largest_expense(self):
        result = largest_expense(self.transactions)

        self.assertEqual(result["amount"], 1500)
        self.assertEqual(result["category"], "Food")

    def test_category_spending(self):
        result = category_spending(self.transactions)

        self.assertEqual(result["Food"], 2000)
        self.assertEqual(result["Travel"], 1000)


if __name__ == "__main__":
    unittest.main()