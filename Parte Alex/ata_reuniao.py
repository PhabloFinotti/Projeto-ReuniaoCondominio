import sqlite3
from sqlite3.dbapi2 import Cursor
from conexao import Conexao 

class Ata_Reuniao:

    #Tabela ATA

    #Cadastrando o assunto da Ata
    def cadastrar(self,ata_assunto,reuniao_id):
        try:
            conn = Conexao()    
            conexao = conn.conectar() 
            cursor = conexao.cursor()

            sql = 'INSERT INTO ata_reuniao (ata_assunto,ata_reuni_id) VALUES (?,?)'
            cursor.execute(sql,[ata_assunto,reuniao_id])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True

        except sqlite3.OperationalError as e:
            print("Error {}".format(e))
            return False


    #Atualizar dados do assunto da Ata
    def atualizar(self,id_reuniao,ata_assunto,reuniao_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE ata_reuniao SET ata_assunto = ?, ata_reuni_id = ? WHERE ata_id = (?)'
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


    #Excluir os dados do assunto da Ata
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


    #Consultando pelo id da reuniao
    def consultar_por_reuniao(self,reuni):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT at.ata_id, at.ata_assunto, at.ata_reuni_id 
                FROM ata_reuniao as at
                WHERE ata_reuni_id = ?"""

        try:
            resultset =  cursor.execute(sql,(reuni,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    #Presença

    #Registrando Presença
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


    #Atualizando Presença
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

    
    #Excluindo Presença
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

   
    # Consultando pelo id da reuniao para mostrar dados da tabela presenca

    def consultar_por_reuniao_presenca(self,reuni): #valor que esta chegando por paramentro
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT cond_apartamento, cond_nome, reuni_tema, presenca, pres_id  
                FROM ata_presenca
                INNER JOIN reuniao ON  pres_reuniao_id = reuni_id
                INNER JOIN condominos ON pres_cond_id = id
                WHERE reuni_id = ?"""

        try:
            resultset =  cursor.execute(sql,(reuni,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

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