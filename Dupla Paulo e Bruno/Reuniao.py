from typing import cast
from Banco import Banco

import sqlite3
from datetime import date

class Reuniao(object):

    def __init__(self, reuniId = 0, dateData = date, txtHorario = "", txtNome = "", txtTema="", txtLocal = ""):
        self.reuni_id = reuniId
        self.reuni_data = dateData
        self.reuni_horario = txtHorario
        self.reuni_nome = txtNome
        self.reuni_tema = txtTema
        self.reuni_local = txtLocal
    
    def insertReuniao(self):
        banco = Banco()

        try:
            sqlInsert = "insert into reuniao(reuni_data, reuni_horario, reuni_nome, reuni_tema, reuni_local) values (?,?,?,?,?)"
            dataTuple = (self.reuni_data.strftime("%Y-%m-%d"), self.reuni_horario, self.reuni_nome, self.reuni_tema, self.reuni_local)
            c = banco.conexao.cursor()
            c.execute(sqlInsert, dataTuple)
            banco.conexao.commit()
            c.close()

            return "Reunião cadastrada com sucesso!"
        except sqlite3.Error as erro:
            return "Ocorreu um erro na inserção da reunião.", erro
    
    def updateReuniao(self):
        banco = Banco()

        try:
            sqlUpdate = "update reuniao set reuni_data=?, reuni_horario=?, reuni_nome=?, reuni_tema=?, reuni_local=? where reuni_id=?"
            dataTuple = (self.reuni_data, self.reuni_horario, self.reuni_nome, self.reuni_tema, self.reuni_local, self.reuni_id)
            c = banco.conexao.cursor()
            c.execute(sqlUpdate, dataTuple)
            banco.conexao.commit()
            c.close()

            return "Reunião atualizada com sucesso!"
        except sqlite3.Error as erro:
                return "Ocorreu um erro na update da reunião.", erro
    
    
    def findAllReuniao():
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select reuni_id, reuni_data, reuni_horario, reuni_nome, reuni_tema, reuni_local from reuniao")
            records = c.fetchall()
            reunioes = []
            for row in records:
                reunioes.append(Reuniao(row[0], row[1], row[2], row[3],  row[4], row[5]))
                
            c.close()
        except sqlite3.Error as erro:
            return []

    def deleteReuniao(self):
        banco = Banco()

        try:
            sqlUpdate = "delete from reuniao reuni_id=?"
            dataTuple = (self.reuni_id)
            c = banco.conexao.cursor()
            c.execute(sqlUpdate, dataTuple)
            banco.conexao.commit()
            c.close()

            return "Reunião apagada com sucesso!"
        except sqlite3.Error as erro:
                return "Ocorreu um erro na delete da reunião.", erro