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

			c.execute("update condominos set cond_apartamento = '" + self.cond_apartamento + "', cond_cpf = '" + self.cond_cpf + "', cond_nome = '" + self.cond_nome + "', cond_tppessoa = '" + self.cond_tppessoa + "', cond_rg = '" + self.cond_rg + "', cond_nascimento = '" + self.cond_nascimento + "', cond_email = '" + self.cond_email + "', cond_telresidencial = '" + self.cond_telresidencial + "', cond_telcomercial = '" + self.cond_telcomercial + "', cond_telcelular = '" + self.cond_telcelular + "', cont_adimplente = '" + self.cont_adimplente + " ")

			banco.conexao.commit()
			c.close()

			return "Usuário atualizado com sucesso!"
		except:
			return "Ocorreu um erro na alteração do usuário"

	def deleteUser(self):

		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("delete from condominos where cond_apartamento = '" + self.cond_apartamento + " ")

			banco.conexao.commit()
			c.close()

			return "Usuário excluído com sucesso!"
		except:
			return "Ocorreu um erro na exclusão do usuário"

	def selectCond(self, txtApartamento):
		banco = Banco()
		try:

			c = banco.conexao.cursor()

			c.execute("select * from condominos where cond_apartamento = '" + self.cond_apartamento + "  ")

			for linha in c:
				self.txtApartamento = linha[0]
				self.txtCPF = linha[1]
				self.txtNome = linha[2]
				self.txtTPpessoa = linha[3]
				self.txtRG = linha[4]
				self.txtNascimento = linha[5]
				self.txtEmail = linha[6]
				self.txtTelResidencia = linha[7]
				self.txtTelComercial = linha[8]
				self.txtTelCelular = linha[9]
				self.txtAdimplente = linha[10]

			c.close()

			return "Busca feita com sucesso!"
		except:
			return "Ocorreu um erro na busca do usuário"