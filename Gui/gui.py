
# # from tkinter import Tk, Label, PhotoImage

# # # Initialize the main window
# # root = Tk()
# # root.title("Talha GUI Window")
# # root.geometry("500x100+200+0")
# # root.minsize(200, 200)
# # root.maxsize(700, 700)

# # # Add a text label
# # label = Label(text="I am Talha")
# # label.pack()

# # # Add another text label with styling
# # label1 = Label(root, text="Hello World",
# #                fg="green", bg="#AFB42B", borderwidth=10,
# #                relief="sunken")
# # label1.pack()

# # # Load and resize the image using subsample
# # image_path = r'C:\Users\Administrator\Desktop\50-days-python\Gui\image.png'
# # photo1 = PhotoImage(file=image_path)
# # resized_photo = photo1.subsample(1, 1)  # Reduce the image size by a factor of 2

# # # Add the resized image label
# # label2 = Label(root, image=resized_photo)
# # label2.pack(side="left")

# # # Start the Tkinter event loop
# # root.mainloop()
# from tkinter import Tk, Label, PhotoImage

# # Initialize the main window
# root = Tk()
# root.title("Talha GUI Window")
# root.geometry("700x500")  # Adjusted for a larger window
# root.minsize(400, 300)  # Minimum window size
# root.maxsize(800, 600)  # Maximum window size

# # Load the background image
# image_path = r'C:\Users\Administrator\Desktop\50-days-python\Gui\image.png'
# background_image = PhotoImage(file=image_path)

# # Add the background image as a label
# background_label = Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the entire window

# # Add styled text over the background
# text_label = Label(root, text="Welcome to Talha's GUI!", 
#                    font=("Helvetica", 24, "bold"), 
#                    fg="white", bg="black", 
#                    padx=20, pady=10, borderwidth=5, relief="raised")
# text_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the text in the window

# # Start the Tkinter event loop
# root.mainloop()
from tkinter import Tk, Label, PhotoImage, Button

# Initialize the main window
root = Tk()
root.title("Talha GUI Window")
root.geometry("700x500")  # Adjusted for a larger window
root.minsize(400, 300)  # Minimum window size
root.maxsize(800, 600)  # Maximum window size

# Label to display the message
message_label = Label(root, text="", font=("Helvetica", 16), fg="black", bg="white")
message_label.place(relx=0.5, rely=0.7, anchor="center")  # Position the message below the button

# Function to handle button click
def on_button_click():
    message_label.config(text="You clicked the button!")  # Update label with a simple message

# Load and resize the background image using subsample
image_path = r'C:\Users\Administrator\Desktop\50-days-python\Gui\image.png'
background_image = PhotoImage(file=image_path)
resized_background = background_image.subsample(2, 2)  # Adjust the factor as needed

# Add the background image as a label
background_label = Label(root, image=resized_background)
background_label.place(relwidth=1, relheight=1)  # Stretch the image to cover the entire window

# Add styled text over the background
text_label = Label(root, text="Welcome to Talha's GUI!", 
                   font=("Helvetica", 20, "bold"), 
                   fg="#2c3e50", bg="#ecf0f1",  # Professional dark blue text on a light gray background
                   padx=15, pady=8, borderwidth=3, relief="raised")
text_label.place(relx=0.5, rely=0.4, anchor="center")  # Center the text in the window

# Add a button below the text
button = Button(root, text="Click Me", 
                font=("Helvetica", 14), 
                bg="#3498db", fg="white", 
                padx=10, pady=5, 
                command=on_button_click)  # Link button to function
button.place(relx=0.5, rely=0.6, anchor="center")  # Place the button below the text

# Start the Tkinter event loop
root.mainloop()

