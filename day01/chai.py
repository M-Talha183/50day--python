# from hello_chai import myFun

# myFun("zain + Talha")
#!/usr/bin/env python3

my_balance = 10000  # Dollars
my_pin = 361738

# Prompt for PIN code
pin_input = input("Enter your Pin Code: ")

if pin_input.isdigit() and int(pin_input) == my_pin:
    print("Pin is correct!!!")

    # Prompt for operation
    print("Please select an option:")
    print("1. Withdraw")
    print("2. Check Balance")
    operation = input("Enter the number corresponding to your choice: ")

    if operation == "1":  # Withdraw
        amount_input = input("Enter the amount to withdraw: ")

        if amount_input.isdigit():
            amount = int(amount_input)

            if amount > my_balance:
                print("Your required amount is greater than your current balance.")
            else:
                my_balance -= amount
                print(f"Your remaining balance is ${my_balance}")
        else:
            print("Invalid amount entered. Please enter a numeric value.")

    elif operation == "2":  # Check Balance
        print(f"Your balance is ${my_balance}")
    else:
        print("Invalid option selected.")

else:
    print("Pin is incorrect.")
