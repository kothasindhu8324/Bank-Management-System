from models import Account
class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
    def create_account(self, name, amount):
        if not name.strip():
            raise ValueError("Name is required")
        if amount < 0:
            raise ValueError("Invalid amount")
        account_no = self.next_account_number
        self.next_account_number += 1
        account = Account(account_no, name, amount)
        self.accounts[account_no] = account
        return account_no
    def check_balance(self, account_no):
        if account_no not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_no].balance
    def deposit(self, account_no, amount):
        if account_no not in self.accounts:
            raise ValueError("Account not found")
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.accounts[account_no].balance += amount
        return self.accounts[account_no].balance
    def withdraw(self, account_no, amount):
        if account_no not in self.accounts:
            raise ValueError("Account not found")
        account = self.accounts[account_no]
        if amount <= 0:
            raise ValueError("Invalid amount")
        if account.balance < amount:
            raise ValueError("Insufficient balance")
        account.balance -= amount
        return account.balance