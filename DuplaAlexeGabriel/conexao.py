import sqlite3

class Conexao:
    
    def conectar(self):
        conexao = None 
        db_path = 'banco.db'
        try:
            conexao = sqlite3.connect(db_path)
        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")

        return conexao

    def createTableAtaReuniao(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS ata_reuniao')

        sql = """ CREATE TABLE IF NOT EXISTS ata_reuniao (
                    ata_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ata_reuni_id INTEGER,
                    ata_assunto TEXT,
                    FOREIGN KEY (ata_reuni_id) REFERENCES reuniao (reuni_id));"""
        cursor.execute(sql)
        conexao.commit()

    def createTablePresenca(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS ata_presenca')
        
        sql = """ CREATE TABLE IF NOT EXISTS ata_presenca( 
                    pres_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pres_cond_id INTEGER,
                    pres_reuniao_id INTEGER,
                    pres_ata_id INTEGER,
                    presenca int,
                    FOREIGN KEY (pres_ata_id) REFERENCES ata_reuniao (ata_id),
                    FOREIGN KEY (pres_cond_id) REFERENCES condominos (id),
                    FOREIGN KEY (pres_reuniao_id) REFERENCES reuniao (reuni_id));"""
        cursor.execute(sql)
        conexao.commit()

    def createTableCondominos(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS condominos')

        sql = """create table if not exists condominos (
				    id integer primary key autoincrement ,
				    cond_apartamento int,
				    cond_cpf varchar(14),
				    cond_nome varchar(255),
				    cond_tppessoa varchar(20),
				    cond_rg varchar(20),
				    cond_nascimento date,
				    cond_email varchar(50),
				    cond_telresidencial varchar(11),
				    cond_telcomercial varchar(11),
				    cond_telcelular varchar(11),
				    cond_adimplente bit,
				    cond_data_cadastro datetime);"""
        cursor.execute(sql)
        conexao.commit()

    def createTableReuniao(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS reuniao')

        sql = """ CREATE TABLE IF NOT EXISTS reuniao (
                reuni_id INTEGER PRIMARY KEY AUTOINCREMENT,
                reuni_data DATETIME,
                reuni_tema TEXT,
                reuni_local TEXT);  """
        cursor.execute(sql)
        conexao.commit()
        

    # def createTables(self):

    def __init__(self):
        conexao = self.conectar() 
        cursor = conexao.cursor()

        self.createTableAtaReuniao(conexao, cursor)
        self.createTablePresenca(conexao,cursor)
        self.createTableCondominos(conexao, cursor)
        self.createTableReuniao(conexao,cursor)

