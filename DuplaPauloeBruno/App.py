import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime
from Reuniao import Reuniao
from tkcalendar import *
from tkinter import ttk


class ReuniaoView:

    def __init__(self, win):

        self.ReuniaoCRUD = Reuniao()
        self.ReuniaoCRUD.criar()

        #self.reuniaoSelected = None
        #self.reuniaoResult = None

        #self.apartamentoSelected = None
        #self.apartamentoResult = None

        #self.temaSelected = None
        #self.temaResult = None

        #Tabela Reuniao

        self.temaLabel = tk.Label(win, text="Tema: ")
        self.temaEdit = tk.Entry(win, width=20, bd=3)

        self.localLabel = tk.Label(win, text="Local: ")
        self.localEdit = tk.Entry(win, width=15, bd=3)

        self.dataLabel = tk.Label(win, text="Data: ")
        self.dataEdit = DateEntry(win, width=10, bd=3)

        self.btnCadastrar = tk.Button(win,
                                      text="Cadastrar", width=7, command=self._on_cadastrar_clicked)
        self.btnAlterar = tk.Button(win,
                                    text="Alterar", width=7, command=self._on_alterar_clicked)
        self.btnExcluir = tk.Button(win,
                                    text="Excluir", width=7, command=self._on_excluir_clicked)

        #Localização itens

        self.temaLabel.place(x=40, y=10)
        self.temaEdit.place(x=40, y=30)

        self.localLabel.place(x=180, y=10)
        self.localEdit.place(x=180, y=30)

        self.dataLabel.place(x=300, y=10)
        self.dataEdit.place(x=300, y=30)

        #TreeView Reuniao
        self.reuniaoList = ttk.Treeview(
            win, columns=(1, 2, 3), show='headings')
        self.verscrlbar = ttk.Scrollbar(
            win, orient="vertical", command=self.reuniaoList.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.reuniaoList.configure(yscrollcommand=self.verscrlbar.set)

        self.reuniaoList.heading(1, text='ID')
        self.reuniaoList.heading(2, text='Tema')
        self.reuniaoList.heading(3, text='Local')

        self.reuniaoList.column(1, minwidth=0, width=80)
        self.reuniaoList.column(2, minwidth=0, width=130)
        self.reuniaoList.column(3, minwidth=0, width=130)
        self.reuniaoList.pack()

        self.reuniaoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)

        #Posicionar List e scroll
        self.reuniaoList.place(x=40, y=73, height=185)
        self.verscrlbar.place(x=387, y=98, height=159)

        self.carregar_dados_iniciais()

        #-> self.carregar_dados_iniciais_Ata()

        #Botoes
        self.btnCadastrar.place(x=40, y=260)
        self.btnAlterar.place(x=110, y=260)
        self.btnExcluir.place(x=180, y=260)

    def carregar_dados_iniciais(self):
        resultado = self.ReuniaoCRUD.consultar_reuniao()
        self.reuniaoList.delete(*self.reuniaoList.get_children())

        count = 0
        for registro in resultado:
            self.reuniaoList.insert('', 'end', iid=count, values=(
                str(registro[0]), str(registro[1]), (registro[2]), (registro[3])))
            count = count + 1

    def _on_mostrar_clicked(self, event):
        selection = self.reuniaoList.selection()
        item = self.reuniaoList.item(selection[0])

        data = item["values"][1]
        tema = item["values"][2]
        local = item["values"][3]
        

        self.localEdit.delete(0, tk.END)
        self.localEdit.insert(0, local)

        self.temaEdit.delete(0, tk.END)
        self.temaEdit.insert(0, tema)

        self.dataEdit.delete(0, tk.END)
        self.dataEdit.insert(0, data)

    def _on_cadastrar_clicked(self):
        tema = self.temaEdit.get()
        local = self.localEdit.get()
        data = self.dataEdit.get()

        teste = self.ReuniaoCRUD.insertReuniao( data, tema, local )

        mb.showinfo("Mensagem", teste)
        # if self.ReuniaoCRUD.insertReuniao(tema, local) == True:

            # mb.showinfo("Mensagem", "Registro executado com sucesso!")

            # self.temaEdit.delete(0, tk.END)
            # self.localEdit.delete(0, tk.END)
        # else:
            # mb.showinfo("Mensagem", "Erro no Registro!")
            # self.temaEdit.focus_set()
            # self.localEdit.focus_set()

        self.carregar_dados_iniciais()

    def _on_alterar_clicked(self):
        linhaSelecionada = self.reuniaoList.selection()
        if (len(linhaSelecionada) != 0):
            reuni_id = self.reuniaoList.item(
                linhaSelecionada[0])["values"][0]
            reuni_data = self.dataEdit.get()
            reuni_tema = self.temaEdit.get()
            reuni_local = self.localEdit.get()
            

            teste = self.ReuniaoCRUD.updateReuniao(reuni_id, reuni_data, reuni_tema, reuni_local)

            mb.showinfo("Mensagem", type(teste))
            
        """ else:
                mb.showinfo("Mensagem", "Erro no alteração!")
                self.presencaEdit.focus_set() """

        self.carregar_dados_iniciais()

    def _on_excluir_clicked(self):
        linhaSelecionada = self.reuniaoList.selection()

        if len(linhaSelecionada) != 0:
            id_presenca = self.reuniaoList.item(
                linhaSelecionada[0])["values"][0]

            if self.ReuniaoCRUD.excluirP(id_presenca):
                self.reuniaoList.delete(linhaSelecionada)

                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.presencaEdit.delete(0, tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.presencaEdit.focus_set()


    #Janela
janela = tk.Tk()
principal = ReuniaoView(janela)
janela.title("Controle de Reuniões")
janela.geometry("430x290+0+0")
janela.resizable(False, False)
janela.mainloop()
