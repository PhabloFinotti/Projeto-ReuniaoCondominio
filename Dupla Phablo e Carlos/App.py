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
		text="Apartamento: ", font=self.fonte, width=10)
		self.lblcond_apartamento.pack(side=LEFT)

		self.txtcond_apartamento = Entry(self.container2)
		self.txtcond_apartamento["width"] = 10
		self.txtcond_apartamento["font"] = self.fonte
		self.txtcond_apartamento.pack(side=LEFT)

		self.btnBuscar = Button(self.container2, text="Buscar",
		font=self.fonte, width=10)
		self.btnBuscar["command"] = self.buscarUsuario
		self.btnBuscar.pack(side=RIGHT)

		self.lblnome = Label(self.container3, text="Nome: ",
		font=self.fonte, width=10)
		self.lblnome.pack(side=LEFT)

		self.txtnome = Entry(self.container3)
		self.txtnome["width"] = 25
		self.txtnome["font"] = self.fonte
		self.txtnome.pack(side=LEFT)

		self.lblcpf = Label(self.container3, text="CPF: ",
		font=self.fonte, width=10)
		self.lblcpf.pack(side=LEFT)

		self.txtcpf = Entry(self.container3)
		self.txtcpf["width"] = 25
		self.txtcpf["font"] = self.fonte
		self.txtcpf.pack(side=LEFT)

		self.lbltppessoa = Label(self.container4, text="Tipo Pessoa: ",
		font=self.fonte, width=10)
		self.lbltppessoa.pack(side=LEFT)

		self.txttppessoa = Entry(self.container4)
		self.txttppessoa["width"] = 3
		self.txttppessoa["font"] = self.fonte
		self.txttppessoa.pack(side=LEFT)

		self.lblrg = Label(self.container4, text="RG: ",
		font=self.fonte, width=10)
		self.lblrg.pack(side=LEFT)

		self.txtrg = Entry(self.container4)
		self.txtrg["width"] = 10
		self.txtrg["font"] = self.fonte
		self.txtrg.pack(side=LEFT)

		self.lblnascimento= Label(self.container4, text="Data de Nascimento: ",
		font=self.fonte, width=10)
		self.lblnascimento.pack(side=LEFT)

		self.txtnascimento = DateEntry(self.container5)
		self.txtnascimento["width"] = 10
		self.txtnascimento["font"] = self.fonte
		self.txtnascimento.pack(side=LEFT)


		self.lblemail= Label(self.container5, text="E-mail: ",
		font=self.fonte, width=10)
		self.lblemail.pack(side=LEFT)

		self.txtemail = Entry(self.container5)
		self.txtemail["width"] = 25
		self.txtemail["font"] = self.fonte
		self.txtemail.pack(side=LEFT)

		self.lblusuario= Label(self.container6, text="Usuário: ",
		font=self.fonte, width=10)
		self.lblusuario.pack(side=LEFT)

		self.txtusuario = Entry(self.container6)
		self.txtusuario["width"] = 25
		self.txtusuario["font"] = self.fonte
		self.txtusuario.pack(side=LEFT)

		self.lblsenha= Label(self.container7, text="Senha: ",
		font=self.fonte, width=10)
		self.lblsenha.pack(side=LEFT)

		self.txtsenha = Entry(self.container7)
		self.txtsenha["width"] = 25
		self.txtsenha["show"] = "*"
		self.txtsenha["font"] = self.fonte
		self.txtsenha.pack(side=LEFT)

		self.bntInsert = Button(self.container8, text="Inserir",
		font=self.fonte, width=12)
		self.bntInsert["command"] = self.inserirUsuario
		self.bntInsert.pack (side=LEFT)

		self.bntAlterar = Button(self.container8, text="Alterar",
		font=self.fonte, width=12)
		self.bntAlterar["command"] = self.alterarUsuario
		self.bntAlterar.pack (side=LEFT)

		self.bntExcluir = Button(self.container8, text="Excluir",
		font=self.fonte, width=12)
		self.bntExcluir["command"] = self.excluirUsuario
		self.bntExcluir.pack(side=LEFT)

		self.lblmsg = Label(self.container9, text="")
		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()


	def inserirUsuario(self):
		user = condominos()

		user.nome = self.txtnome.get()
		user.telefone = self.txttelefone.get()
		user.email = self.txtemail.get()
		user.usuario = self.txtusuario.get()
		user.senha = self.txtsenha.get()

		self.lblmsg["text"] = user.insertUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txttelefone.delete(0, END)
		self.txtemail.delete(0, END)
		self.txtusuario.delete(0, END)
		self.txtsenha.delete(0, END)



	def alterarUsuario(self):
		user = condominos()

		user.cond_apartamento = self.txtcond_apartamento.get()
		user.nome = self.txtnome.get()
		user.telefone = self.txttelefone.get()
		user.email = self.txtemail.get()
		user.usuario = self.txtusuario.get()
		user.senha = self.txtsenha.get()

		self.lblmsg["text"] = user.updateUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txttelefone.delete(0, END)
		self.txtemail.delete(0, END)
		self.txtusuario.delete(0, END)
		self.txtsenha.delete(0, END)



	def excluirUsuario(self):
		user = condominos()

		user.cond_apartamento = self.txtcond_apartamento.get()

		self.lblmsg["text"] = user.deleteUser()

		self.txtcond_apartamento.delete(0, END)
		self.txtnome.delete(0, END)
		self.txttelefone.delete(0, END)
		self.txtemail.delete(0, END)
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

		self.txttelefone.delete(0, END)
		self.txttelefone.insert(INSERT,user.telefone)

		self.txtemail.delete(0, END)
		self.txtemail.insert(INSERT, user.email)

		self.txtusuario.delete(0, END)
		self.txtusuario.insert(INSERT, user.usuario)

		self.txtsenha.delete(0, END)
		self.txtsenha.insert(INSERT,user.senha)



root = Tk()
Application(root)
root.mainloop()