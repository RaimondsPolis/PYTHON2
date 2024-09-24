from Classes import Cilveks
from Classes import Sieviete
from Classes import Virietis
import tkinter as tk
from tkinter import ttk

visi_cilveki = []

root = tk.Tk()
root.title("Human Manufacturer")
root.geometry('500x500')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# labels
vards_label = ttk.Label(frame, text='Vārds')
vards_label.grid(column=0, row=0, sticky='W', **options)

dzimums_label = ttk.Label(frame, text='Dzimums')
dzimums_label.grid(column=0, row=1, sticky='W', **options)

vecums_label = ttk.Label(frame, text='Vecums')
vecums_label.grid(column=0, row=2, sticky='W', **options)

# entries
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=1, **options)

vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)

# button click handlers
def convert_button_clicked():
    cilveka_vards = vards.get()
    cilveka_dzimums = dzimums.get()
    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_dzimums, cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].info())

def list_clicked():
    list_window = tk.Toplevel(root)
    list_window.title('Cilvēku saraksts')
    var = tk.Variable(value=[person.info2() for person in visi_cilveki])  # Convert objects to strings
    listbox = tk.Listbox(list_window, listvariable=var, height=10, selectmode=tk.EXTENDED)
    listbox.pack(expand=True, fill=tk.BOTH)

# buttons
convert_button = ttk.Button(frame, text='Ražot cilvēku', command=convert_button_clicked)
convert_button.grid(column=2, row=0, sticky='W', **options)

list_button = ttk.Button(frame, text="Cilvēku saraksts", command=list_clicked)
list_button.grid(column=2, row=1, sticky="W", **options)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()
