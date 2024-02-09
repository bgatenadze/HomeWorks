class BankAccount:
    def __init__(self, username, password, initial_balance=0):
        self.username = username
        self._password = password if len(password) >= 8 else "DefaultPwd"
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.balance += amount
        print(f"Deposited ${amount}. Remaining balance: ${self.balance}")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, target_account, amount):
        """Transfer funds to another account if sufficient funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} to {target_account.username}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds for transfer.")

    def show_balance(self):
        """Display the current account balance."""
        print(f"Current balance for {self.username}: ${self.balance}")

    def __repr__(self):
        """String representation of the BankAccount object."""
        return f"BankAccount(username='{self.username}', balance=${self.balance})"


# Example usage:
if __name__ == "__main__":
    # Creating two bank accounts
    account1 = BankAccount(username="user1", password="securepassword", initial_balance=1000)
    account2 = BankAccount(username="user2", password="strongpwd", initial_balance=500)

    # Depositing, withdrawing, transferring, and showing balance
    account1.deposit(200)
    account1.withdraw(50)
    account1.show_balance()

    account2.show_balance()
    account1.transfer(account2, 100)
    account2.show_balance()

    # Testing __repr__ method
    print(repr(account1))
    print(repr(account2))
