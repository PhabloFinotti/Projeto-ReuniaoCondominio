import tkinter as tk
from tkinter import messagebox as mb
from reuniao import Reuniao
from tkinter import ttk

class ReuniaoView:
    
    def __init__(self,win):
        self.reuniaoCRUD = Reuniao() 

        #Local/Data/Hora
        self.localLabel = tk.Label(win, text="Local:")
        self.localEdit = tk.Entry(win, width=10, bd=3)
        self.dataLabel = tk.Label(win, text="Data:")
        self.dataEdit = tk.Entry(win, width=10, bd=3)
        self.horaLabel = tk.Label(win, text="Hora:")
        self.horaEdit = tk.Entry(win, width=9, bd=3)

        #Tema
        self.temaLabel = tk.Label(win, text="Tema")
        self.temaEdit = tk.Entry(win, width=32, bd=3)
        #Assunto
        self.assuntoLabel = tk.Label(win, text="Assunto")
        self.assuntoEdit = tk.Entry(win, width=32, bd=3)
        #self.assuntoEdit = tk.Text(win, height=6, width=24, bd=3)
        
        #Tabela Presença
        self.presencaLabel = tk.Label(win, text="Presença:")

        #Botoes
        self.btnCadastrar = tk.Button(win,
                text="Cadastrar", width=7, command=self._on_cadastrar_clicked)
        self.btnAlterar = tk.Button(win,
                text="Alterar", width=7, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(win,
                text="Excluir", width=7, command=self._on_deletar_clicked)

        #Localização dos intens na tela.
        #Local/Data/Hora
        self.localLabel.place(x=20,y=10)
        self.localEdit.place(x=10,y=30)
        self.dataLabel.place(x=90,y=10)
        self.dataEdit.place(x=80,y=30)
        self.horaLabel.place(x=160,y=10)
        self.horaEdit.place(x=150,y=30)

        #Tema
        self.temaLabel.place(x=90,y=60) 
        self.temaEdit.place(x=10,y=80) 
        #Assunto
        self.assuntoLabel.place(x=85,y=110) 
        self.assuntoEdit.place(x=10,y=130)
        #self.assuntoEdit.place(x=10,y=130)

        #Botoes
        self.btnCadastrar.place(x=10,y=240)
        self.btnAlterar.place(x=80,y=240)
        self.btnExcluir.place(x=150,y=240)

        #Tabela Presença
        self.presencaLabel.place(x=350,y=30)


    def _on_cadastrar_clicked(self):
        
        ata_tema = self.temaEdit.get()
        ata_assuntos = self.assuntoEdit.get() 

        if self.reuniaoCRUD.cadastrar(ata_tema,ata_assuntos) == True:
     
            mb.showinfo("Mensagem", "Registro executado com sucesso!")

            self.temaEdit.delete(0,tk.END)
            self.assuntoEdit.delete(0,tk.END)

        else:
            mb.showinfo("Mensagem", "Erro no Registro!")
            self.temaEdit.focus_set() 
            self.assuntoEdit.focus_set() 

    def _on_atualizar_clicked(self):
        print("Atualizando")

    def _on_deletar_clicked(self):
        print("Excluindo")


janela = tk.Tk()

principal = ReuniaoView(janela)

janela.title(" Ata de reuniao | Presença")
janela.geometry("600x270+0+0")
janela.resizable(False, False)
janela.mainloop()