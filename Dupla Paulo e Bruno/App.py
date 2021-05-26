from datetime import datetime
from Reuniao import Reuniao 

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
            self.container10 = Frame(master)
            self.container10["pady"] = 15
            self.container10.pack()

            self.titulo = Label(self.container1, text="Informe os dados : ")
            self.titulo["font"] = ("Calibri", "9", "bold")
            self.titulo.pack ()

            #Campo nome
            self.txtNome = Label(self.container2,
            text="Reunião: ", font=self.fonte, width=15)
            self.txtNome.pack(side=LEFT)

            self.txtNome = Entry(self.container2)
            self.txtNome["width"] = 10
            self.txtNome["font"] = self.fonte
            self.txtNome.pack(side=LEFT)

            
            #Campo tema
            self.txtTema = Label(self.container2,
            text="Tema: ", font=self.fonte, width=15)
            self.txtTema.pack(side=LEFT)

            self.txtTema = Entry(self.container2)
            self.txtTema["width"] = 10
            self.txtTema["font"] = self.fonte
            self.txtTema.pack(side=LEFT)

            
            #Campo local
            self.txtLocal = Label(self.container2,
            text="Local: ", font=self.fonte, width=15)
            self.txtLocal.pack(side=LEFT)

            self.txtLocal = Entry(self.container2)
            self.txtLocal["width"] = 10
            self.txtLocal["font"] = self.fonte
            self.txtLocal.pack(side=LEFT)


            
            #Campo nome
            self.txtData = Label(self.container2,
            text="Data: ", font=self.fonte, width=15)
            self.txtData.pack(side=LEFT)

            self.txtData = Entry(self.container2)
            self.txtData["width"] = 10
            self.txtData["font"] = self.fonte
            self.txtData.pack(side=LEFT)

            #Campo horario
            self.txtHorario = Label(self.container2,
            text="Horário: ", font=self.fonte, width=15)
            self.txtHorario.pack(side=LEFT)

            self.txtHorario = Entry(self.container2)
            self.txtHorario["width"] = 10
            self.txtHorario["font"] = self.fonte
            self.txtHorario.pack(side=LEFT)

        
            # Botão Cadastro
            self.btnSalvar = Button(self.container2, text="Salvar",
            font=self.fonte, width=10)
            self.btnSalvar["command"] = self.salvarReuniao
            self.btnSalvar.pack(side=RIGHT)

            # MENSAGEM, pega o return da função na Class Condomino
            self.lblmsg = Label(self.container10, text="")
            self.lblmsg["font"] = ("Verdana", "9", "italic")
            self.lblmsg.pack()

    

    def salvarReuniao(self):
        reuniao = self.preencherCampos()
        self.lblmsg["text"] = reuniao.insertReuniao()
        self.limparCampos()
    
    
    def preencherCampos(self):
        reuniao = Reuniao()
        reuniao.reuni_nome = self.txtNome.get()
        reuniao.reuni_tema = self.txtTema.get()
        reuniao.reuni_local = self.txtLocal.get()
        reuniao.reuni_data = datetime.now()
        reuniao.reuni_horario = self.txtHorario.get()
        
        return reuniao

    def limparCampos(self):
        self.txtNome.delete(0, END)
        self.txtTema.delete(0, END)
        self.txtLocal.delete(0, END)
        self.txtHorario.delete(0, END)



root = Tk()
Application(root)
root.mainloop()