import tkinter as tk
from tkinter import ttk

# Global list to store names
name_list = []

# Function to update the Listbox with current names
def update_listbox():
    listbox.delete(0, 'end')  # Clear current items in Listbox
    for name in name_list:
        listbox.insert('end', name)  # Insert each name into the Listbox

# Function to add a name to the list
def add_name():
    name = name_var.get()
    if name:
        name_list.append(name)
        name_var.set('')  # Clear entry field
        update_listbox()  # Update Listbox with the new name
        result_label.config(text=f"Added: {name}")

# Function to open a new window to modify a selected name
def open_modify_window():
    selected_index = listbox.curselection()
    if not selected_index:
        result_label.config(text="Select a name to modify.")
        return

    index = selected_index[0]  # Get the index of the selected name

    modify_window = tk.Toplevel(root)
    modify_window.title("Modify Name")

    # Label and Entry to modify the selected name
    tk.Label(modify_window, text="New Name:").pack(pady=5)
    new_name_var = tk.StringVar()
    new_name_entry = tk.Entry(modify_window, textvariable=new_name_var)
    new_name_entry.pack(pady=5)
    
    # Function to modify the name in the list
    def modify_name():
        new_name = new_name_var.get()
        if new_name:
            name_list[index] = new_name
            modify_window.destroy()
            update_listbox()  # Update the Listbox with modified name
            result_label.config(text=f"Modified: {new_name}")
        else:
            result_label.config(text="New name cannot be empty.")

    # Button to confirm modification
    tk.Button(modify_window, text="Modify Name", command=modify_name).pack(pady=5)

# Set up main window
root = tk.Tk()
root.title("Name List Manager")
root.geometry("300x300")

# Entry field to input name
name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack(pady=10)

# Button to add name to the list
add_button = ttk.Button(root, text="Add Name", command=add_name)
add_button.pack(pady=5)

# Listbox to display names
listbox = tk.Listbox(root, height=10)
listbox.pack(pady=10, expand=True, fill=tk.BOTH)

# Button to open the modify window
modify_button = ttk.Button(root, text="Modify Name", command=open_modify_window)
modify_button.pack(pady=5)

# Label to show the result
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
