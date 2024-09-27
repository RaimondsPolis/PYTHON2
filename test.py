from Classes import Cilveks
from Classes import Sieviete
from Classes import Virietis
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
    # listbox.insert(Cilveks(cilveka_vards, cilveka_dzimums, cilveka_vecums))
    nomainit_sarakstu()


var = tk.Variable(value=visi_cilveki)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED
)
listbox.pack(expand=True, fill=tk.BOTH)

listbox.grid(column = 1, row = 4, **options)

def nomainit_sarakstu():
    listbox.delete(0,END)
    for cilveks in visi_cilveki:
        listbox.insert("end","{}, {}, {}".format(cilveks.name, cilveks.gender, cilveks.age))


def dzimenes_poga_clicked():
    jaunais_teksts =""
    for izveletais in listbox.curselection():
        visi_cilveki[izveletais].dzdiena()
        jaunais_teksts += visi_cilveki[izveletais].info() +"\n"
    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()

def vardamaina_clicked():
    nameChange = tk.Toplevel(root)
    nameChange.title('Vārda maiņa')
    nameChange.resizable(False, False)
    window_width = 300
    window_height = 200

    # get the screen dimension
    screen_width = nameChange.winfo_screenwidth()
    screen_height = nameChange.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    nameChange.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def jaunaisvards():
        cilveka_vards = vards.get()
        for izveletais in listbox.curselection():
            visi_cilveki[izveletais].dzdiena()
        result_label.config(text=cilveka_vards)
        nomainit_sarakstu()
        nameChange.destroy()


    jaunsvards_label = ttk.Label(nameChange, text='Jaunais vārds: ')
    jaunsvards_label.grid(column=0, row=0, sticky='W', **options)


    jvards = tk.StringVar()
    jvards_entry = ttk.Entry(nameChange, textvariable=jvards)
    jvards_entry.grid(column=1, row=0, **options)
    jvards_entry.focus()

    jvards_poga = ttk.Button(nameChange, text='Mainīt vārdu', command=jaunaisvards)
    jvards_poga.grid(column=1, row = 1, **options)


    result_label = ttk.Label(nameChange)
    result_label.grid(row=3, columnspan=3, **options)

    nameChange.grid(padx=10, pady=10)

    nameChange.mainloop()





# buttons
convert_button = ttk.Button(frame, text='Ražot cilvēku', command=convert_button_clicked)
convert_button.grid(column=2, row=0, sticky='W', **options)

dzimenes_poga = ttk.Button(frame, text='Dzimšanas diena', command=dzimenes_poga_clicked)
dzimenes_poga.grid(column=3, row=0, sticky='W', **options)

vardamaina_poga = ttk.Button(frame, text='Vārda maiņa', command=vardamaina_clicked)
vardamaina_poga.grid(column=4, row=0, sticky='W', **options)



# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()
