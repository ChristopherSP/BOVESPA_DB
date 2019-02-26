import sqlite3

conn = sqlite3.connect('BOVESPAteste')
conn.text_factory = str
cur = conn.cursor()

fname = raw_input('Enter file name: ')

if len(fname)<1: fname = 'DemoCotacoesHistoricas12022003.txt'

pasta = '/home/user/Downloads/Hist_Bovespa/'

with open(pasta+fname,'r') as file:
	lines = file.readlines()
	for line in lines[1:-1]: 
		identi_id = int(line[0:2])
		data = line[2:6] + '-' + line[6:8] + '-' + line[8:10]
		codbdi_id = int(line[10:12])
		acoes_sigla = line[12:24].strip()
		tpmerc_id = int(line[24:27])
		acoes_nome = line[27:39].strip()
		especi_sigla = line[39:49].strip()
		try:
			prazot = int(line[49:52])
		except:
			prazot = None
		moeda = line[52:56].strip()
		preabe = float(line[56:69])/100
		premax = float(line[69:82])/100
		premin = float(line[82:95])/100
		premed = float(line[95:108])/100
		preult = float(line[108:121])/100
		preofc = float(line[121:134])/100
		preofv = float(line[134:147])/100
		totneg = int(line[147:152])
		quatot = int(line[152:170])
		voltot = float(line[170:188])/100
		preexe = float(line[188:201])/100
		indopc_id = int(line[201])
		datven =  line[202:206] + '-' + line[206:208] + '-' + line[208:210]
		fatcot = int(line[210:217])
		ptoexe = float(line[217:230])/1000000
		dismes = int(line[242:245])

		cur.execute('INSERT OR IGNORE INTO ESPECI(sigla) VALUES(?)',(especi_sigla,))
		cur.execute('INSERT OR IGNORE INTO MODREF(moeda) VALUES(?)',(moeda,))
		cur.execute('INSERT OR IGNORE INTO ACOES(sigla,nome) VALUES(?,?)',(acoes_sigla,acoes_nome))

		cur.execute('SELECT id FROM ESPECI WHERE sigla = ?',(especi_sigla,))
		especi_id = cur.fetchone()[0]

		cur.execute('SELECT id FROM MODREF WHERE moeda = ?',(moeda,))
		moeda_id = cur.fetchone()[0]
		
		cur.execute('SELECT id FROM ACOES WHERE sigla = ?',(acoes_sigla,))
		acoes_id = cur.fetchone()[0]

		cur.execute('''INSERT INTO ATRIBUTOS(data,prazot,preabe,premax,premin,premed,preult,
			preofc,preofv,totneg,quatot,voltot,preexe,datven,fatcot,ptoexe,dismes,id_identi,
			id_codbdi,id_especi,id_modref,id_indopc,id_tpmerc,id_acao) 
			VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(data,prazot,preabe,
			premax,premin,premed,preult,preofc,preofv,totneg,quatot,voltot,preexe,datven,fatcot,
			ptoexe,dismes,identi_id,codbdi_id,especi_id,moeda_id,indopc_id,tpmerc_id,acoes_id))
		
conn.commit()
cur.close()
file.close()