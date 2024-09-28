import tkinter as tk
from tkinter import ttk

def option_selected(value):
    # If "Other" is selected, show the entry box for custom gender input
    if value == "Other":
        custom_label.pack(pady=5)
        custom_entry.pack(pady=5)
    else:
        # Hide the custom gender input if not "Other"
        custom_label.pack_forget()
        custom_entry.pack_forget()
        label.config(text=f"You selected: {value}")

def submit_custom_gender():
    # Get the custom gender and display it
    custom_gender = custom_entry.get()
    label.config(text=f"You entered: {custom_gender}")

root = tk.Tk()
root.title("Gender Selection")
root.geometry("300x250")

# Create a StringVar to hold the selected option
selected_option = tk.StringVar()
selected_option.set("Select Gender")  # Default text

# List of gender options
gender_options = ["Male", "Female", "Other"]

# Create the OptionMenu dropdown
dropdown = tk.OptionMenu(root, selected_option, *gender_options, command=option_selected)
dropdown.pack(pady=20)

# Label to display the result
label = ttk.Label(root, text="")
label.pack(pady=10)

# Create label and entry for custom gender (initially hidden)
custom_label = ttk.Label(root, text="Please enter your gender:")
custom_entry = ttk.Entry(root)

root.mainloop()
