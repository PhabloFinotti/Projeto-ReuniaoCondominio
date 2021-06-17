from typing import cast
from Banco import Conexao

import sqlite3
from datetime import datetime


class Reuniao:

    # def __init__(self, reuniId=0, dateData=datetime, txtNome="", txtTema="", txtLocal=""):
    # self.reuni_id = reuniId
    # self.reuni_data = dateData
    # self.reuni_nome = txtNome
    # self.reuni_tema = txtTema
    # self.reuni_local = txtLocal


    
    def criar(self):
        conn = Conexao()

        conn.createTables()

    def insertReuniao(self, date, tema, local):

        self.reuni_tema = tema
        self.reuni_local = local
        self.reuni_data = date

        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()
            sqlInsert = "insert into reuniao( reuni_data, reuni_tema, reuni_local) values ( '"+ self.reuni_data +"', '"+ self.reuni_tema +"', '"+ self.reuni_local +"' )"
            # dataTuple = (self.reuni_tema, self.reuni_local)


            cursor.execute( sqlInsert )

            conexao.commit()

            cursor.close()

            conexao.close()

            # return True

            return "Reunião cadastrada com sucesso!"
        except sqlite3.Error as erro:
            return "Ocorreu um erro na inserção da reunião.", erro

    def updateReuniao(self, id="", date="", tema="", local=""):

        self.reuni_id = id
        self.reuni_tema = tema
        self.reuni_local = local
        self.reuni_data = date


        banco = Conexao()

        try:
            # sqlUpdate = "update reuniao set reuni_data='"+self.reuni_data+"', reuni_tema='"+self.reuni_tema+"', reuni_local='"+self.reuni_local+"' where reuni_id='"+self.reuni_id+"'"
            sqlUpdate = "update reuniao set reuni_tema='"+self.reuni_tema+"' where reuni_id = '", self.reuni_id ,"'"
            # dataTuple = (self.reuni_data, self.reuni_tema, self.reuni_local, self.reuni_id)
            c = banco.conexao.cursor()
            c.execute(sqlUpdate)
            banco.conexao.commit()
            c.close()

            return "Reunião atualizada com sucesso!"
        except sqlite3.Error as erro:
            return "Ocorreu um erro na update da reunião.", erro

    def findAllReuniao():
        banco = Conexao()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "select reuni_id, reuni_data, reuni_horario, reuni_nome, reuni_tema, reuni_local, reuni_condominio from reuniao")
            records = c.fetchall()
            reunioes = []
            for row in records:
                reunioes.append(
                    Reuniao(row[0], row[1], row[2], row[3],  row[4], row[5], row[6]))

            c.close()
        except sqlite3.Error as erro:
            return []

    def deleteReuniao(self):
        banco = Conexao()

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

    def consultar_reuniao(self):
        conn = Conexao()

        conexao = conn.conectar()

        cursor = conexao.cursor()

        sql = "SELECT * FROM reuniao"

        resultado = cursor.execute(sql).fetchall()

        cursor.close()

        conexao.close()

        return resultado