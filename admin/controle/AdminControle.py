'''
Created on 18 de nov de 2019

@author: jeff
'''
import mysql.connector

from admin.controle.Conexao import Conexao
from admin.modelo.Admin import Admin
from admin.modelo.Aluno import Aluno


class AdminControle():
    def selectUS(self):
            dados = ""
            try:
                con = Conexao()
                cursor = con.getCon().cursor()
                sql = "SELECT * FROM admin;"
                consulta = cursor.fetchall()
                cursor.execute(sql)
                for i in range(0,consulta.__len__(),1):
                    admin = Admin()
                    admin.setUser(consulta[i]['user'])
                    admin.setSenha(consulta[i]['senha'])
                    dados.append(admin)
              
            except mysql.connector.Error as e:
                print("Erro no mysql",str(e))
            except Exception as e:
                print("Erro",str(e))
      
    def remover(self,admin,id):
            try:
                con = Conexao()
                id = admin.getId()
                cursor = con.getCon().cursor()
                sql = "DELETE FROM admin WHERE id = id"
                valor = (id)
                cursor.execute(sql,valor)
                con.getCon().commit()
                if con.execute():
                    return True
                else:
                    return False
                
            except mysql.connector.Error as e:
                print("Erro:",e)
            except Exception as e:
                print("Erro geral:",e) 
    def update(self,Admin):
        try:
            con = Conexao()
            sql = "UPDATE admin SET nome = %s,cargo = %s,user = %s,senha = %s WHERE id = %s;"
            valores = (Admin.getNome(),Admin.getCargo(), Admin.getUser(),Admin.getSenha(),Admin.getId())
            print(valores)
            cursor = con.getCon().cursor()
            cursor.execute(sql,valores)
            if con.getCon().commit() != True:
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print("Erro em mysql", e)
        except Exception as e:
            print("Erro geral", e)
            
            
            
            
    def selectPid(self):
        dados = []
        try:
            con = Conexao()
            sql = "SELECT * FROM admin WHERE id = %s;"
            cursor = con.getCon.cursor(dictionary=True)
            valor = (Admin.getId())
            cursor.execute(sql,valor)
            consulta = cursor.fetchone()
            for i in range(0,consulta.__len_(),1):
                admin = Admin()
                admin.setId(consulta[i]['id'])
                dados.append(admin)
        except mysql.connector.Error as e:
            print("Erro no mysql:",str(e))
        except Exception as e:
            print("Erro geral:",str(e))
            
    def selecionarTodos(self):
            dados = ""
            try:
                con = Conexao()
                sql = "SELECT * FROM admin;"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    admin = Admin()
                    admin.setId(consulta[i]['id'])
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
                
    def inserir(self,Admin,evt):
        try:
                con = Conexao()#instância da classe Conexao
                nome = Admin.getNome()#nome recebe encapsulamento da modelo Admin que está sendo instânciada na controle pegar dados 
                cargo = Admin.getCargo()#O mesmo acontece com as outras variaveis até senha.
                user = Admin.getUser()
                senha = Admin.getSenha()
                sql = "INSERT INTO admin(nome,cargo,user,senha) VALUES(%s,%s,%s,%s);" #variavel que recebe um comando sql, para poder inserir os dados na tabela do banco        
                cursor  = con.getCon().cursor()#metodo utilizado para direcionar os dados para o banco
                valores = (nome,cargo,user,senha)#valores recebe as váriaveis
                cursor.execute(sql,valores)#executa a variavel sql e valores
                con.getCon().commit()#commit para enviar os dados
                return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",str(e))
            return False
        except Exception as e:
            print("Erro geral:",str(e))
            return False
    def inserirAlu(self,Aluno,evt):
        try:
            con = Conexao()
            nome = Aluno.getNomeAlu()
            curso = Aluno.getCurso()
            serie = Aluno.getSerie()
            matricula = Aluno.getMatricula()
            sql = "INSERT INTO alunos(nome,curso,serie,matricula) VALUES(%s,%s,%s,%s);"
            cursor = con.getCon().cursor()
            valores = (nome,curso,serie,matricula)
            cursor.execute(sql,valores)
            con.getCon().commit()
            return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",str(e))
        except Exception as e:
            print("Erro geral:",str(e))
                
                
    def selectInfor(self):
            dados = ""       
            try:
                con = Conexao()
                sql = "SELECT * FROM alunos WHERE curso = 'informatica';"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    aluno = Aluno()
                    aluno.setNomeAlu(consulta[i]['nome'])
                    aluno.setCurso(consulta[i]['curso'])
                    aluno.setSerie(consulta[i]['serie'])
                    aluno.setMatricula(consulta[i]['matricula'])
                    dados.append(aluno)
            except mysql.connector.Error as e:
                    print("Erro no mysql:",str(e))
            except Exception as e:
                    print("Error geral:",str(e))
            return dados
    def selectEnfer(self):     
            dados = ""      
            try:
                con = Conexao()
                sql = "SELECT * FROM alunos WHERE curso = 'enfermagem';"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    aluno = Aluno()
                    aluno.setNomeAlu(consulta[i]['nome'])
                    aluno.setCurso(consulta[i]['curso'])
                    aluno.setSerie(consulta[i]['serie'])
                    aluno.setMatricula(consulta[i]['matricula'])
                    dados.append(aluno)
            except mysql.connector.Error as e:
                    print("Erro no mysql:",str(e))
            except Exception as e:
                    print("Error geral:",str(e))
            return dados           
    def selectEvenTur(self):     
            dados = ""      
            try:
                con = Conexao()
                sql = "SELECT * FROM alunos WHERE curso = 'Turismo/Eventos';"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    aluno = Aluno()
                    aluno.setNomeAlu(consulta[i]['nome'])
                    aluno.setCurso(consulta[i]['curso'])
                    aluno.setSerie(consulta[i]['serie'])
                    aluno.setMatricula(consulta[i]['matricula'])
                    dados.append(aluno)
            except mysql.connector.Error as e:
                    print("Erro no mysql:",str(e))
            except Exception as e:
                    print("Error geral:",str(e))           
            return dados               
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
