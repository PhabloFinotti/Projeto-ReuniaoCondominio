from Banco import Banco
import sqlite3
from datetime import datetime

class Condominos(object):


	def __init__(self, txtApartamento = "", txtCPF = "", txtNome = "", txtTPpessoa = "", txtRG = "", txtNascimento = "", txtEmail = "", txtTelResidencia = "", txtTelComercial = "", txtTelCelular = "", resTxtAdimplente = bool):

		self.cond_apartamento = txtApartamento
		self.cond_cpf = txtCPF
		self.cond_nome = txtNome
		self.cond_tppessoa = txtTPpessoa
		self.cond_rg = txtRG
		self.cond_nascimento = txtNascimento
		self.cond_email = txtEmail
		self.cond_telresidencial = txtTelResidencia
		self.cond_telcomercial = txtTelComercial
		self.cond_telcelular = txtTelCelular

		self.cond_adimplente = resTxtAdimplente


	def insertUser(self):

		banco = Banco()

		##Data do Cadastro
		time = datetime.now().strftime("%B %d, %Y %I:%M%p")

		try:

			c = banco.conexao.cursor()

			c.execute("insert into condominos (cond_apartamento, cond_cpf, cond_nome, cond_tppessoa, cond_rg, cond_nascimento, cond_email, cond_telresidencial, cond_telcomercial, cond_telcelular, cond_adimplente, cond_data_cadastro) values ('" + self.cond_apartamento + "', '" + self.cond_cpf + "', '" + self.cond_nome + "', '" + self.cond_tppessoa + "', '" + self.cond_rg + "', '" + self.cond_nascimento + "', '" + self.cond_email + "', '" + self.cond_telresidencial + "', '" + self.cond_telcomercial + "', '" + self.cond_telcelular + "', '" + str(self.cond_adimplente) + "', '" + str(time) + "' )")

			banco.conexao.commit()
			c.close()

			return "Usuário cadastrado com sucesso!"
		except sqlite3.Error as erro:
			return "Ocorreu um erro na inserção do usuário", erro

	def updateUser(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()


			c.execute("update condominos set cond_apartamento = '" + self.cond_apartamento + "', cond_cpf = '" + self.cond_cpf + "', cond_nome = '" + self.cond_nome + "', cond_tppessoa = '" + self.cond_tppessoa + "', cond_rg = '" + self.cond_rg + "', cond_nascimento = '" + self.cond_nascimento + "', cond_email = '" + self.cond_email + "', cond_telresidencial = '" + self.cond_telresidencial + "', cond_telcomercial = '" + self.cond_telcomercial + "', cond_telcelular = '" + self.cond_telcelular + "', cond_adimplente = '" + str(self.cond_adimplente) + "' where cond_apartamento = '" + self.cond_apartamento + "'")			
		
			banco.conexao.commit()
			c.close()

			return "Usuário atualizado com sucesso!"
		except sqlite3.Error as erro:
			return "Ocorreu um erro na alteração do usuário", erro

	def deleteUser(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("delete from condominos where cond_apartamento = '" + self.cond_apartamento + "'")

			banco.conexao.commit()
			c.close()

			return "Usuário excluído com sucesso!"
		except sqlite3.Error as erro:
			return "Ocorreu um erro na exclusão do usuário", erro



	#Busca no banco de dados
	def selectCond(self, cond_apartamento = ""):
		banco = Banco()
 
		try:

			c = banco.conexao.cursor()

			c.execute("select * from condominos where cond_apartamento = '" + self.cond_apartamento + "'")

			# registros = c.fetchall()
			

			for linha in c:
				self.cond_apartamento = linha[1]
				self.cond_cpf = linha[2]
				self.cond_nome = linha[3]
				self.cond_tppessoa = linha[4]
				self.cond_rg = linha[5]
				self.cond_nascimento = linha[6]
				self.cond_email = linha[7]
				self.cond_telresidencial = linha[8]
				self.cond_telcomercial = linha[9]
				self.cond_telcelular = linha[10]
				self.cond_adimplente = int(linha[11])

			c.close()

			return "Busca feita com sucesso!"
		except sqlite3.Error as erro:
			return "Ocorreu um erro na busca do usuário", erro
