from tests import Cilveks
from tests import Sieviete
from tests import Virietis
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

visi_cilveki = []



root = tk.Tk()
root.title("Human Manufacturer")
root.geometry( '500x500' )
root.resizable(False, False)

# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# temperature label
vards_label = ttk.Label(frame, text='Vārds')
vards_label.grid(column=0, row=0, sticky='W', **options)

dzimums_label = ttk.Label(frame, text='Dzimums')
dzimums_label.grid(column=0, row=1, sticky='W', **options)

vecums_label = ttk.Label(frame, text='Vecums')
vecums_label.grid(column=0, row=2, sticky='W', **options)

# vards entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

# dzimums entry

dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=1, **options)
dzimums_entry.focus()

#vecums entry

vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)
vecums_entry.focus()

# convert button


def convert_button_clicked():
    cilveka_vards = vards.get()
    cilveka_dzimums = dzimums.get()
    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_dzimums, cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].info())



    


convert_button = ttk.Button(frame, text='Ražot cilvēku')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()