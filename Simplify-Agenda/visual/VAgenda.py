import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from controle.agendaControle import agendaControle
from modelo.agendaMo import agendaMo
from controle.dados import dados
class VAgenda():
    def __init__(self):
        builder = Gtk.Builder()
        "JANELA CALENDARIO PRINCIPAL"
        builder.add_from_file("Agenda.glade")
        self.janela = builder.get_object("Age")
        self.calen = builder.get_object("calAge")
        self.defOrd = builder.get_object("defO")
        self.verOrd = builder.get_object("verO")
        self.apagOrd = builder.get_object("apagO")
        self.defAE = builder.get_object("defA")
        self.verAE = builder.get_object("verA")
        self.apagAE = builder.get_object("apagA")
        
        "JANELA PARA DEFINIR ORDEM DAS SALAS"
        self.defSal = builder.get_object("Sal")
        self.labDPri = builder.get_object("lbDpri")
        self.labDSeg = builder.get_object("lbDSeg")
        self.labDTer = builder.get_object("lbDTer")
        self.labDQuar = builder.get_object("lbDQuar")
        self.labDQuin = builder.get_object("lbDQuin")
        self.labDSex = builder.get_object("lbDSex")
        self.labDSet = builder.get_object("lbDSet")
        self.ladDOi = builder.get_object("lbDOi")
        self.labDNo = builder.get_object("lbDNo")
        self.box1 = builder.get_object("cb1")
        self.box2 = builder.get_object("cb2")
        self.box3 = builder.get_object("cb3")
        self.box4 = builder.get_object("cb4")
        self.box5 = builder.get_object("cb5")
        self.box6 = builder.get_object("cb6")
        self.box7 = builder.get_object("cb7")
        self.box8 = builder.get_object("cb8")
        self.box9 = builder.get_object("cb9")
        self.okS = builder.get_object("btOk")
        self.canS = builder.get_object("btCan")
        
        "JANELA PARA VER ORDEM DAS SALAS"
        self.verSal = builder.get_object("Tab")
        self.priS = builder.get_object("lbVPri")
        self.segS = builder.get_object("lbVSeg")
        self.terS = builder.get_object("lbVTer")
        self.quarS = builder.get_object("lbVQuar")
        self.quinS = builder.get_object("lbVQuin")
        self.sexS = builder.get_object("lbVSex")
        self.setS = builder.get_object("lbVSet")
        self.oiS = builder.get_object("lbVOi")
        self.noS = builder.get_object("lbVNo")
        self.fecS = builder.get_object("btfecS")
        self.lab1 = builder.get_object("lb1")
        self.lab2 = builder.get_object("lb2")
        self.lab3 = builder.get_object("lb3")
        self.lab4 = builder.get_object("lb4")
        self.lab5 = builder.get_object("lb5")
        self.lab6 = builder.get_object("lb6")
        self.lab7 = builder.get_object("lb7")
        self.lab8 = builder.get_object("lb8")
        self.lab9 = builder.get_object("lb9")
        
        "JANELA PARA APAGAR ORDEM DAS SALAS"
        self.apagSal = builder.get_object("Apag")
        self.cert = builder.get_object("lbCer")
        self.si = builder.get_object("btCS")
        self.no = builder .get_object("btCN")
        
        "JANELA PARA DEFINIR ALUNOS EDUCADORES"
        self.dAES = builder.get_object("IAE")
        self.labA1 = builder.get_object("lbA1")
        self.labA2 = builder.get_object("lbA2")
        self.labA3 = builder.get_object("lbA3")
        self.labA4 = builder.get_object("lbA4")
        self.labA5 = builder.get_object("lbA5")
        self.labA6 = builder.get_object("lbA6")
        self.labA7 = builder.get_object("lbA7")
        self.labA8 = builder.get_object("lbA8")
        self.labA9 = builder.get_object("lbA9")
        self.tfi1 = builder.get_object("tfA1")
        self.tfi2 = builder.get_object("tfA2")
        self.tfi3 = builder.get_object("tfA3")
        self.tfi4 = builder.get_object("tfA4")
        self.tfi5 = builder.get_object("tfA5")
        self.tfi6 = builder.get_object("tfA6")
        self.tfi7 = builder.get_object("tfA7")
        self.tfi8 = builder.get_object("tfA8")
        self.tfi9 = builder.get_object("tfA9")
        self.okA = builder.get_object("btOkA")
        self.canA = builder.get_object("btCanA")
        
        "JANELA PARA VER AES"
        self.vAE = builder.get_object("LAE")
        self.labAE = builder.get_object("lbAE")
        self.labAS1 = builder.get_object("lbAS1")
        self.labAS2 = builder.get_object("lbAS2")
        self.labAS3 = builder.get_object("lbAS3")
        self.labAS4 = builder.get_object("lbAS4")
        self.labAS5 = builder.get_object("lbAS5")
        self.labAS6 = builder.get_object("lbAS6")
        self.labAS7 = builder.get_object("lbAS7")
        self.labAS8 = builder.get_object("lbAS8")
        self.labAS9 = builder.get_object("lbAS9")
        self.labAE1 = builder.get_object("lbAE1")
        self.labAE2 = builder.get_object("lbAE2")
        self.labAE3 = builder.get_object("lbAE3")
        self.labAE4 = builder.get_object("lbAE4")
        self.labAE5 = builder.get_object("lbAE5")
        self.labAE6 = builder.get_object("lbAE6")
        self.labAE7 = builder.get_object("lbAE7")
        self.labAE8 = builder.get_object("lbAE8")
        self.labAE9 = builder.get_object("lbAE9")
        self.fecAE = builder.get_object("btfecA")
        
        "JANELA PARA APAGAR AES"
        self.apagarAE = builder.get_object("Apag2")
        self.labApagA = builder.get_object("lbAEP")
        self.AESi = builder.get_object("btAES")
        self.AENo = builder.get_object("btAEN")
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()
        Gtk.main_quit()
    
        "METODOS E SINAIS"
        "SINAIS PARA JANELA DE DEFINIR ORDEM"
    def definirO(self,evt):
        self.defSal.show_all()
    def cancelarO(self,evt):
        self.defSal.hide()
    def okO(self,evt):
        pegar = dados()
        self.defSal.hide()
        pegar.salas(self.box1.get_active_text(),self.box2.get_active_text(),self.box3.get_active_text(),
        self.box4.get_active_text(),self.box5.get_active_text(),self.box6.get_active_text(),self.box7.get_active_text(),
        self.box8.get_active_text(),self.box9.get_active_text())
        
        try:
            am = agendaMo()
            am.setpriSala(self.box1.get_active_text())
            am.setsegSala(self.box2.get_active_text())
            am.setterSala(self.box3.get_active_text())
            am.setquarSala(self.box4.get_active_text())
            am.setquinSala(self.box5.get_active_text())
            am.setsexSala(self.box6.get_active_text())
            am.setsetSala(self.box7.get_active_text())
            am.setoiSala(self.box8.get_active_text())
            am.setnoSala(self.box9.get_active_text())
            control = agendaControle()
            if control.inserirSal(am,evt):
                self.defSal.hide()
        except Exception as e:
            print("Erro geral:",str(e))       
        
        "SINAIS PARA JANELA DE VER ORDEM"
    def verO(self,evt):
        self.verSal.show_all()
        control = agendaControle()
        tes = control.selectSal()
        print(tes)
        for i in range(0,tes.__len__(),1):
            self.lab1.set_text(tes[i].getpriSala())
            self.lab2.set_text(tes[i].getsegSala())
            self.lab3.set_text(tes[i].getterSala())
            self.lab4.set_text(tes[i].getquarSala())
            self.lab5.set_text(tes[i].getquinSala())
            self.lab6.set_text(tes[i].getsexSala())
            self.lab7.set_text(tes[i].getsetSala())
            self.lab8.set_text(tes[i].getoiSala())
            self.lab9.set_text(tes[i].getnoSala())
        self.verSal.hide()
    def fecharO(self,evt):
        self.verSal.hide()
        "SINAIS PARA JANELA APAGAR ORDEM"
    def apagarO(self,evt):
        self.apagSal.show_all()
    def SiS(self,evt):
        self.apagSal.hide()
    def NoS(self,evt):
        self.apagSal.hide()
        "SINAIS PARA JANELA DE DEFINIR AES"
    def definirAE(self,evt):
        self.dAES.show_all()
    def CanAE(self,evt):
        self.dAES.hide()
        self.tfi1.set_active_text("")
        self.tfi2.set_active_text("")
        self.tfi3.set_active_text("")
        self.tfi4.set_active_text("")
        self.tfi5.set_active_text("")
        self.tfi6.set_active_text("")
        self.tfi7.set_active_text("")
        self.tfi8.set_active_text("")
        self.tfi9.set_active_text("")
    def OkAE(self,evt):
        "SINAIS PARA JANELA DE VER AES"
    def verAES(self,evt):
        self.vAE.show_all()
    def fecAES(self,evt):
        self.vAE.hide()
        "SINAIS PARA JANELAS DE APAGAR AES"
    def apagAES(self,evt):
        self.apagarAE.show_all()
    def simAES(self,evt):
        self.apagarAE.hide()
    def naoAES(self,evt):
        self.apagarAE.hide()
vag = VAgenda()   
