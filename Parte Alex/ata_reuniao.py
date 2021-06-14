import sqlite3
from sqlite3.dbapi2 import Cursor
from conexao import Conexao 

class Ata_Reuniao:

    #Tabela ATA
    def cadastrar(self,ata_assunto,reuniao_id):
        try:
            conn = Conexao()    
            conexao = conn.conectar() 
            cursor = conexao.cursor()

            sql = 'INSERT INTO ata_reuniao (ata_assunto,reuniao_id) VALUES (?,?)'
            cursor.execute(sql,[ata_assunto,reuniao_id])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True

        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False


    def atualizar(self,id_reuniao,ata_assunto,reuniao_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE ata_reuniao SET ata_assunto = ?, reuniao_id = ? WHERE ata_id = (?)'
            cursor.execute(sql,(ata_assunto,reuniao_id, id_reuniao))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,id_reuniao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM ata_reuniao WHERE ata_id = (?)'
            cursor.execute(sql,[id_reuniao])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False




        #except sqlite3.OperationalError as e:
         #   print("Erro na exclusão {}".format(e))
          #  return False
        #except sqlite3.IntegrityError as e:
         #   print("Erro de integridade: {}".format(e))
          #  return False


    def consultar_por_reuniao(self,reuni): #valor que esta chegando por paramentro
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT at.ata_id, at.ata_assunto, at.reuniao_id 
                FROM ata_reuniao as at
                WHERE reuniao_id = ?"""

        try:
            resultset =  cursor.execute(sql,(reuni,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    #Presença

    def confirma(self,presenca,ap,reuniao):
        try:
            conn = Conexao()    
            conexao = conn.conectar() 
            cursor = conexao.cursor()

            sql = 'INSERT INTO ata_presenca (presenca,pres_cond_id, pres_reuniao_id) VALUES (?,?,?)'
            cursor.execute(sql,(presenca,ap,reuniao))

            conexao.commit()
            cursor.close()
            conexao.close()

            return True

        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False

    def atualizarP(self,id_presenca,presenca,reuniao_id,apartamento_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE ata_presenca SET presenca = ?, pres_reuniao_id = ?, pres_cond_id = ? WHERE pres_id = (?)'
            cursor.execute(sql,(presenca, reuniao_id,apartamento_id,id_presenca))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    
    def excluirP(self,id_presenca):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM ata_presenca WHERE pres_id = (?)'
            cursor.execute(sql,[id_presenca])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False

   
# Consultas
    def consultar_por_apartamento(self,cond): #valor que esta chegando por paramentro
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT ap.pres_id, ap.pres_cond_id, pres_reuniao_id, ap.presenca
                FROM ata_presenca as ap
                WHERE pres_cond_id = ?"""

        try:
            resultset =  cursor.execute(sql,(cond,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

    def consultar_presenca(self,id_cond):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        
        sql = """SELECT c.id, c.cond_apartamento, c.cond_nome, p.pres_id, p.presenca  
                FROM condominos as c, ata_presenca as p
                WHERE c.id = ? AND p.pres_id = c.id"""

        
        resultado = cursor.execute(sql,[id_cond]).fetchall()
        
        cursor.close()
        conexao.close()
        return resultado

    def consultar_tabela_presenca(self,cond):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        

        sql = """SELECT cond_apartamento, cond_nome, reuni_tema, presenca FROM reuniao
                    INNER JOIN ata_reuniao on ata_reuni_id=reuni_id
                    INNER JOIN ata_presenca ON pres_ata_id=ata_id
                    INNER JOIN condominos on condominos.id=pres_cond_id
                    WHERE pres_ata_id = ? """

        
        resultado = cursor.execute(sql,(cond,)).fetchall() 
        
        
        cursor.close()
        conexao.close()
        return resultado

    #sql = """SELECT c.cond_apartamento, c.cond_nome, r.reuni_id, r.reuni_tema, r.reuni_local, p.pres_id, p.pres_cond_id, p.pres_reuniao_id, p.presenca
    #            FROM condominos as c, ata_presenca as p, reuniao as r
    #                INNER JOIN ata_reuniao ON
    #                ata_reuni_id=reuni_id
    #                INNER JOIN ata_presenca ON
    #                pres_ata_id = ata_id
    #                INNER JOIN condominos ON
    #                c.id=pres_cond_id;"""


    #Consultas simples
    def consultar_reuniao(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        
        sql = "SELECT * FROM reuniao"
        resultado = cursor.execute(sql).fetchall()

        cursor.close()
        conexao.close()
        return resultado

    def consultar_condominos(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM condominos"
        resultado = cursor.execute(sql).fetchall()

        cursor.close()
        conexao.close()
        return resultado

    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        
        sql = "SELECT * FROM ata_presenca"
        resultado = cursor.execute(sql).fetchall()

        cursor.close()
        conexao.close()
        return resultado


    def criar(self):
        conn = Conexao()
        conn.createTables()
        #conexao =conn.conectar()
        #criar =conexao.createTables()

        #return criar