# bank_account.py

class BankAccount:
    def transaction_fee(self):
        return 2.5

class PremiumAccount(BankAccount):
    def transaction_fee(self):
        return 0  # Free transactions

# Usage
normal = BankAccount()
premium = PremiumAccount()
print(normal.transaction_fee())   # Output: 2.5
print(premium.transaction_fee()) # Output: 0
