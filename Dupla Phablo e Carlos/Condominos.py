from Banco import Banco

class Condominos(object):


	def __init__(self, txtApartamento = "", txtCPF = "", txtNome = "", txtTPpessoa = "", txtRG = "", txtNascimento = "", txtEmail = "", txtTelResidencia = "", txtTelComercial = "", txtTelCelular = "", txtAdimplente):

		self.txtApartamento = txtApartamento
		self.txtCPF = txtCPF
		self.txtNome = txtNome
		self.txtTPpessoa = txtTPpessoa
		self.txtRG = txtRG
		self.txtNascimento = txtNascimento
		self.txtEmail = txtEmail
		self.txtTelResidencia = txtTelResidencia
		self.txtTelComercial = txtTelComercial
		self.txtTelCelular = txtTelCelular
		self.txtAdimplente = txtAdimplente


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

		  c.execute("update condominos set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha +  "' where txtApartamento = " + self.txtApartamento + " ")

		  banco.conexao.commit()
		  c.close()

		  return "Usuário atualizado com sucesso!"
	  except:
		  return "Ocorreu um erro na alteração do usuário"

	def deleteUser(self):

	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("delete from condominos where txtApartamento = " + self.txtApartamento + " ")

		  banco.conexao.commit()
		  c.close()

		  return "Usuário excluído com sucesso!"
	  except:
		  return "Ocorreu um erro na exclusão do usuário"

	def selectCond(self, txtApartamento):
	  banco = Banco()
	  try:

		  c = banco.conexao.cursor()

		  c.execute("select * from condominos where txtApartamento = " + txtApartamento + "  ")

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