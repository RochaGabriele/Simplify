from modelo.agendaMo import agendaMo
from controle.Conexao import Conexao
import mysql.connector
class agendaControle():
    def selectSal(self):
        dadosSal = ""
        try:
            con = Conexao()
            cursor = con.getCon().cursor(dictionary=True)
            sql = "SELECT * FROM Agenda;"
            dadosSal = []
            cursor.execute(sql)
            consultaSal = cursor.fetchall()
            for i in range(0,consultaSal.__len__(),1):
                agendaMo = agendaMo()
                agendaMo.setpriSala(consultaSal[i]['PrimeiraSala'])
                agendaMo.setsegSala(consultaSal[i]['SegundaSala'])
                agendaMo.setterSala(consultaSal[i]['TerceiraSala'])
                agendaMo.setquarSala(consultaSal[i]['QuartaSala'])
                agendaMo.setquinSala(consultaSal[i]['QuintaSala'])
                agendaMo.setsexSala(consultaSal[i]['SextaSala'])
                agendaMo.setsetSala(consultaSal[i]['SetimaSala'])
                agendaMo.setoiSala(consultaSal[i]['OitavaSala'])
                agendaMo.setnoSala(consultaSal[i]['NonaSala'])
                dadosSal.append(agendaMo)
                print(consultaSal)
        except mysql.connector.Error as e:
            print("Erro no mysql", str(e))
        except Exception as e:
            print("Erro geral", str(e))
        return dadosSal
        print(dadosSal)
    def removerSal(self,agendaMo):
        try:
            con = Conexao()
            iDSal = agendaMo.getidSal()
            cursor = con.getCon().cursor()
            sql = "DELETE PrimeiraSala,SegundaSala,TerceiraSala,QuartaSala,QuintaSala,SextaSala,OitavaSala,NonaSala FROM Agenda WHERE Id = Id"
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
            OitaSala = agendaMo.getoiSala()
            NonSala = agendaMo.getnoSala()
            sql = "INSERT INTO Agenda(PrimeiraSala,SegundaSala,TerceiraSala,QuartaSala,QuintaSala,SextaSala,SetimaSala,OitavaSala,NonaSala) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor  = con.getCon().cursor()
            valores = (PrimSala,SeguSala,TercSala,QuarSala,QuintSala,SextSala,OitaSala,NonSala)
            cursor.execute(sql,valores)
            con.getCon().commit()
            return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",str(e))
            return False
        except Exception as e:
            print("Erro geral:",str(e))
            return False
        
        
    def selectAES(self):
        dadosAE = ""
        try:
            con = Conexao()
            cursor = con.getCon().cursor(dictionary=True)
            sql = "SELECT PrimeiroAE,SegundoAE,TerceiroAE,QuartoAE,QuintoAE,SextoAE,SetimoAE,OitavoAE,NonoAE FROM Agenda;"
            dadosAE = []
            consultaAE = cursor.fetchall()
            cursor.execute(sql)
            for j in range(0,consultaAE.__len__(),1):
                agendaMo = agendaMo()
                agendaMo.setpriAE(consultaAE[j]['PrimeiroAE'])
                agendaMo.setsegAE(consultaAE[j]['SegundoAE'])
                agendaMo.setterAE(consultaAE[j]['TerceiroAE'])
                agendaMo.setquarAE(consultaAE[j]['QuartoAE'])
                agendaMo.setquinAE(consultaAE[j]['QuintoAE'])
                agendaMo.setsexAE(consultaAE[j]['SextoAE'])
                agendaMo.setsetAE(consultaAE[j]['SetimoAE'])
                agendaMo.setoiAE(consultaAE[j]['OitavoAE'])
                agendaMo.setnoAE(consultaAE[j]['NonoAE'])
                dadosAE.append(agendaMo)
        except mysql.connector.Error as e:
            print("Erro no mysql", str(e))
        except Exception as e:
            print("Erro geral", str(e))
        return dadosAE    
    def removerAES(self):
        try:
            con = Conexao()
            iDAE = agendaMo.getidAE()
            cursor = con.getCon().cursor()
            sql = "DELETE PrimeiroAE,SegundoAE,TerceiroAE,QuartoAE,QuintoAE,SextoAE,OitavoAE,NonoAE FROM Agenda WHERE Id = Id"
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
    
    def inserirAES(self):
        try:
            con = Conexao()
            PrimAE = agendaMo.getpriAE()
            SeguAE = agendaMo.getsegAE()
            TercAE = agendaMo.getterAE()
            QuarAE = agendaMo.getquarAE()
            QuintAE = agendaMo.getquinAE()
            SextAE = agendaMo.getsexAE()
            OitAE = agendaMo.getoiAE()
            NonAE = agendaMo.getnoAE()
            sql = "INSERT INTO (PrimeiroAE,SegundoAE,TerceiroAE,QuartoAE,QuintoAE,SextoAE,SetimoAE,OitavoAE,NonoAE) VALUES ($s,$s,$s,$s,$s,$s,$s,$s,$s)"
            cursor  = con.getCon().cursor()
            valoresAE = (PrimAE,SeguAE,TercAE,QuarAE,QuintAE,SextAE,OitAE,NonAE)
            cursor.execute(sql,valoresAE)
            cursor.getCon().commit()
            return True
        except mysql.connector.Error as e:
            print("Erro ao conectar no banco:",e)
            return False
        except Exception as e:
            print("Erro geral:",e)
            return False
            