from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance
        self.__account_number = str(hash(account_holder))[:10]

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def _deduct_balance(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
            print(f"Current Balance: {self.__balance}")
        else:
            print("Deposit amount should be positive.")

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def account_type(self):
        pass

    def get_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.account_type()}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount should be positive.")

        elif amount > self.get_balance():
            print("Insufficient balance.")

        else:
            self._deduct_balance(amount)

            print(f"Savings Withdrawal: {amount}")
            print(f"Remaining Balance: {self.get_balance()}")


class CurrentAccount(BankAccount):

    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):

        service_charge = 10

        if amount + service_charge > self.get_balance():
            print("Insufficient balance including service charge.")

        else:
            self._deduct_balance(amount + service_charge)

            print(f"Current Account Withdrawal: {amount}")
            print(f"Service Charge: {service_charge}")
            print(f"Remaining Balance: {self.get_balance()}")


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_type):

        if name in self.accounts:
            print("Account already exists.")
            return

        if account_type == "savings":
            account = SavingsAccount(name)

        elif account_type == "current":
            account = CurrentAccount(name)

        else:
            print("Invalid account type.")
            return

        self.accounts[name] = account

        print(f"{account_type.capitalize()} account created.")

    def get_account(self, name):
        return self.accounts.get(name)

    def display_all_accounts(self):

        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts.values():
            account.get_account_details()
            print("-" * 30)


def main():

    bank = Bank()

    while True:

        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. View All Accounts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter account holder name: ")
            acc_type = input(
                "Enter account type (savings/current): "
            ).lower()

            bank.create_account(name, acc_type)

        elif choice == "2":

            name = input("Enter account holder name: ")
            account = bank.get_account(name)

            if account:
                amount = float(input("Amount to deposit: "))
                account.deposit(amount)

        elif choice == "3":

            name = input("Enter account holder name: ")
            account = bank.get_account(name)

            if account:
                amount = float(input("Amount to withdraw: "))
                account.withdraw(amount)

        elif choice == "4":

            name = input("Enter account holder name: ")
            account = bank.get_account(name)

            if account:
                print(
                    "Current Balance:",
                    account.get_balance()
                )

        elif choice == "5":

            name = input("Enter account holder name: ")
            account = bank.get_account(name)

            if account:
                account.get_account_details()

        elif choice == "6":

            bank.display_all_accounts()

        elif choice == "7":

            print(
                "Thank you for using the Bank Management System."
            )
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()