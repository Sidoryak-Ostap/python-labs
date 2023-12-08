import uuid
from datetime import datetime


def get_current_date():
    current_datetime = datetime.now()
    return current_datetime


class Transaction():
    def __init__(self, amount, description, date):
        self.id = uuid.uuid4()
        self.amount = amount
        self.description = description
        self.date = date


class TransactionTracker():
    def __init__(self):
        self.transaction_history = []
        with open('transaction_list.csv', 'w') as file:
            file.write("Amount, Type, Date\n")

    def write_transaction(self, transaction):
        try:
            with open('transaction_list.csv', 'a') as file:
                file.write(f"{transaction.amount},{transaction.description}, {transaction.date}\n")
        except FileNotFoundError:
            print("Error: The specified file or directory does not exist.")

        except PermissionError:
            print("Error: You don't have permission to write to the specified file.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print("File write successful.")


    def delete_transaction(self, transaction_id):
        for index, transaction in enumerate(self.transaction_history):
            if transaction.id == transaction_id:
                del self.transaction_history[index]
                return print("Transaction has been deleted successfully")

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)
        self.write_transaction(transaction)

    def display_balance(self):
        balance = 0
        for transaction in self.transaction_history:
            balance += transaction.amount
        print(f"Balance: {balance}\nDate: {get_current_date()}\n\n")


class TransactionUI():
    def __init__(self):
        transaction_tracker = TransactionTracker()
        
        while True:
            print("Transaction Menu")
            print("1. Income\n2. Expense\n3. Display balance\n4. delete transaction\n5. Exit")
            try:
                action = int(input())
                match action:
                    case 1:
                        amount = float(input("Enter the amount: "))
                        income = Transaction(amount, 'income', get_current_date())
                        transaction_tracker.add_transaction(income)
                    case 2:
                        amount = float(input("Enter the amount: "))
                        expense = Transaction(-amount, 'expense', get_current_date())
                        transaction_tracker.add_transaction(expense)
                        
                    case 3:
                        transaction_tracker.display_balance()
                    case 4: 
                        id = input("Enter transaction id")
                        transaction_tracker.delete_transaction(id)
                    case 5:
                        break
                    case _:
                        print("Incorrect operation, please choose 1 - 5")
            except ValueError as e:
                print("Incorrect operation")

        print("-----------------  PROGRAM CLOSED ---------------------")


TransactionUI()
