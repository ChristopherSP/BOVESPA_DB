import sqlite3
import matplotlib.pyplot as pyplot
import time
import Tkinter as tk

conn = sqlite3.connect('BOVESPA', detect_types=sqlite3.PARSE_DECLTYPES)
conn.text_factory = str
cur = conn.cursor()

cur.execute('SELECT sigla,nome FROM ACOES order by sigla')
acoes = cur.fetchall()

acoes_sigla = [variable[0] for variable in acoes]
acoes_nome = [variable[1] for variable in acoes]

cur.execute('SELECT data,preabe,preult FROM ATRIBUTOS where id_acao = 1 order by data')
data = cur.fetchall()

date = [variable[0] for variable in data]
preabe = [variable[1] for variable in data]
preult = [variable[2] for variable in data]

frame = tk.Tk()
frame.title('Window')
frame.geometry('800x300+100+100')

b_acao = tk.Button(frame,text='Acao',width=10)
b_acao.grid(column=1,row=1)

enter = tk.Entry(frame,text='Teste')

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.grid(column=3,row=1,sticky='NS')

lst = tk.Listbox(frame,yscrollcommand=scrollbar.set,height=5)
lst.grid(column=2,row=1)

scrollbar.config(command=lst.yview)

for i in range(len(acoes_sigla)):
	lst.insert(i,acoes_sigla[i])

frame.mainloop()