from amount import Amount


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            transaction = Amount("DEPOSIT", amount)
            self.transactions.append(transaction)
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            transaction = Amount("WITHDRAWAL", amount)
            self.transactions.append(transaction)
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self
