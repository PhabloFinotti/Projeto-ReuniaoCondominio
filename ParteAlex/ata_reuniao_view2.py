import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from ata_reuniao import Ata_Reuniao
# from Condominos import Condominos
from tkinter import ttk

class Ata_ReuniaoView:
    
    def __init__(self,win):

        self.ata_reuniaoCRUD = Ata_Reuniao()
        # self.CondoCRUD = Condominos() 
        self.reuniaoCRUD = Ata_Reuniao()

        #self.ata_reuniaoCRUD.criar()

        self.apartamentoSelected = None
        self.apartamentoResult = None

        self.temaSelected = None
        self.temaResult = None

        #Tabela ATA
        #Tema
        self.temaLabel = tk.Label(win, text="Tema")
        self.temaCombo = ttk.Combobox(win, width=15, values=[])
        self.temaCombo.bind("<<ComboboxSelected>>", self._on_combo_changed_Tema)

        self.popular_combo_Ata()

        #Assunto
        self.assuntoLabel = tk.Label(win, text="Assunto")
        self.assuntoEdit = tk.Text(win, height=3, width=24, bd=3)
        self.assuntoEdit.pack()


        #Tabela Presença
        self.presencaLabel = tk.Label(win, text="Presença:")
        self.presencaCombo = ttk.Combobox(win, width=8, values=["Presente","Ausente"])
        self.presencaCombo.bind("<<ComboboxSelected>>")

        self.apartamentoLabel = tk.Label(win, text="N° AP:")
        self.apartamentoCombo = ttk.Combobox(win, width=2, values=[])
        self.apartamentoCombo.bind("<<ComboboxSelected>>", self._on_combo_changed_ap)


        self.popular_combo_apartamento()

        #Botoes
        self.btnCadastrar = tk.Button(win,
                text="Cadastrar", width=7, command=self._on_cadastrar_clicked)
        self.btnAlterar = tk.Button(win,
                text="Alterar", width=7, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(win,
                text="Excluir", width=7, command=self._on_deletar_clicked)
        #Presenca
        self.btnConfirma = tk.Button(win,
                text="Confirmar", width=7, command=self._on_confirma_clicked)
        self.btnAlterarP = tk.Button(win,
                text="Alterar", width=7, command=self._on_alterar_clicked)
        self.btnExcluirP = tk.Button(win,
                text="Excluir", width=7, command=self._on_excluir_clicked)

        #Localização itens

        #Tabela ATA 
        self.temaLabel.place(x=90,y=10) 
        self.temaCombo.place(x=52,y=30) 

        self.assuntoLabel.place(x=85,y=58) 
        self.assuntoEdit.place(x=10,y=78)

        #TreeView ATA
        self.ata_reuniaoList = ttk.Treeview(win, columns=(1,2), show='headings')
        self.verscrlbar_ata = ttk.Scrollbar(win,orient="vertical", command=self.ata_reuniaoList.yview)
        self.verscrlbar_ata.pack(side = 'right', fill='x')
        self.ata_reuniaoList.configure(yscrollcommand = self.verscrlbar_ata.set)

        self.ata_reuniaoList.heading(1, text='ID')
        self.ata_reuniaoList.heading(2, text='Lista de Assuntos')

        self.ata_reuniaoList.column(1, minwidth=0, width=0)
        self.ata_reuniaoList.column(2, minwidth=0, width=195)
        self.ata_reuniaoList.pack()

        self.ata_reuniaoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked_Ata)

        #Posicionar List e scroll
        self.ata_reuniaoList.place(x=10,y=145, height= 80)
        self.verscrlbar_ata.place(x=208,y=150, height=74)

        

        #Tabela Presença
        self.presencaLabel.place(x=357,y=10)
        self.presencaCombo.place(x=360,y=30)

        self.apartamentoLabel.place(x=277,y=10)
        self.apartamentoCombo.place(x=280,y=30)


        #TreeView Presença
        self.ata_presencaList = ttk.Treeview(win, columns=(1,2,3,4,5), show='headings')
        self.verscrlbar = ttk.Scrollbar(win,orient="vertical", command=self.ata_presencaList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.ata_presencaList.configure(yscrollcommand = self.verscrlbar.set)

        self.ata_presencaList.heading(1, text='ID')
        self.ata_presencaList.heading(2, text='N°AP')
        self.ata_presencaList.heading(3, text='Nome Morador')
        self.ata_presencaList.heading(4, text='Tema')
        self.ata_presencaList.heading(5, text='Presente/Ausente')

        self.ata_presencaList.column(1, minwidth=0, width=0)
        self.ata_presencaList.column(2, minwidth=0, width=50) 
        self.ata_presencaList.column(3, minwidth=0, width=115)
        self.ata_presencaList.column(4, minwidth=0, width=100)
        self.ata_presencaList.column(5, minwidth=0, width=135)
        self.ata_presencaList.pack()

        self.ata_presencaList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked_Presenca)

        #Posicionar List e scroll
        self.ata_presencaList.place(x=280,y=55, height= 185)
        self.verscrlbar.place(x=665,y=80, height=159)

        #self.carregar_dados_iniciais()

        self.carregar_dados_iniciais_Ata()

        #Botoes
        #Ata
        self.btnCadastrar.place(x=10,y=235)
        self.btnAlterar.place(x=80,y=235)
        self.btnExcluir.place(x=150,y=235)

        #Presença
        self.btnConfirma.place(x=475,y=28)
        self.btnAlterarP.place(x=550,y=28)
        self.btnExcluirP.place(x=625,y=28)

    #Codigos parte ATA
    #Popular combo do tema que sera usado tanto para cadastrar o assunto como também para registrar a presença
    def popular_combo_Ata(self):
        tema = Ata_Reuniao() 

        self.temaResult = tema.consultar_reuniao() 
        if (len(self.temaResult)> 0):
            self.temaSelected = self.temaResult[0][0] 

            for registro in self.temaResult:
                self.temaCombo['values']=(*self.temaCombo['values'],registro[2])     
            self.temaCombo.current(0)

    
    def _on_combo_changed_Tema(self, event):
        index = self.temaCombo.current()
        self.temaSelected = self.temaResult[index][0]
        self.carregar_dados_iniciais_Ata()


    #Carregando os novos dados
    def carregar_dados_iniciais_Ata(self):
        if (self.temaSelected != None):
            resultado = self.ata_reuniaoCRUD.consultar_por_reuniao(self.temaSelected) 
            self.ata_reuniaoList.delete(*self.ata_reuniaoList.get_children())

            count = 0 
            for registro in resultado:
                self.ata_reuniaoList.insert('', 'end',iid=count,values=(str(registro[0]),(registro[1])))
                count = count + 1

            resultado = self.ata_reuniaoCRUD.consultar_por_reuniao_presenca(self.temaSelected) 
            self.ata_presencaList.delete(*self.ata_presencaList.get_children())

            count = 0 
            for registro in resultado:
                self.ata_presencaList.insert('', 'end',iid=count,values=(str(registro[4]),str(registro[0]),(registro[1]),(registro[2]),registro[3]))
                count = count + 1


   #mMostrar condigos nos campos
    def _on_mostrar_clicked_Ata(self, event):
        selection = self.ata_reuniaoList.selection()
        item = self.ata_reuniaoList.item(selection[0])

        assunto = item["values"][1]

        self.assuntoEdit.delete(1.0,tk.END)
        self.assuntoEdit.insert(1.0,assunto)
    

    #Cadastrando Assunto
    def _on_cadastrar_clicked(self):
        ata_assunto = self.assuntoEdit.get(1.0, END) 

        if self.ata_reuniaoCRUD.cadastrar(ata_assunto,self.temaSelected):

            mb.showinfo("Mensagem", "Registro executado com sucesso!")
            self.assuntoEdit.delete(1.0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no Registro!") 
            self.assuntoEdit.focus_set()   

        self.carregar_dados_iniciais_Ata()     


    #Atuazalizando Assunto
    def _on_atualizar_clicked(self):
        linhaSelecionada = self.ata_reuniaoList.selection()
        if (len(linhaSelecionada) != 0 ): 
            id_reuniao = self.ata_reuniaoList.item(linhaSelecionada[0])["values"][0]   
            ata_assunto = self.assuntoEdit.get(1.0,tk.END)
            reuniao_id = self.temaSelected


            if self.ata_reuniaoCRUD.atualizar(id_reuniao, ata_assunto,reuniao_id):

                self.ata_reuniaoList.item(self.ata_reuniaoList.focus(), values=(str(id_reuniao),ata_assunto)) 

                
                mb.showinfo("Mensagem", "Alteração executado com sucesso!")
                self.assuntoEdit.delete(1.0,tk.END) 
            else:
                mb.showinfo("Mensagem", "Erro no alteração!")
                self.assuntoEdit.focus_set() 

        self.carregar_dados_iniciais_Ata()


    #Deletando Assunto
    def _on_deletar_clicked(self):
        linhaSelecionada = self.ata_reuniaoList.selection()

        if  len(linhaSelecionada) != 0:
            id_assunto = self.ata_reuniaoList.item(linhaSelecionada[0])["values"][0]

            if  self.ata_reuniaoCRUD.excluir(id_assunto):
                self.ata_reuniaoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.assuntoEdit.delete(1.0,tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.assuntoEdit.focus_set()


    #Codigos parte Presença  

    #Populando combo do numero do apartamento
    def popular_combo_apartamento(self):
        apartamento = Ata_Reuniao() 

        self.apartamentoResult = apartamento.consultar_condominos() 
        if (len(self.apartamentoResult)> 0):
            self.apartamentoSelected = self.apartamentoResult[0][0] #1 e do campo que deseja ser salvo

            for registro in self.apartamentoResult:
                self.apartamentoCombo['values']=(*self.apartamentoCombo['values'],registro[1])       
            self.apartamentoCombo.current(0)


    def _on_combo_changed_ap(self, event):
        index = self.apartamentoCombo.current()
        self.apartamentoSelected = self.apartamentoResult[index][0]



    #Mostrar dados no campo presenca
    def _on_mostrar_clicked_Presenca(self, event):
        selection = self.ata_presencaList.selection()
        item = self.ata_presencaList.item(selection[0])

        presenca = item["values"][4]

        self.presencaCombo.delete(0,tk.END)
        self.presencaCombo.insert(0,presenca)


    #Confirmando Presenca
    def _on_confirma_clicked(self):
        presenca = self.presencaCombo.get()

        if self.ata_reuniaoCRUD.confirma(presenca,self.apartamentoSelected,self.temaSelected) == True:
     
            mb.showinfo("Mensagem", "Registro executado com sucesso!")

            self.presencaCombo.delete(0,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no Registro!")
            self.presencaCombo.focus_set()

        self.carregar_dados_iniciais_Ata()


    #Alterando Presença
    def _on_alterar_clicked(self):
        linhaSelecionada = self.ata_presencaList.selection()
        if (len(linhaSelecionada) != 0 ): 
            id_presenca = self.ata_presencaList.item(linhaSelecionada[0])["values"][0]  
            presenca = self.presencaCombo.get() 
            reuniao_id = self.temaSelected
            apartamento_id = self.apartamentoSelected


            if self.ata_reuniaoCRUD.atualizarP(id_presenca,presenca,reuniao_id,apartamento_id ):

                
                mb.showinfo("Mensagem", "Alteração executado com sucesso!")
                self.presencaCombo.delete(0,tk.END) 
            else:
                mb.showinfo("Mensagem", "Erro no alteração!")
                self.presencaCombo.focus_set() 

        self.carregar_dados_iniciais_Ata()


    #Excluindo Presença
    def _on_excluir_clicked(self):
        linhaSelecionada = self.ata_presencaList.selection()

        if  len(linhaSelecionada) != 0:
            id_presenca = self.ata_presencaList.item(linhaSelecionada[0])["values"][0]

            if  self.ata_reuniaoCRUD.excluirP(id_presenca):
                self.ata_presencaList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.presencaCombo.delete(0,tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.presencaCombo.focus_set()


    #Janela
    
janela = tk.Tk()
principal = Ata_ReuniaoView(janela)
janela.title(" Ata de reuniao | Presença")
janela.geometry("700x270+0+0")
janela.resizable(False, False)
janela.mainloop()

