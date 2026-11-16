from bank import Bank

bank = Bank()

while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    try:
        if choice == "1":
            name = input("Enter your name: ")
            amount = float(input("Enter initial deposit: "))
            account_no = bank.create_account(name, amount)
            print("Account created successfully!")
            print("Your Account Number:", account_no)

        elif choice == "2":
            account_no = int(input("Enter account number: "))
            balance = bank.check_balance(account_no)
            print("Available Balance:", balance)

        elif choice == "3":
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            balance = bank.deposit(account_no, amount)
            print("Deposit successful!")
            print("Updated Balance:", balance)

        elif choice == "4":
            account_no = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            balance = bank.withdraw(account_no, amount)
            print("Withdrawal successful!")
            print("Updated Balance:", balance)

        elif choice == "5":
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")

    except ValueError as error:
        print("Error:", error)