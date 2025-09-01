class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        print(f"Current balance: {self.balance}")

    def get_account_number(self):
        return self.account_number

def main():
    print("Welcome to the Bank Account System")
    acc_num = input("Enter new account number: ")
    while True:
        try:
            init_balance = float(input("Enter initial balance: "))
            if init_balance < 0:
                print("Initial balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for balance.")
    account = BankAccount(acc_num, init_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit Amount")
        print("2. Withdraw Amount")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            account.get_balance()
        elif choice == '4':
            print("Thank you for using the Bank Account System.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()