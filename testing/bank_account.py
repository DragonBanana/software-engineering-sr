class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)  # Start with a balance of 100

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == "__main__":
    unittest.main()

class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance
        self.transaction_fee = 2  # New feature: Transaction fee

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        total_amount = amount + self.transaction_fee
        if total_amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= total_amount

    def get_balance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)  # Start with a balance of 100

    # Existing tests
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)  # Withdraw 30 + fee 2 = 32
        self.assertEqual(self.account.get_balance(), 68)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)  # Cannot withdraw more than balance

    # New tests for transaction fee
    def test_withdraw_with_fee(self):
        self.account.withdraw(50)  # Withdraw 50 + fee 2 = 52
        self.assertEqual(self.account.get_balance(), 48)

    def test_insufficient_funds_with_fee(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(99)  # 99 + fee 2 = 101, exceeds balance

    def test_exact_balance_with_fee(self):
        self.account.withdraw(98)  # 98 + fee 2 = 100, exact balance
        self.assertEqual(self.account.get_balance(), 0)

if __name__ == "__main__":
    unittest.main()