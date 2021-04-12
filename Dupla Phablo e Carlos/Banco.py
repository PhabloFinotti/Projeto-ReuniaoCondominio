#importando módulo do SQlite
import sqlite3

class Banco():

	def __init__(self):
		self.conexao = sqlite3.connect('banco.db')
		self.createTable()

	def createTable(self):
		c = self.conexao.cursor()

		c.execute("""create table if not exists condominos (
					 cond_apartamento integer primary key autoincrement ,
					 cond_apartamento int,
					 cond_cpf varchar(255),
					 cond_tppessoa varchar(20),
					 cond_rg varchar(20),
					 cond_nascimento date,
					 cond_email varchar(50),
					 cond_tel_resid varchar(11),
					 cond_tel_com varchar(11),
					 cond_tel_cel varchar(11),
					 cond_data_cadastro datetime,
					 cond_adimplente bit)""")
		self.conexao.commit()
		c.close()