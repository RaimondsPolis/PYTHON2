import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a Listbox inside the main window
listbox = tk.Listbox(root)
listbox.pack()

# Add items to the Listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

# Start the Tkinter event loop
root.mainloop()