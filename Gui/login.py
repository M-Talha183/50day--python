import tkinter as tk
from tkinter import messagebox

# Global variables for window size
WIDTH = 400  # Fixed width of the form
HEIGHT = 600  # Increased height to accommodate additional fields

# Function to validate sign-in
def sign_in():
    username = entry_username.get()
    password = entry_password.get()

    # Basic validation
    if not username or not password:
        messagebox.showerror("Error", "Both fields are required!")
    elif username == "admin" and password == "password123":
        messagebox.showinfo("Success", "You are successfully signed in!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to handle the Sign Up form submission
def sign_up(entry_signup_username, entry_signup_password, entry_confirm_password,
            entry_email, entry_email_2):
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    confirm_password = entry_confirm_password.get()
    email = entry_email.get()
    email_2 = entry_email_2.get()

    # Validation for Sign Up form
    if not username or not password or not confirm_password or not email or not email_2:
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    elif email != email_2:
        messagebox.showerror("Error", "Email addresses do not match!")
    else:
        messagebox.showinfo("Success", f"Account created for {username}!")

# Function to open the Sign Up window
def open_sign_up():
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry(f"{WIDTH}x{HEIGHT}")
    sign_up_window.config(bg="#f0f2f5")

    # Image for Sign Up page (replace with a valid image path)
    signup_image = tk.PhotoImage(file="D:/50-days-python/Gui/image4.png")  # Adjust the path
    image_label = tk.Label(sign_up_window, image=signup_image, bg="#f0f2f5")
    image_label.image = signup_image  # Keep a reference to avoid garbage collection
    image_label.grid(row=0, column=1, padx=30, pady=20, sticky="nsew")

    # Form container (Centered vertically and horizontally)
    form_frame = tk.Frame(sign_up_window, bg="#f0f2f5")
    form_frame.grid(row=0, column=0, padx=30, pady=20, sticky="nsew")

    # Helper function to create a labeled entry field
    def create_input_field(parent, label_text, show=""):
        label = tk.Label(parent, text=label_text, font=("Arial", 12), bg="#f0f2f5")
        label.grid(sticky="w", padx=30, pady=10)
        
        entry = tk.Entry(parent, font=("Arial", 12), bd=0, relief="solid", highlightthickness=0, highlightbackground="white", show=show)
        entry.grid(sticky="ew", padx=30, pady=5)
        
        return entry

    # Create input fields
    entry_signup_username = create_input_field(form_frame, "Username")
    entry_signup_password = create_input_field(form_frame, "Password", show="*")
    entry_confirm_password = create_input_field(form_frame, "Confirm Password", show="*")
    entry_email = create_input_field(form_frame, "Email")
    entry_email_2 = create_input_field(form_frame, "Confirm Email")

    # Configure grid row weight so that each row expands evenly
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_rowconfigure(1, weight=1)
    form_frame.grid_rowconfigure(2, weight=1)
    form_frame.grid_rowconfigure(3, weight=1)
    form_frame.grid_rowconfigure(4, weight=1)
    form_frame.grid_rowconfigure(5, weight=1)
    
    # Add an empty row after the email fields to ensure the button stays at the bottom
    form_frame.grid_rowconfigure(6, weight=0)

    # Sign Up Button (submits the form)
    btn_sign_up = tk.Button(sign_up_window, text="Sign Up", font=("Arial", 12), width=20, command=lambda: sign_up(entry_signup_username, entry_signup_password, entry_confirm_password, entry_email, entry_email_2))
    btn_sign_up.grid(row=7, column=0, columnspan=2, pady=20)

# Create the main window (Sign In Form)
root = tk.Tk()
root.title("Sign In")
root.config(bg="#f0f2f5")

# Set a fixed width and adaptive height for the window
root.geometry(f"{WIDTH}x{HEIGHT}")

# Set window icon (adjust path to your .ico file)
root.iconbitmap(r'D:/50-days-python/Gui/image4.ico')

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window
position_top = int(screen_height / 2 - HEIGHT / 2)
position_right = int(screen_width / 2 - WIDTH / 2)

# Apply the geometry with the centered position
root.geometry(f"{WIDTH}x{HEIGHT}+{position_right}+{position_top}")

# Helper function to create an entry field with a line (simulated border)
def create_input_line(master, label_text):
    label = tk.Label(master, text=label_text, font=("Arial", 12), bg="#f0f2f5")
    label.pack(pady=10, anchor="w", padx=30)
    
    entry = tk.Entry(master, font=("Arial", 12), bd=0, relief="solid", highlightthickness=0, highlightbackground="white")
    entry.pack(pady=5, padx=30, fill="x")
    
    # Draw the line manually by placing a frame under the entry widget
    line = tk.Frame(master, height=1, bg="#ccc", bd=0)
    line.pack(fill="x", padx=30, pady=5)
    
    return entry

# Username Label and Entry
entry_username = create_input_line(root, "Username")

# Password Label and Entry
entry_password = create_input_line(root, "Password")
entry_password.config(show="*")  # Make password characters hidden

# Sign In Button
btn_sign_in = tk.Button(root, text="Sign In", font=("Arial", 12), width=20, command=sign_in)
btn_sign_in.pack(pady=20)

# Sign Up Button (opens Sign Up form window) - Present only in Sign In page
sign_up_button = tk.Button(root, text="Sign Up", font=("Arial", 10), fg="#007BFF", bg="#f0f2f5", bd=0, activebackground="#f0f2f5", cursor="hand2", command=open_sign_up)
sign_up_button.pack(pady=10)

# Optional: Forgot Password button (you could link it to a reset password function)
forgot_password_button = tk.Button(root, text="Forgot Password?", font=("Arial", 8), fg="#007BFF", bg="#f0f2f5", bd=0, activebackground="#f0f2f5", cursor="hand2")
forgot_password_button.pack(pady=5)

# Run the main loop
root.mainloop()
