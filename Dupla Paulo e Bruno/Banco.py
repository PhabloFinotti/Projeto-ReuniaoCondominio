import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists reuniao(
                        reuni_id integer primary key autoincrement,
                        reuni_data datetime,
                        reuni_condominos varchar(50), 
                        reuni_horario varchar(20),
                        reuni_nome varchar(50),
                        reuni_tema varchar(50),
                        reuni_local varchar(50))""")
        
        self.conexao.commit()
        c.close()