import tkinter as tk
from tkinter import messagebox

# Account details (for simulation purposes)
account_number = "12345"
pin = "6789"
balance = 1000.0

# Function to verify the login credentials
def verify_login():
    entered_account = entry_account.get()
    entered_pin = entry_pin.get()

    if entered_account == account_number and entered_pin == pin:
        login_frame.pack_forget()  # Hide the login screen
        show_main_screen()  # Show the main ATM screen
    else:
        messagebox.showerror("Login Failed", "Incorrect Account or PIN")

# Function to display the main screen after login
def show_main_screen():
    main_frame.pack(fill="both", expand=True)
    lbl_balance.config(text=f"Balance: ${balance}")
    # Show the transaction buttons
    btn_deposit.pack(pady=10)
    btn_withdraw.pack(pady=10)
    btn_exit.pack(pady=20)

# Function to handle deposit
def deposit():
    try:
        amount = float(entry_amount.get())
        global balance
        balance += amount
        entry_amount.delete(0, tk.END)
        lbl_balance.config(text=f"Balance: ${balance}")
        messagebox.showinfo("Deposit Successful", f"${amount} deposited successfully!")
        show_main_screen()  # Return to main screen after deposit
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

# Function to handle withdrawal
def withdraw():
    try:
        amount = float(entry_amount.get())
        global balance
        if amount <= balance:
            balance -= amount
            entry_amount.delete(0, tk.END)
            lbl_balance.config(text=f"Balance: ${balance}")
            messagebox.showinfo("Withdrawal Successful", f"${amount} withdrawn successfully!")
            show_main_screen()  # Return to main screen after withdrawal
        else:
            messagebox.showerror("Insufficient Funds", "Not enough balance to withdraw!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

# Function to exit the ATM session
def exit_atm():
    root.quit()

# Function to show the transaction screen (Deposit or Withdraw) with the input field for amount
def show_transaction_screen(transaction_type):
    global current_transaction
    current_transaction = transaction_type

    # Hide the transaction buttons (Deposit, Withdraw, Exit)
    btn_deposit.pack_forget()
    btn_withdraw.pack_forget()
    btn_exit.pack_forget()

    # Show the amount entry field
    lbl_amount.pack(pady=10)
    entry_amount.pack(pady=5)
    
    # Show the keypad and transaction buttons in one row
    show_keypad_and_buttons()

# Function to show the numeric keypad and transaction buttons
def show_keypad_and_buttons():
    keypad_frame.pack(pady=10)
    
    # Creating the numeric keypad (1-9)
    for i in range(3):
        for j in range(3):
            button = tk.Button(keypad_frame, text=str(3 * i + j + 1), font=("Arial", 14), width=5, height=2,
                               command=lambda num=3 * i + j + 1: append_number(num), relief="flat", bg="#BDC3C7", fg="#2C3E50", borderwidth=2, highlightbackground="#2C3E50")
            button.grid(row=i, column=j)

    # Add the last row for 0, Clear, and Enter
    tk.Button(keypad_frame, text="0", font=("Arial", 14), width=5, height=2, command=lambda: append_number(0), relief="flat", bg="#BDC3C7", fg="#2C3E50", borderwidth=2, highlightbackground="#2C3E50").grid(row=3, column=0)
    tk.Button(keypad_frame, text="Clear", font=("Arial", 14), width=5, height=2, command=clear_input, relief="flat", bg="#95A5A6", fg="white", borderwidth=2, highlightbackground="#2C3E50").grid(row=3, column=1)
    tk.Button(keypad_frame, text="Enter", font=("Arial", 14), width=5, height=2, command=submit_amount, relief="flat", bg="#27AE60", fg="white", borderwidth=2, highlightbackground="#2C3E50").grid(row=3, column=2)

    # Transaction buttons placed below the keypad
    btn_deposit.grid(row=4, column=0, padx=10, pady=10)
    btn_withdraw.grid(row=4, column=1, padx=10, pady=10)
    btn_exit.grid(row=4, column=2, padx=10, pady=10)

# Function to append a number to the input
def append_number(num):
    current_text = entry_amount.get()
    entry_amount.delete(0, tk.END)
    entry_amount.insert(tk.END, current_text + str(num))

# Function to clear the input field
def clear_input():
    entry_amount.delete(0, tk.END)

# Function to submit the amount (Deposit or Withdraw)
def submit_amount():
    amount = entry_amount.get()
    if current_transaction == "deposit":
        deposit()
    elif current_transaction == "withdraw":
        withdraw()

# Function to cancel the current transaction and return to the main screen
def cancel_transaction():
    entry_amount.delete(0, tk.END)
    keypad_frame.pack_forget()  # Hide the keypad
    show_main_screen()  # Return to main screen after cancellation

# Create the main window
root = tk.Tk()
root.title("ATM Machine")
root.geometry("400x600")
root.config(bg="#2C3E50")  # Dark Charcoal background for a professional look

# Login screen (initially displayed)
login_frame = tk.Frame(root, bg="#34495E")  # Dark Charcoal background for login screen
login_frame.pack(fill="both", expand=True)

# Account number and PIN labels and entry fields
lbl_account = tk.Label(login_frame, text="Account Number:", font=("Arial", 14), bg="#34495E", fg="white")
lbl_account.pack(pady=10)
entry_account = tk.Entry(login_frame, font=("Arial", 14), bg="#BDC3C7", fg="#2C3E50")  # Light Gray input field
entry_account.pack(pady=5)

lbl_pin = tk.Label(login_frame, text="PIN:", font=("Arial", 14), bg="#34495E", fg="white")
lbl_pin.pack(pady=10)
entry_pin = tk.Entry(login_frame, font=("Arial", 14), show="*", bg="#BDC3C7", fg="#2C3E50")  # Light Gray input field
entry_pin.pack(pady=5)

# Login button
btn_login = tk.Button(login_frame, text="Login", font=("Arial", 14), bg="#27AE60", fg="white", command=verify_login)
btn_login.pack(pady=20)

# Main screen (hidden until login)
main_frame = tk.Frame(root, bg="#2C3E50")  # Dark Charcoal background for main frame

# Balance label
lbl_balance = tk.Label(main_frame, text=f"Balance: ${balance}", font=("Arial", 18), bg="#2C3E50", fg="white")
lbl_balance.pack(pady=20)

# Buttons for transaction options
btn_deposit = tk.Button(main_frame, text="Deposit", font=("Arial", 14), bg="#27AE60", fg="white", command=lambda: show_transaction_screen("deposit"))  # Green for Deposit
btn_withdraw = tk.Button(main_frame, text="Withdraw", font=("Arial", 14), bg="#E74C3C", fg="white", command=lambda: show_transaction_screen("withdraw"))  # Red for Withdraw
btn_exit = tk.Button(main_frame, text="Exit", font=("Arial", 14), bg="#F39C12", fg="white", command=exit_atm)  # Yellow for Exit

# Amount input field (hidden initially)
lbl_amount = tk.Label(main_frame, text="Enter Amount:", font=("Arial", 14), bg="#2C3E50", fg="white")
entry_amount = tk.Entry(main_frame, font=("Arial", 14), bg="#BDC3C7", fg="#2C3E50")  # Light Gray input field

# Keypad frame (hidden initially)
keypad_frame = tk.Frame(main_frame, bg="#34495E")  # Dark Charcoal for keypad background

# Start the application
root.mainloop()
