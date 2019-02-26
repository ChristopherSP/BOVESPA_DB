#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Tkinter as tk
import re		

# def transfer():
# 	print lst.curselection()[0],lst.get(lst.curselection()[0])
# 	text['text'] = lst.get(lst.curselection()[0])

# def search(event):
# 	lst.itemconfig(enter.get(),bg='lightgray')

''' Frame Configurations '''
frame = tk.Tk()
frame.title('Vi_Stock')

screen_width = 800#frame.winfo_screenwidth()
screen_height = 300#frame.winfo_screenheight()

frame.geometry(str(screen_width)+'x'+str(screen_height))

plot = tk.Frame(frame,height=screen_height)

''' Frame Buttons '''
'Stock Label'
acao = text = tk.Label(frame,text='Acao: ')
acao.grid(column=0,row=0)

'Error Message'
error = tk.Label(frame,text='Error: ')
error['fg'] = 'red'
#error.grid(column=1,row=2)

'Text Bar'
v = tk.StringVar(frame, value='Search: ')
enter = tk.Entry(frame,textvariable = v,bd=5)
#enter.grid(column=2,row=1,sticky='E')
#enter.bind('<Return>',search)
enter['fg'] = 'gray'

scrollbar = tk.Scrollbar(frame)

lst = tk.Listbox(frame,yscrollcommand=scrollbar.set,height=5)
#lst.grid(column=2,row=2)
#scrollbar.grid(column=3,row=2,sticky='NS')

scrollbar.config(command=lst.yview)

for i in range(30):
	lst.insert(i,str(i+1))


# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# scrollbar.config(command=lst.yview)
# lst.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
# text.pack()
# button1.pack()

frame.mainloop()
