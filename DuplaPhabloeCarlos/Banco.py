#importando módulo do SQlite
import sqlite3

class Banco():

	def __init__(self):
		self.conexao = sqlite3.connect('../banco.db')
		self.createTable()

	def createTable(self):
		c = self.conexao.cursor()

		c.execute("""create table if not exists condominos (
					 id integer primary key autoincrement ,
					 cond_apartamento int,
					 cond_cpf varchar(14),
					 cond_nome varchar(255),
					 cond_tppessoa varchar(20),
					 cond_rg varchar(20),
					 cond_nascimento date,
					 cond_email varchar(50),
					 cond_telresidencial varchar(11),
					 cond_telcomercial varchar(11),
					 cond_telcelular varchar(11),
					 cond_adimplente bit,
					 cond_data_cadastro datetime)""")

		self.conexao.commit()
		c.close()
