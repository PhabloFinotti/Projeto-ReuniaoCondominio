from Condominos import Condominos
from tkinter import *
from tkcalendar import *

class Application:
	def __init__(self, master=None):
		self.fonte = ("Verdana", "8")

		self.container1 = Frame(master)
		self.container1["pady"] = 10
		self.container1.pack()
		self.container2 = Frame(master)
		self.container2["padx"] = 20
		self.container2["pady"] = 5
		self.container2.pack()
		self.container3 = Frame(master)
		self.container3["padx"] = 20
		self.container3["pady"] = 5
		self.container3.pack()
		self.container4 = Frame(master)
		self.container4["padx"] = 20
		self.container4["pady"] = 5
		self.container4.pack()
		self.container5 = Frame(master)
		self.container5["padx"] = 20
		self.container5["pady"] = 5
		self.container5.pack()
		self.container6 = Frame(master)
		self.container6["padx"] = 20
		self.container6["pady"] = 5
		self.container6.pack()
		self.container7 = Frame(master)
		self.container7["padx"] = 20
		self.container7["pady"] = 5
		self.container7.pack()
		self.container8 = Frame(master)
		self.container8["padx"] = 20
		self.container8["pady"] = 10
		self.container8.pack()
		self.container9 = Frame(master)
		self.container9["pady"] = 15
		self.container9.pack()

		self.titulo = Label(self.container1, text="Informe os dados : ")
		self.titulo["font"] = ("Calibri", "9", "bold")
		self.titulo.pack ()

		self.txtApartamento = Label(self.container2,
		text="Apartamento: ", font=self.fonte, width=15)
		self.txtApartamento.pack(side=LEFT)

		self.txtApartamento = Entry(self.container2)
		self.txtApartamento["width"] = 10
		self.txtApartamento["font"] = self.fonte
		self.txtApartamento.pack(side=LEFT)


		# Botão de Busca
		self.btnBuscar = Button(self.container2, text="Buscar",
		font=self.fonte, width=10)
		self.btnBuscar["command"] = self.buscarUsuario
		self.btnBuscar.pack(side=RIGHT)


		# Nome usuário
		self.lblNome = Label(self.container3, text="Nome: ",
		font=self.fonte, width=10)
		self.lblNome.pack(side=LEFT)

		self.txtNome = Entry(self.container3)
		self.txtNome["width"] = 25
		self.txtNome["font"] = self.fonte
		self.txtNome.pack(side=LEFT)


		# CPF Usuário
		self.lblCPF = Label(self.container3, text="CPF: ",
		font=self.fonte, width=10)
		self.lblCPF.pack(side=LEFT)

		self.txtCPF = Entry(self.container3)
		self.txtCPF["width"] = 25
		self.txtCPF["font"] = self.fonte
		self.txtCPF.pack(side=LEFT)


		# Tipo de pessoa (Física ou Jurídica)
		self.lblTPpessoa = Label(self.container4, text="Tipo Pessoa: ",
		font=self.fonte, width=13)
		self.lblTPpessoa.pack(side=LEFT)

		self.txtTPpessoa = Entry(self.container4)
		self.txtTPpessoa["width"] = 3
		self.txtTPpessoa["font"] = self.fonte
		self.txtTPpessoa.pack(side=LEFT)


		# RG do Usuário
		self.lblRG = Label(self.container4, text="RG: ",
		font=self.fonte, width=7)
		self.lblRG.pack(side=LEFT)

		self.txtRG = Entry(self.container4)
		self.txtRG["width"] = 10
		self.txtRG["font"] = self.fonte
		self.txtRG.pack(side=LEFT)


		# Data de Nascimento
		self.lblNascimento= Label(self.container4, text="Data de Nascimento: ",
		font=self.fonte, width=20)
		self.lblNascimento.pack(side=LEFT)

		self.txtNascimento = DateEntry(self.container4)
		self.txtNascimento["width"] = 10
		self.txtNascimento["font"] = self.fonte
		self.txtNascimento.pack(side=LEFT)


		# Usuário é Adimplente
		self.txtAdimplente = Checkbutton(self.container5, text='Adimplente', onvalue=1, offvalue=0)
		self.txtAdimplente["width"] = 10
		self.txtAdimplente["font"] = self.fonte
		self.txtAdimplente.pack(side=LEFT)


		# Email Usuário
		self.lblEmail= Label(self.container5, text="E-mail: ",
		font=self.fonte, width=10)
		self.lblEmail.pack(side=LEFT)

		self.txtEmail = Entry(self.container5)
		self.txtEmail["width"] = 25
		self.txtEmail["font"] = self.fonte
		self.txtEmail.pack(side=LEFT)

		# Título dos Telefones
		self.tituloTel = Label(self.container6, text="Informe os telefones : ")
		self.tituloTel["font"] = ("Calibri", "9", "bold")
		self.tituloTel.pack ()

		#Telefone Residência
		self.lblTelResidencia= Label(self.container6, text="Residencial: ",
		font=self.fonte, width=10)
		self.lblTelResidencia.pack(side=LEFT)

		self.txtTelResidencia = Entry(self.container6)
		self.txtTelResidencia["width"] = 25
		self.txtTelResidencia["font"] = self.fonte
		self.txtTelResidencia.pack(side=LEFT)


		#Telefone Comercial
		self.lblTelComercial= Label(self.container7, text="Comercial: ",
		font=self.fonte, width=10)
		self.lblTelComercial.pack(side=LEFT)

		self.txtTelComercial = Entry(self.container7)
		self.txtTelComercial["width"] = 25
		self.txtTelComercial["font"] = self.fonte
		self.txtTelComercial.pack(side=LEFT)


		#Telefone Celular
		self.lblTelCelular= Label(self.container8, text="Celular: ",
		font=self.fonte, width=10)
		self.lblTelCelular.pack(side=LEFT)

		self.txtTelCelular = Entry(self.container8)
		self.txtTelCelular["width"] = 25
		self.txtTelCelular["show"] = "*"
		self.txtTelCelular["font"] = self.fonte
		self.txtTelCelular.pack(side=LEFT)


		#Botão inserir
		self.btnInsert = Button(self.container9, text="Inserir",
		font=self.fonte, width=12)
		self.btnInsert["command"] = self.inserirUsuario
		self.btnInsert.pack (side=LEFT)


		#Botão Alterar Dados do banco (UPDATE)
		self.btnAlterar = Button(self.container9, text="Alterar",
		font=self.fonte, width=12)
		self.btnAlterar["command"] = self.alterarUsuario
		self.btnAlterar.pack (side=LEFT)

		#Botão Deletar Dados do banco (DELETE)
		self.btnExcluir = Button(self.container9, text="Excluir",
		font=self.fonte, width=12)
		self.btnExcluir["command"] = self.excluirUsuario
		self.btnExcluir.pack(side=LEFT)


		# MENSAGEM, pega o return da função na Class Condomino
		self.lblmsg = Label(self.container9, text="")
		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()


	def inserirUsuario(self):
		user = Condominos()

		user.txtApartamento = self.txtApartamento.get()
		user.txtCPF = self.txtCPF.get()
		user.txtNome = self.txtNome.get()
		user.txtTPpessoa = self.txtTPpessoa.get()
		user.txtRG = self.txtRG.get()
		user.txtNascimento = self.txtNascimento.get()
		user.txtEmail = self.txtEmail.get()
		user.txtTelResidencia = self.txtTelResidencia.get()
		user.txtTelComercial = self.txtTelComercial.get()
		user.txtTelCelular = self.txtTelCelular.get()
		user.txtAdimplente = self.txtAdimplente.get()

		self.lblmsg["text"] = user.insertUser()

		self.txtApartamento.delete(0, END)
		self.txtCPF.delete(0, END)
		self.txtNome.delete(0, END)
		self.txtTPpessoa.delete(0, END)
		self.txtRG.delete(0, END)
		self.txtNascimento.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtTelResidencia.delete(0, END)
		self.txtTelComercial.delete(0, END)
		self.txtTelCelular.delete(0, END)
		self.txtAdimplente.delete(0, END)


	def alterarUsuario(self):
		user = Condominos()

		user.txtApartamento = self.txtApartamento.get()
		user.txtCPF = self.txtCPF.get()
		user.txtNome = self.txtNome.get()
		user.txtTPpessoa = self.txtTPpessoa.get()
		user.txtRG = self.txtRG.get()
		user.txtNascimento = self.txtNascimento.get()
		user.txtEmail = self.txtEmail.get()
		user.txtTelResidencia = self.txtTelResidencia.get()
		user.txtTelComercial = self.txtTelComercial.get()
		user.txtTelCelular = self.txtTelCelular.get()
		user.txtAdimplente = self.txtAdimplente.get()

		self.lblmsg["text"] = user.updateUser()

		self.txtApartamento.delete(0, END)
		self.txtCPF.delete(0, END)
		self.txtNome.delete(0, END)
		self.txtTPpessoa.delete(0, END)
		self.txtRG.delete(0, END)
		self.txtNascimento.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtTelResidencia.delete(0, END)
		self.txtTelComercial.delete(0, END)
		self.txtTelCelular.delete(0, END)
		self.txtAdimplente.delete(0, END)



	def excluirUsuario(self):
		user = Condominos()

		user.txtApartamento = self.txtApartamento.get()

		self.lblmsg["text"] = user.deleteUser()

		self.txtApartamento.delete(0, END)
		self.txtCPF.delete(0, END)
		self.txtNome.delete(0, END)
		self.txtTPpessoa.delete(0, END)
		self.txtRG.delete(0, END)
		self.txtNascimento.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtTelResidencia.delete(0, END)
		self.txtTelComercial.delete(0, END)
		self.txtTelCelular.delete(0, END)
		self.txtAdimplente.delete(0, END)


	def buscarUsuario(self):
		user = Condominos()

		user.txtApartamento = self.txtApartamento.get()

		self.lblmsg["text"] = user.selectCond(apartamento)


		self.txtApartamento.delete(0, END)
		self.txtApartamento.insert(INSERT, user.apartamento)

		self.txtCPF.delete(0, END)
		self.txtCPF.insert(INSERT, user.txtCPF)

		self.txtNome.delete(0, END)
		self.txtNome.insert(INSERT, user.txtNome)

		self.txtTPpessoa.delete(0, END)
		self.txtTPpessoa.insert(INSERT, user.txtTPpessoa)

		self.txtRG.delete(0, END)
		self.txtRG.insert(INSERT, user.txtRG)

		self.txtNascimento.delete(0, END)
		self.txtNascimento.insert(INSERT, user.txtNascimento)

		self.txtEmail.delete(0, END)
		self.txtEmail.insert(INSERT, user.txtEmail)

		self.txtTelResidencia.delete(0, END)
		self.txtTelResidencia.insert(INSERT, user.txtTelResidencia)

		self.txtTelComercial.delete(0, END)
		self.txtTelComercial.insert(INSERT, user.txtTelComercial)

		self.txtTelCelular.delete(0, END)
		self.txtTelCelular.insert(INSERT, user.txtTelCelular)

		self.txtAdimplente.delete(0, END)
		self.txtAdimplente.insert(INSERT, user.txtAdimplente)


root = Tk()
Application(root)
root.mainloop()