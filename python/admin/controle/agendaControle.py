'''
@author: José Maik
'''


import mysql.connector

from admin.controle.Conexao import Conexao
from admin.modelo.agendaMo import agendaMo


class agendaControle():
   
    def selectSal(self):
            dados = ""
            try:
                con = Conexao()
                sql = "SELECT * FROM Agenda;"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    agendaM = agendaMo()
                    agendaM.setpriSala(consulta[i]['PrimeiraSala'])
                    agendaM.setsegSala(consulta[i]['SegundaSala'])
                    agendaM.setterSala(consulta[i]['TerceiraSala'])
                    agendaM.setquarSala(consulta[i]['QuartaSala'])
                    agendaM.setquinSala(consulta[i]['QuintaSala'])
                    agendaM.setsexSala(consulta[i]['SextaSala'])
                    agendaM.setsetSala(consulta[i]['SetimoSala'])
                    agendaM.setoiSala(consulta[i]['OitavaSala'])
                    agendaM.setnoSala(consulta[i]['NonaSala'])
                    dados.append(agendaM)
                   
            except mysql.connector.Error as e:
                print("Erro no mysql:",str(e))
            except Exception as e:
                print("Erro:",str(e))
            return dados
        
    def removerSal(self,agendaMo):
        try:
            con = Conexao()
            iDSal = agendaMo.getidSal()
            cursor = con.getCon().cursor()
            sql = "DELETE PrimeiraSala,SegundaSala,TerceiraSala,QuartaSala,QuintaSala,SextaSala,OitavaSala,NonaSala FROM Agenda WHERE Id = Id;"
            valorSal = (iDSal)
            cursor.execute(sql,valorSal)
            con.getCon.commit()
            if con.execute():
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print("Erro:",e)
        except Exception as e:
            print("Erro geral:",e) 
   
        
    def inserirSal(self,agendaMo,evt):
        try:
            con = Conexao()
            PrimSala = agendaMo.getpriSala()
            SeguSala = agendaMo.getsegSala()
            TercSala = agendaMo.getterSala()
            QuarSala = agendaMo.getquarSala()
            QuintSala = agendaMo.getquinSala()
            SextSala = agendaMo.getsexSala()
            SetSala = agendaMo.getsetSala()
            OitaSala = agendaMo.getoiSala()
            NonSala = agendaMo.getnoSala()
            sql = "INSERT INTO Agenda(PrimeiraSala,SegundaSala,TerceiraSala,QuartaSala,QuintaSala,SextaSala,SetimoSala,OitavaSala,NonaSala) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor = con.getCon().cursor()
            valores = (PrimSala,SeguSala,TercSala,QuarSala,QuintSala,SextSala,SetSala,OitaSala,NonSala)
            cursor.execute(sql,valores)
            con.getCon().commit()
            return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",str(e))
        except Exception as e:
            print("Erro geral:",str(e))
            
    def inserirAe(self,agendaMo,evt):
        try:
            con = Conexao()
            primAe = agendaMo.getpriAE()
            segumAe = agendaMo.getsegAE()
            terceAe = agendaMo.getterAE()
            quarAe = agendaMo.getquarAE()
            quiAe = agendaMo.getquiAE()
            sexAe = agendaMo.getsexAE()
            setAe = agendaMo.getsetAE()
            oitAe = agendaMo.getoiAE()
            nonAe = agendaMo.getnoAE() 
            sql = "INSERT INTO Aes(PrimeiroAE,SegundoAE,TerceiroAE,QuartoAE,QuintoAE,SextoAE,SetimoAE,OitavoAE,NonoAE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor = con.getCon().cursor()
            valores = (primAe,segumAe,terceAe,quarAe,quiAe,sexAe,setAe,oitAe,nonAe)
            cursor.execute(sql,valores)
            con.getCon().commit()
            return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",str(e))
        except Exception as e:
            print("Erro geral:",str(e))    
    
    def selecionarAes(self):
            dados = ""
            try:
                con = Conexao()
                sql = "SELECT * FROM Aes;"
                cursor = con.getCon().cursor(dictionary=True)
                dados = []
                cursor.execute(sql)
                consulta = cursor.fetchall()
                for i in range(0,consulta.__len__(),1):
                    agendaM = agendaMo()
                    agendaM.setpriAE(consulta[i]['PrimeiroAE'])
                    agendaM.setsegAE(consulta[i]['SegundoAE'])
                    agendaM.setterAE(consulta[i]['TerceiroAE'])
                    agendaM.setquarAE(consulta[i]['QuartoAE'])
                    agendaM.setquiAE(consulta[i]['QuintoAE'])
                    agendaM.setsexAE(consulta[i]['SextoAE'])
                    agendaM.setsetAE(consulta[i]['SetimoAE'])
                    agendaM.setoiAE(consulta[i]['OitavoAE'])
                    agendaM.setnoAE(consulta[i]['NonoAe'])
                    dados.append(agendaM)
            except mysql.connector.Error as e:
                print("Erro no mysql:",str(e))
            except Exception as e:
                print("Erro:",str(e))
            return dados
    def removerAES(self):
        try:
            con = Conexao()
            iDAE = agendaMo.getidAE()
            cursor = con.getCon().cursor()
            sql = "DELETE PrimeiroAE,SegundoAE,TerceiroAE,QuartoAE,QuintoAE,SextoAE,OitavoAE,NonoAE FROM Agenda WHERE Id = Id;"
            valorAE = (iDAE)
            cursor.execute(sql,valorAE)
            con.getCon.commit()
            if con.execute():
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print("Erro:",e)
        except Exception as e:
            print("Erro geral:",e) 
    
   
            
