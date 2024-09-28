from Classes import Cilveks
import tkinter as tk
from tkinter import ttk, END

visi_cilveki = []

root = tk.Tk()
root.title("Human Manufacturer")
root.geometry('1000x500')
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

# entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)

selected_gender = tk.StringVar()
selected_gender.set("Vīrietis") #Default

# izvēles iespējas
gender_options = ["Vīrietis", "Sieviete", "Cits"]

# OptionMenu
gender_dropdown = tk.OptionMenu(frame, selected_gender, *gender_options)
gender_dropdown.grid(column=1, row=1, **options)

# cita dzimuma rakstīšanai (sākumā paslēpts)
custom_gender_label = ttk.Label(frame, text="Cits dzimums:")
custom_gender = tk.StringVar()
custom_gender_entry = ttk.Entry(frame, textvariable=custom_gender)

# parādīt/paslēpt cita dzimuma rakstīšanas lauku
def update_gender_option(value):
    if value == "Cits":
        custom_gender_label.grid(column=2, row=1, sticky='W', **options)
        custom_gender_entry.grid(column=3, row=1, **options)
    else:
        custom_gender_label.grid_forget()
        custom_gender_entry.grid_forget()

# Trigger the update when the gender is selected
selected_gender.trace_add("write", lambda *args: update_gender_option(selected_gender.get()))

# button click funkcijas n stuff
def convert_button_clicked():
    cilveka_vards = vards.get()
    cilveka_dzimums = selected_gender.get()

    if cilveka_dzimums == "Cits":
        cilveka_dzimums = custom_gender.get()

    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_dzimums, cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].info())
    nomainit_sarakstu()

# Listbox
listbox = tk.Listbox(root, height=6, selectmode=tk.EXTENDED)
listbox.grid(column=1, row=4, **options)

# listboxa atjaunināšana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for cilveks in visi_cilveki:
        listbox.insert(END, "{}, {}, {}".format(cilveks.name, cilveks.gender, cilveks.age))

# vēl nospiestu pogu funkcijas
def dzimenes_poga_clicked():
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        visi_cilveki[izveletais].dzdiena()
        jaunais_teksts += visi_cilveki[izveletais].info() + "\n"
    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()

def vardamaina_clicked():
    nameChange = tk.Toplevel(root)
    nameChange.title('Vārda maiņa')
    nameChange.resizable(False, False)
    window_width = 300
    window_height = 200

    screen_width = nameChange.winfo_screenwidth()
    screen_height = nameChange.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    nameChange.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def jaunaisvards():
        cilveka_vards = jvards.get()
        for izveletais in listbox.curselection():
            visi_cilveki[izveletais].name = cilveka_vards
        nomainit_sarakstu()
        nameChange.destroy()

    jaunsvards_label = ttk.Label(nameChange, text='Jaunais vārds:')
    jaunsvards_label.grid(column=0, row=0, sticky='W', **options)

    jvards = tk.StringVar()
    jvards_entry = ttk.Entry(nameChange, textvariable=jvards)
    jvards_entry.grid(column=1, row=0, **options)
    jvards_entry.focus()

    jvards_poga = ttk.Button(nameChange, text='Mainīt vārdu', command=jaunaisvards)
    jvards_poga.grid(column=1, row=1, **options)

    result_label = ttk.Label(nameChange)
    result_label.grid(row=3, columnspan=3, **options)

    nameChange.mainloop()

# pogas 
convert_button = ttk.Button(frame, text='Ražot cilvēku', command=convert_button_clicked)
convert_button.grid(column=2, row=0, sticky='W', **options)

dzimenes_poga = ttk.Button(frame, text='Dzimšanas diena', command=dzimenes_poga_clicked)
dzimenes_poga.grid(column=3, row=0, sticky='W', **options)

vardamaina_poga = ttk.Button(frame, text='Vārda maiņa', command=vardamaina_clicked)
vardamaina_poga.grid(column=4, row=0, sticky='W', **options)

# Result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# atstarpes no malām
frame.grid(padx=10, pady=10)

# piešķilt grabažu
root.mainloop()
