from personal_account1 import PersonalAccount


def main():
    # Create an account with user input
    account_number = int(input("Enter your account number: "))
    account_holder = input("Enter account holder name: ")
    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\n MENU ")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print(f" Deposited ${amount:.2f}")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            print(f" Current Balance: ${account.get_balance():.2f}")

        elif choice == "4":
            print("\n Transaction History:")
            account.print_transaction_history()

        elif choice == "5":
            print(" Exiting. Thank you!")
            break

        else:
            print(" Invalid option. Please try again.")


if __name__ == "__main__":
    main()
