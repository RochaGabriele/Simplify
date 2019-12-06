'''
Created on 18 de nov de 2019

@author: jeff
'''
from controle.Conexao import Conexao
from controle.PegarDados import PegarDados
import mysql.connector
from modelo.Admin import Admin
class AdminControle():
    def remover(self,ide):
            try:
                con = Conexao()
                cursor = con.getCon().cursor()
                sql = "DELETE FROM admin WHERE id=:id"
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
    def selecionarTodos(self):
            dados = ""
            try:
                con = Conexao()
                sql = "SELECT * FROM admin"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    admin = Admin()
                    admin.setNome(consulta[i]['nome'])
                    admin.setCargo(consulta[i]['cargo'])
                    admin.setUser(consulta[i]['user'])
                    admin.setSenha(consulta[i]['senha'])
                    dados.append(admin)
            except mysql.connector.Error as e:
                print("Erro no mysql:",str(e))
            except Exception as e:
                print("Erro:",str(e))
            return dados
    '''
    def selecionarUltimo(self):
            dados = ""
            try:
                con = Conexao()
                sql = "SELECT * FROM admin ORDER BY id DESC LIMIT 1"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    admin = Admin()
                    admin.setNome(consulta[i]['nome'])
                    admin.setCargo(consulta[i]['cargo'])
                    admin.setUser(consulta[i]['user'])
                    dados.append(admin)
            except mysql.connector.Error as e:
                print("Erro no mysql:",str(e))
            except Exception as e:
                print("Erro:",str(e))
            return dados                    
       '''         
    def inserir(self,evt):
            peg = PegarDados()
            try:
                con = Conexao()#instância da classe Conexao
                nome = peg.adm.getNome()#nome recebe encapsulamento da modelo Admin que está sendo instânciada na controle pegar dados 
                cargo = peg.adm.getCargo()#os mesmo acontece com as outras variaveis até senha.
                user = peg.adm.getUser()
                senha = peg.adm.getSenha()
                sql = "INSERT INTO admin(nome,cargo,user,senha) VALUES(%s,%s,%s,%s)" #variavel que recebe um comando sql, para poder inserir os dados na tabela do banco        
                cursor  = con.getCon().cursor()#metodo utilizado para direcionar os dados para o banco
                valores = (nome,cargo,user,senha)#valores recebe as váriaveis
                cursor.execute(sql,valores)#executa a variavel sql e valores
                con.getCon().commit()#commit para enviar os dados
                return True
               
            except mysql.connector.Error as e:
                print("Erro ao conectar no banco:",e)
                return False
            except Exception as e:
                print("Erro geral:",e)
                return False
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
