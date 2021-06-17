# from Condominos import Condominos
from tkinter import *
from tkcalendar import *


import sys
import os

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")


        # Molda os containeres que serão usados 

        self.container1 = Frame(master)
        self.container1["padx"] = 50
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 50
        self.container2["pady"] = 10
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 50
        self.container3["pady"] = 10
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 50
        self.container4["pady"] = 10
        self.container4.pack()


        self.titulo = Label(self.container1, text="Selecione qual tela quer ver ")
        self.titulo["font"] = ("Comic Sans", "15", "bold")
        self.titulo.pack ()


        ############ FEITA POR PHABLO FINOTTI E CARLOS CAVALCANTE ###########
        self.iniciarCondominos = Button(self.container2, text="Abrir Tela de Condominos",
        font=self.fonte, width=30, pady=10)
        self.iniciarCondominos["command"] = abrirTelaCondominos
        self.iniciarCondominos.pack(side=RIGHT, pady=20)


        ########### FEITA ALEX MOREIRA E GABRIEL BANDEIRA ###########
        self.iniciarAtaReunioes = Button(self.container3, text="Abrir Ata de Reuniões",
        font=self.fonte, width=30, pady=10)
        self.iniciarAtaReunioes["command"] = abrirTelaAtaReuniao
        self.iniciarAtaReunioes.pack(side=RIGHT, pady=20)


        ########### FEITA POR PAULO GUILHERME E BRUNO VIEIRA ###########
        self.iniciarTelaPresenca = Button(self.container4, text="Abrir tela Ata de Presença",
        font=self.fonte, width=30, pady=10)
        self.iniciarTelaPresenca["command"] = abrirTelaAtaPresenca
        self.iniciarTelaPresenca.pack(side=RIGHT, pady=20)


def abrirTelaCondominos():
    path = os.path.join('DuplaPhabloeCarlos', 'App.py')
    os.system('python '+ path)

def abrirTelaAtaReuniao():
    path = os.path.join('DuplaAlexeGabriel', 'ata_reuniao_view2.py')
    os.system('python '+ path)

def abrirTelaAtaPresenca():
    path = os.path.join('DuplaPauloeBruno', 'App.py')
    os.system('python '+ path)
	
root = Tk()
root.title('Tela Inicial')
root.resizable(False, False)

Application(root)
root.mainloop()