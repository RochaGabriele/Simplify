'''
Created on 18 de nov de 2019

@author: jeff
'''
from Conexao import Conexao
from PegarDados import PegarDados
import mysql.connector
from modelo.graficoDois import graficoDois
class graphDoisControle():
    def remover(self,id):
            try:
                con = Conexao()
                cursor = con.getCon().cursor()
                sql = "DELETE FROM graficos1 WHERE id=:id;"
                cursor.execute(sql)
                con.getCon.commit()
                if con.execute():
                    return True
                else:
                    return False
                
            except mysql.connector.Error as e:
                print("Erro:",e)
            except Exception as e:
                print("Erro geral:",e) 
              
    def inserir(self,evt):
            peg = PegarDados()
            try:
                con = Conexao()#instância da classe Conexao
               
            except mysql.connector.Error as e:
                print("Erro ao conectar no banco:",e)
                return False
            except Exception as e:
                print("Erro geral:",e)
                return False
            
    def selecionarPid(self,id):
        pass