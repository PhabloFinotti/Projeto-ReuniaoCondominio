import sqlite3

class Conexao:
    
    def conectar(self):
        conexao = None 
        db_path = 'presença.db'
        try:
            conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")

        return conexao

    def createTableReuniao(self,conexao,cursor):
        sql ='CREATE TABLE IF NOT EXISTS Reuniao ( ata_id INTEGER PRIMARY KEY AUTOINCREMENT, ata_tema varchar, ata_assuntos varchar);'
        cursor.execute(sql)
        conexao.commit()

    def createTablePresenca(self,conexao,cursor):
        sql ='CREATE TABLE IF NOT EXISTS Presença ( press_ata_id INTEGER PRIMARY KEY AUTOINCREMENT, press_cond_id varchar NOT NULL);'
        cursor.execute(sql)
        conexao.commit()

    def createTables(self):
        conexao = self.conectar() 
        cursor = conexao.cursor()

        self.createTableReuniao(conexao, cursor)
        self.createTablePresenca(conexao,cursor)