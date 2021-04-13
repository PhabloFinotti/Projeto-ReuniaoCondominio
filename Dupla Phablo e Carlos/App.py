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

		self.lblcond_apartamento = Label(self.container2,
		text="Apartamento: ", font=self.fonte, width=15)
		self.lblcond_apartamento.pack(side=LEFT)

		self.txtcond_apartamento = Entry(self.container2)
		self.txtcond_apartamento["width"] = 10
		self.txtcond_apartamento["font"] = self.fonte
		self.txtcond_apartamento.pack(side=LEFT)


		# Botão de Busca
		self.btnBuscar = Button(self.container2, text="Buscar",
		font=self.fonte, width=10)
		self.btnBuscar["command"] = self.buscarUsuario
		self.btnBuscar.pack(side=RIGHT)


		# Nome usuário
		self.lblnome = Label(self.container3, text="Nome: ",
		font=self.fonte, width=10)
		self.lblnome.pack(side=LEFT)

		self.txtnome = Entry(self.container3)
		self.txtnome["width"] = 25
		self.txtnome["font"] = self.fonte
		self.txtnome.pack(side=LEFT)


		# CPF Usuário
		self.lblcpf = Label(self.container3, text="CPF: ",
		font=self.fonte, width=10)
		self.lblcpf.pack(side=LEFT)

		self.txtcpf = Entry(self.container3)
		self.txtcpf["width"] = 25
		self.txtcpf["font"] = self.fonte
		self.txtcpf.pack(side=LEFT)


		# Tipo de pessoa (Física ou Jurídica)
		self.lbltppessoa = Label(self.container4, text="Tipo Pessoa: ",
		font=self.fonte, width=13)
		self.lbltppessoa.pack(side=LEFT)

		self.txttppessoa = Entry(self.container4)
		self.txttppessoa["width"] = 3
		self.txttppessoa["font"] = self.fonte
		self.txttppessoa.pack(side=LEFT)


		# RG do Usuário
		self.lblrg = Label(self.container4, text="RG: ",
		font=self.fonte, width=7)
		self.lblrg.pack(side=LEFT)

		self.txtrg = Entry(self.container4)
		self.txtrg["width"] = 10
		self.txtrg["font"] = self.fonte
		self.txtrg.pack(side=LEFT)


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

		self.lblmsg = Label(self.container9, text="")
		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()


	def inserirUsuario(self):
		user = condominos()

		user.nome = self.txtnome.get()
		user.telefone = self.txtTelefone.get()
		user.email = self.txtEmail.get()
		user.usuario = self.txtusuario.get()
		user.senha = self.txtsenha.get()

		self.lblmsg["text"] = user.insertUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtTelefone.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtusuario.delete(0, END)
		self.txtsenha.delete(0, END)



	def alterarUsuario(self):
		user = condominos()

		user.cond_apartamento = self.txtcond_apartamento.get()
		user.nome = self.txtnome.get()
		user.Telefone = self.txtTelefone.get()
		user.Email = self.txtEmail.get()
		user.usuario = self.txtusuario.get()
		user.senha = self.txtsenha.get()

		self.lblmsg["text"] = user.updateUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtTelefone.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtusuario.delete(0, END)
		self.txtsenha.delete(0, END)



	def excluirUsuario(self):
		user = condominos()

		user.cond_apartamento = self.txtcond_apartamento.get()

		self.lblmsg["text"] = user.deleteUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txtTelefone.delete(0, END)
		self.txtEmail.delete(0, END)
		self.txtusuario.delete(0, END)
		self.txtsenha.delete(0, END)


	def buscarUsuario(self):
		user = condominos()

		cond_apartamento = self.txtcond_apartamento.get()

		self.lblmsg["text"] = user.selectCond(cond_apartamento)

		self.txtcond_apartamento.delete(0, END)
		self.txtcond_apartamento.insert(INSERT, user.cond_apartamento)

		self.txtnome.delete(0, END)
		self.txtnome.insert(INSERT, user.nome)

		self.txtTelefone.delete(0, END)
		self.txtTelefone.insert(INSERT,user.Telefone)

		self.txtEmail.delete(0, END)
		self.txtEmail.insert(INSERT, user.Email)

		self.txtusuario.delete(0, END)
		self.txtusuario.insert(INSERT, user.usuario)

		self.txtsenha.delete(0, END)
		self.txtsenha.insert(INSERT,user.senha)



root = Tk()
Application(root)
root.mainloop()