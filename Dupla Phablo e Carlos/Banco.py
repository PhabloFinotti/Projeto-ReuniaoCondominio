#importando módulo do SQlite
import sqlite3

class Banco():

	def __init__(self):
		self.conexao = sqlite3.connect('banco.db')
		self.createTable()

	def createTable(self):
		c = self.conexao.cursor()

		c.execute("""create table if not exists condominos (
					 id integer primary key autoincrement ,
					 txtApartamento int,
					 txtCPF varchar(14),
					 txtNome varchar(255),
					 txtTPpessoa varchar(20),
					 txtRG varchar(20),
					 txtNascimento date,
					 txtEmail varchar(50),
					 txtTelResidencia varchar(11),
					 txtTelComercial varchar(11),
					 txtTelCelular varchar(11),
					 txtAdimplente bit,
					 cond_data_cadastro datetime)""")

		self.conexao.commit()
		c.close()