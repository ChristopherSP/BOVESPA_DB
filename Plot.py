import sqlite3
import matplotlib.pyplot as pyplot
import time

conn = sqlite3.connect('BOVESPA', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

cur.execute('SELECT data,preabe,preult FROM atributos where id_acao = 1 order by data')
data = cur.fetchall()

date = [date[0] for date in data]
preabe = [preabe[1] for preabe in data]
preult = [preult[2] for preult in data]

pyplot.ion()
pyplot.subplot(2,1,1)
pyplot.plot(date,preabe,'b-')

pyplot.xlabel('Ano')
pyplot.ylabel('Preco')

pyplot.subplot(2,1,2)
pyplot.plot(date,preult,'r-')

pyplot.xlabel('Ano')
pyplot.ylabel('Preco')

#pyplot.ion()
#pyplot.figure(1)
#pyplot.plot(date,preabe)
# aux = len(date)
# while pyplot.fignum_exists(1):
# 	try:
# 		pyplot.plot(date[aux+1],preabe[aux+1],'bo-')
# 	except:
# 		time.sleep(0.1)


#pyplot.show()

#if plt.fignum_exists(<figure number>):
    # Figure is still opened
#else:
    # Figure is closed
    # no windows

#if plt.get_fignums():
    # window(s) open
#else:

conn.commit()
cur.close()