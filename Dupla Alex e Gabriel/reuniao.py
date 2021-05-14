import sqlite3
from conexao import Conexao 

class Reuniao:

    def cadastrar(self,ata_tema,ata_assuntos):
        try:
            conn = Conexao()    
            conexao = conn.conectar() 
            cursor = conexao.cursor()

            sql = 'INSERT INTO Reuniao (ata_tema, ata_assuntos) VALUES (?,?)'
            cursor.execute(sql,[ata_tema,ata_assuntos])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True

        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False
        

    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM Reuniao"
        resultado = cursor.execute(sql).fetchall()

        cursor.close()
        conexao.close()
        return resultado



    