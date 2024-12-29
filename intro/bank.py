class BankAccount:
    # Class attribute shared by all accounts
    bank_name = "Python Bank"
    
    # Constructor method to initialize an account
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0  # Initial balance
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    # Method to get the current balance
    def get_balance(self):
        return self.balance
    
    # Method to transfer money to another account
    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"Transferred {amount} to {other_account.account_holder}.")
        else:
            print("Transfer failed. Check the amount and balance.")

# Example usage
# Create two accounts
account1 = BankAccount("Alice", "12345")
account2 = BankAccount("Bob", "67890")

# Display bank name
print("Bank:", BankAccount.bank_name)

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.transfer(100, account2)

# Check balances
print(f"{account1.account_holder}'s Balance: {account1.get_balance()}")
print(f"{account2.account_holder}'s Balance: {account2.get_balance()}")