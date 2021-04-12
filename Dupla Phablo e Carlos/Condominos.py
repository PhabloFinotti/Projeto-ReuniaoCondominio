from Banco import Banco

class Condominos(object):


	def __init__(self, cond_apartamento = 0, nome = "", telefone = "",
	email = "", usuario = "", senha = ""):
	  self.info = {}
	  self.cond_apartamento = cond_apartamento
	  self.nome = nome
	  self.telefone = telefone
	  self.email = email
	  self.usuario = usuario
	  self.senha = senha


	def insertUser(self):

	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("insert into condominos (nome, telefone, email,usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

		  banco.conexao.commit()
		  c.close()

		  return "Usuário cadastrado com sucesso!"
	  except:
		  return "Ocorreu um erro na inserção do usuário"

	def updateUser(self):

	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("update condominos set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha +  "' where cond_apartamento = " + self.cond_apartamento + " ")

		  banco.conexao.commit()
		  c.close()

		  return "Usuário atualizado com sucesso!"
	  except:
		  return "Ocorreu um erro na alteração do usuário"

	def deleteUser(self):

	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("delete from condominos where cond_apartamento = " + self.cond_apartamento + " ")

		  banco.conexao.commit()
		  c.close()

		  return "Usuário excluído com sucesso!"
	  except:
		  return "Ocorreu um erro na exclusão do usuário"

	def selectCond(self, cond_apartamento):
	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("select * from condominos where cond_apartamento = " + cond_apartamento + "  ")

		  for linha in c:
			  self.cond_apartamento = linha[0]
			  self.nome = linha[1]
			  self.telefone = linha[2]
			  self.email = linha[3]
			  self.usuario = linha[4]
			  self.senha = linha[5]

		  c.close()

		  return "Busca feita com sucesso!"
	  except:
		  return "Ocorreu um erro na busca do usuário"