import mysql.connector

class Conexao():
    __con = ''
    def getCon(self):
        return self.__con
    def setCon(self, con):
        self.con = con
    def fecharConexao(self):
        self.con = None
        
    def __init__(self):
        try:
            usr = "root"
            senha = "123456"
            hst = "localhost"
            bd = "Simplify"
            self.setCon(mysql.connector.connect(user = usr,password = senha,database = bd,host = hst))
        except mysql.connector.Error as e:
            print("erro ao conectar com o banco:", e)
        except Exception as e:
            print("Erro geral")
    