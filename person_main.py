from personal_account1 import PersonalAccount


def main():

    account = PersonalAccount(33456, "Islam")


    account.deposit(900)
    account.withdraw(300)
    account + 200
    account - 100


    print(account)
    print("\nTransaction History:")
    account.print_transaction_history()


    print("\nCurrent Balance:", account.get_balance())


if __name__ == "__main__":
    main()
