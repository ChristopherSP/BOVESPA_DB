from Tkinter import *

root = Tk()
root.title('Buttons')

external = Frame(root)
internal = Frame(external, borderwidth = 5, relief = "sunken", width = 200, height = 100)

stock_label = Label(external, text = "Stock:")
stock_entry = Entry(external)

scrollbar = Scrollbar(external)
lst = Listbox(external, yscrollcommand = scrollbar.set, height = 5)

scrollbar.config(command = lst.yview)

for i in range(30):
	lst.insert(i,str(i+1))

bool_preabe = BooleanVar()
bool_premax = BooleanVar()
bool_premin = BooleanVar()
bool_premed = BooleanVar()
bool_preult = BooleanVar()
bool_preofc = BooleanVar()
bool_preofv = BooleanVar()
bool_totneg = BooleanVar()
bool_quatot = BooleanVar()
bool_voltot = BooleanVar()
bool_preexe = BooleanVar()

check_preabe = Checkbutton(external, text = "Abertura", variable=bool_preabe, onvalue=True)
check_premax = Checkbutton(external, text = "Maximo", variable=bool_premax, onvalue=True)
check_premin = Checkbutton(external, text = "Minimo", variable=bool_premin, onvalue=True)
check_premed = Checkbutton(external, text = "Medio", variable=bool_premed, onvalue=True)
check_preult = Checkbutton(external, text = "Fechamento", variable=bool_preult, onvalue=True)
check_preofc = Checkbutton(external, text = "OFC", variable=bool_preofc, onvalue=True)
check_preofv = Checkbutton(external, text = "OFV", variable=bool_preofv, onvalue=True)
check_totneg = Checkbutton(external, text = "Total", variable=bool_totneg, onvalue=True)
check_quatot = Checkbutton(external, text = "Quantidade", variable=bool_quatot, onvalue=True)
check_voltot = Checkbutton(external, text = "Volume", variable=bool_voltot, onvalue=True)
check_preexe = Checkbutton(external, text = "EXE", variable=bool_preexe, onvalue=True)

ok = Button(external, text="Okay")
cancel = Button(external, text="Cancel")

external.grid(column=0, row=0, sticky=(N, S, E, W))
internal.grid(column=0, row=0, columnspan=1, rowspan=13, sticky=(N, S, E, W))

stock_label.grid(column=1, row=0, columnspan=4, sticky=(N, W), padx=5)
stock_entry.grid(column=1, row=1, columnspan=4, sticky=(N, E, W), padx=(5,0))

lst.grid(column=1, row=2, columnspan=3, sticky = (N, E, W), padx=(5,0))
scrollbar.grid(column=4,row=2, sticky= (N, S, W))

check_preabe.grid(column=1, row=8, sticky=(N, S, W))
check_premax.grid(column=2, row=8, sticky=(N, S, W))
check_premin.grid(column=3, row=8, sticky=(N, S, W))
check_premed.grid(column=1, row=9, sticky=(N, S, W))
check_preult.grid(column=2, row=9, sticky=(N, S, W))
check_preofc.grid(column=3, row=9, sticky=(N, S, W))
check_preofv.grid(column=1, row=10, sticky=(N, S, W))
check_totneg.grid(column=2, row=10, sticky=(N, S, W))
check_quatot.grid(column=3, row=10, sticky=(N, S, W))
check_voltot.grid(column=1, row=11, sticky=(N, S, W))
check_preexe.grid(column=2, row=11, sticky=(N, S, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
external.columnconfigure(0, weight=10)
external.columnconfigure(1, weight=1)
external.columnconfigure(2, weight=1)
external.columnconfigure(3, weight=1)

external.rowconfigure(12, weight=1)

root.mainloop()